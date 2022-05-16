OpenVINO™ integration with OnnxRuntime
======================================

-  `OpenVINO™ integration with OnnxRuntime <https://github.com/intel/onnxruntime/>`_. is a product designed for OnnxRuntime developers who want to get started with OnnxRuntime in their inferencing applications. This product delivers  `OpenVINO™ <https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html>`_. inline optimizations which enhance inferencing performance with minimal code modifications. **OpenVINO™ integration with OnnxRuntime** accelerates inference across many  `AI models <https://github.com/onnx/models>`_. on a variety of Intel silicon such as:
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

For installation instructions on Windows please refer to  `OpenVINO™ integration with OnnxRuntime** for Windows <https://github.com/intel/onnxruntime/releases/tag/v4.0>`_. 

For more details on build and installation please refer to `Build.md <https://onnxruntime.ai/docs/build/eps.html#openvino>`_.

Usage
^^^^^

By default, Intel CPU is used to run inference. However, you can change the default option to either Intel integrated GPU or Intel VPU for AI inferencing. Invoke the following function to change the hardware on which inferencing is done.

For more API calls and environment variables, see  `Usage.md <https://onnxruntime.ai/docs/execution-providers/OpenVINO-ExecutionProvider.html#configuration-options>`_.

Examples
^^^^^^^^

To see what you can do with **OpenVINO™ integration with OnnxRuntime**, explore the demos located in the  `Examples <https://github.com/microsoft/onnxruntime-inference-examples>`_.

Docker Support
^^^^^^^^^^^^^^

The latest OpenVINO EP docker image can be downloaded from dockerhub. 
For more details see  `Docker ReadMe <https://hub.docker.com/r/openvino/onnxruntime_ep_ubuntu18>`_.


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

Please submit your questions, feature requests and bug reports via   `GitHub Issues <https://github.com/intel/onnxruntime/issues>`_.

How to Contribute
^^^^^^^^^^^^^^^^^^

We welcome community contributions to **OpenVINO™ integration with OnnxRuntime**. If you have an idea for improvement:

* Share your proposal via  `GitHub Issues <https://github.com/intel/onnxruntime/issues>`_.
* Submit a  `Pull Request <https://github.com/intel/onnxruntime/pulls>`_.



