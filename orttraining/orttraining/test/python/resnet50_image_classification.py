import os
import sys
import time
import torch
import wget
import argparse
from PIL import Image
from torchvision import transforms
import torchvision.models as models
from torch_ort import ORTModule, ProviderConfigs, DebugOptions

def download_labels(labels):
    if not labels:
        labelsUrl = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'
        labels = "imagenet_classes.txt"
        if not os.path.exists(labels):
            # Download the file (if we haven't already)
            wget.download(labelsUrl)
        else:
            print("\nReusing downloaded imagenet labels")

    # Read the categories
    with open(labels, "r") as f:
        categories = [s.strip() for s in f.readlines()]
        return categories

def preprocess(input):
    transform = transforms.Compose([
     transforms.Resize(256),
     transforms.CenterCrop(224),
     transforms.ToTensor(),
     transforms.Normalize(
     mean=[0.485, 0.456, 0.406],
     std=[0.229, 0.224, 0.225]
    )])
    return transform(input)

def predict(model,image,categories):
    # warmup
    for _ in range(5):
        outputs = model(image)

    # Start inference
    t0 = time.time()
    outputs = model(image)
    t1 = time.time() - t0
    print("\nInference time: {:.4f}ms\n".format(t1 * 1000))

    # The output has unnormalized scores. Run a softmax on it for probabilities.
    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    print("Labels , Probabilities:")
    for i in range(top5_prob.size(0)):
        print(categories[top5_catid[i]],top5_prob[i].item())

def main():
    # 1. Basic setup
    parser = argparse.ArgumentParser(description='PyTorch Image Classification Example')
    parser.add_argument('--pytorch-only', action='store_true', default=False,
                        help='disables ONNX Runtime inference')
    parser.add_argument('--labels', type=str, default=None,
                        help="labels file")
    parser.add_argument('--input', type=str, required = True,
                        help="input image")
    parser.add_argument('--provider', type=str, default="openvino",
                        help="Execution Provider")
    parser.add_argument('--backend', type=str, default="CPU",
                        help="Backend name")
    parser.add_argument('--precision', type=str, default="FP32",
                        help="Precision for prediction(Default FP32)")
    parser.add_argument('--export-onnx-graphs', action='store_true', default=False,
                        help='export ONNX graphs to current directory')
    args = parser.parse_args()

    # 2. Download and load the model
    model = models.resnet50(pretrained=True)
    if not args.pytorch_only:
        provider_configs = ProviderConfigs(provider=args.provider, backend=args.backend, precision=args.precision)
        # Just for future debugging
        debug_options = DebugOptions(save_onnx=args.export_onnx_graphs, onnx_prefix='resnet50')
        model = ORTModule(model, provider_configs=provider_configs, debug_options=debug_options)

    # Convert model for evaluation
    model.eval()

    # 3. Download ImageNet labels
    categories = download_labels(args.labels)
    
    # 4. Read input image and preprocess
    if not args.input:
        raise ValueError("Input image not provided!")
    img = Image.open(args.input)
    img_trans = preprocess(img)
    #Adding batch dimension (size 1)
    img_trans = torch.unsqueeze(img_trans, 0)

    # 5. Predict
    predict(model,img_trans,categories)

if __name__ == '__main__':
    main()
