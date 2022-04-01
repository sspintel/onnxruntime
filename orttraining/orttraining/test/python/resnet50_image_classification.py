import sys
import time
import torch
import wget
import argparse
import torchvision.models as models
#from torch_ort import ORTModule, DebugOptions
from torch_ort import ORTModule, ProviderConfigs, DebugOptions
from PIL import Image
from torchvision import transforms

def download_labels(labels):
    if not labels:
        labelsUrl = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'
        wget.download(labelsUrl)
    # Read the categories
        with open("imagenet_classes.txt", "r") as f:
            categories = [s.strip() for s in f.readlines()]
            return categories
    else:
        with open(labels, "r") as f:
            categories = [s.strip() for s in f.readlines()]
            return categories

def preprocess_image(input):
    # preprocessing input image
    transform = transforms.Compose([
     transforms.Resize(256),
     transforms.CenterCrop(224),
     transforms.ToTensor(),
     transforms.Normalize(
     mean=[0.485, 0.456, 0.406],
     std=[0.229, 0.224, 0.225]
    )])
    # Read input image and preprocess
    img = Image.open(input)
    img_trans = transform(img)
    batch = torch.unsqueeze(img_trans, 0)
    return batch

def predict(model,batch,categories):
    # warmup
    for i in range(5):
        start = time.time()
        out = model(batch)
        end = time.time()
        print("warmup time in ms: ", (end-start) * 1000)  

    # Start inference
    for i in range(100):
        start = time.time()
        out = model(batch)
        end = time.time()
        print("Inference time in ms: ", (end-start) * 1000)

    # The output has unnormalized scores. Run a softmax on it for probabilities.
    probabilities = torch.nn.functional.softmax(out[0], dim=0)

    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    print("Labels, Probabilities:")
    for i in range(top5_prob.size(0)):
        print(categories[top5_catid[i]], top5_prob[i].item())
        return

def main():
    # 1. Basic setup
    parser = argparse.ArgumentParser(description='PyTorch Image Classification Example')
    parser.add_argument('--pytorch-only', action='store_true', default=False,
                        help='disables ONNX Runtime training')
    parser.add_argument('--labels', type=str, default=None,
                        help="labels file for prediction")
    parser.add_argument('--export-onnx-graphs', action='store_true', default=False,
                        help='export ONNX graphs to current directory')
    parser.add_argument('--input', type=str, required = True,
                        help="input image for prediction")
    parser.add_argument('--provider', type=str, default="openvino",
                        help="Execution Provider")
    parser.add_argument('--backend_device', type=str, default="CPU",
                        help="Backend device for prediction") 
    parser.add_argument('--precision', type=str, default="FP32",
                        help="precision for prediction(Default FP32)")
    # TODO Add arguments for the options: e.g. pytorch only, label file, export onnx graphs, input, provider, backend, precision
    args = parser.parse_args()

    # 2. Download and load the model
    # TODO Load model
    model = models.resnet50(pretrained=True)
    if not args.pytorch_only:
        provider_configs = ProviderConfigs(provider="openvino", backend=args.backend_device, precision=args.precision)
        model = ORTModule(model, provider_configs=provider_configs)
    # Convert model for evaluation
    model.eval()

    # 3. Download ImageNet labels
    categories = download_labels(args.labels)
    
    # 4. Read input image and preprocess
    batch = preprocess_image(args.input)

    # 5. Predict
    predict(model,batch,categories)

if __name__ == '__main__':
    main()
