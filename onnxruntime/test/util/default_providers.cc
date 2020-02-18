// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

#include "default_providers.h"
#include "providers.h"
#include "core/session/onnxruntime_cxx_api.h"
#include "core/providers/providers.h"

namespace onnxruntime {

std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_CPU(int use_arena);
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_CUDA(OrtDevice::DeviceId device_id);
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_Dnnl(int use_arena);
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_NGraph(const char* ng_backend_type);
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_Nuphar(bool, const char*);
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_Nnapi();
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_Tensorrt(int device_id);
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_OpenVINO(const char* device_id);
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_Intel(const char* device_id);
std::shared_ptr<IExecutionProviderFactory> CreateExecutionProviderFactory_ACL(int use_arena);

namespace test {

std::unique_ptr<IExecutionProvider> DefaultCpuExecutionProvider(bool enable_arena) {
  return CreateExecutionProviderFactory_CPU(enable_arena)->CreateProvider();
}

std::unique_ptr<IExecutionProvider> DefaultTensorrtExecutionProvider() {
#ifdef USE_TENSORRT
  return CreateExecutionProviderFactory_Tensorrt(0)->CreateProvider();
#else
  return nullptr;
#endif
}

std::unique_ptr<IExecutionProvider> DefaultOpenVINOExecutionProvider() {
#ifdef USE_OPENVINO
  return CreateExecutionProviderFactory_OpenVINO("CPU")->CreateProvider();
#else
  return nullptr;
#endif
}

std::unique_ptr<IExecutionProvider> DefaultIntelExecutionProvider() {
#ifdef USE_INTEL
   return CreateExecutionProviderFactory_Intel("CPU")->CreateProvider();
#else
   return nullptr;
#endif
}


std::unique_ptr<IExecutionProvider> DefaultCudaExecutionProvider() {
#ifdef USE_CUDA
  return CreateExecutionProviderFactory_CUDA(0)->CreateProvider();
#else
  return nullptr;
#endif
}

std::unique_ptr<IExecutionProvider> DefaultDnnlExecutionProvider(bool enable_arena) {
#ifdef USE_DNNL
  return CreateExecutionProviderFactory_Dnnl(enable_arena ? 1 : 0)->CreateProvider();
#else
  ORT_UNUSED_PARAMETER(enable_arena);
  return nullptr;
#endif
}

std::unique_ptr<IExecutionProvider> DefaultNGraphExecutionProvider() {
#ifdef USE_NGRAPH
  return CreateExecutionProviderFactory_NGraph("CPU")->CreateProvider();
#else
  return nullptr;
#endif
}

std::unique_ptr<IExecutionProvider> DefaultNupharExecutionProvider(bool allow_unaligned_buffers) {
#ifdef USE_NUPHAR
  return CreateExecutionProviderFactory_Nuphar(allow_unaligned_buffers, "")->CreateProvider();
#else
  ORT_UNUSED_PARAMETER(allow_unaligned_buffers);
  return nullptr;
#endif
}

std::unique_ptr<IExecutionProvider> DefaultNnapiExecutionProvider() {
#ifdef USE_NNAPI
  return CreateExecutionProviderFactory_Nnapi()->CreateProvider();
#else
  return nullptr;
#endif
}

std::unique_ptr<IExecutionProvider> DefaultAclExecutionProvider(bool enable_arena) {
#ifdef USE_ACL
  return CreateExecutionProviderFactory_ACL(enable_arena)->CreateProvider();
#else
  ORT_UNUSED_PARAMETER(enable_arena);
  return nullptr;
#endif
}

}  // namespace test
}  // namespace onnxruntime
