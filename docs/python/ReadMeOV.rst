OpenVINO™ integration with OnnxRuntime
======================================

-  `OpenVINO™ integration with OnnxRuntime <https://github.com/intel/onnxruntime/>`_.  is a product designed for OnnxRuntime* developers who want to get started with `OnnxRuntime (https://l) in their inferencing applications. This product delivers [OpenVINO™](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html) inline optimizations which enhance inferencing performance with minimal code modifications. **OpenVINO™ integration with OnnxRuntime** accelerates inference across many [AI models](https://github.com/onnx/models) on a variety of Intel<sup>®</sup> silicon such as:
- Intel CPUs
- Intel integrated GPUs
- Intel Movidius™ Vision Processing Units - referred to as VPU
- Intel Vision Accelerator Design with 8 Intel Movidius™ MyriadX VPUs - referred to as VAD-M or HDDL

Installation
------------

Requirements
^^^^^^^^^^^^

- Ubuntu 18.04, macOS 11.2.3 or Windows 10 - 64 bit
- Python* 3.7, 3.8 or 3.9

Windows release supports only Python3.9 

This **OpenVINO™ integration with OnnxRuntime** package comes with pre-built libraries of OpenVINO™ version 2022.1.0 meaning you do not have to install OpenVINO™ separately.
This package supports:
- Intel CPUs
- Intel integrated GPUs
- Intel Movidius™ Vision Processing Units (VPUs)
Please Note for VADM Please use Docker installation / Build from Source for Linux. 

        pip3 install openvino-onnxruntime==1.11.0

For installation instructions on Windows please refer to [**OpenVINO™ integration with OnnxRuntime** for Windows ](https://github.com/intel/onnxruntime/releases/tag/v4.0)

For more details on build and installation please refer to [BUILD.md](https://onnxruntime.ai/docs/build/eps.html#openvino)

Usage
^^^^^

By default, Intel CPU is used to run inference. However, you can change the default option to either Intel integrated GPU or Intel VPU for AI inferencing. Invoke the following function to change the hardware on which inferencing is done.

For more API calls and environment variables, see [USAGE.md](https://onnxruntime.ai/docs/execution-providers/OpenVINO-ExecutionProvider.html#configuration-options).

Examples
^^^^^^^^

To see what you can do with **OpenVINO™ integration with OnnxRuntime**, explore the demos located in the [examples](https://github.com/microsoft/onnxruntime-inference-examples) repository.

Docker Support
^^^^^^^^^^^^^^

The latest OpenVINO EP docker image can be downloaded from dockerhub. 
For more details see [docker readme](https://hub.docker.com/r/openvino/onnxruntime_ep_ubuntu18).

Prebuilt Images
^^^^^^^^^^^^^^^^

- Please find prebuilt images for CPU and GPU on https://github.com/intel/onnxruntime/releases/tag/v4.0

License
^^^^^^^^

**OpenVINO™ integration with OnnxRuntime** is licensed under [MIT](https://github.com/microsoft/onnxruntime/blob/master/LICENSE).
By contributing to the project, you agree to the license and copyright terms therein
and release your contribution under these terms.  

Support
^^^^^^^^

Please submit your questions, feature requests and bug reports via [**GitHub issues**](https://github.com/intel/onnxruntime/issues).

How to Contribute
^^^^^^^^^^^^^^^^^^

We welcome community contributions to **OpenVINO™ integration with OnnxRuntime**. If you have an idea for improvement:

* Share your proposal via [GitHub issues](https://github.com/intel/onnxruntime/issues).
* Submit a [pull request](https://github.com/intel/onnxruntime/pulls).

We will review your contribution as soon as possible. If any additional fixes or modifications are necessary, we will guide you and provide feedback. Before you make your contribution, make sure you can build **OpenVINO™ integration with OnnxRuntime** and run all the examples with your fix/patch. If you want to introduce a large feature, create test cases for your feature. Upon the verification of your pull request, we will merge it to the repository provided that the pull request has met the above mentioned requirements and proved acceptable.

---
\* Other names and brands may be claimed as the property of others.
