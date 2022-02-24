#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "openvino::frontend::onnx" for configuration "Release"
set_property(TARGET openvino::frontend::onnx APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openvino::frontend::onnx PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/runtime/lib/intel64/libov_onnx_frontend.so"
  IMPORTED_SONAME_RELEASE "libov_onnx_frontend.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS openvino::frontend::onnx )
list(APPEND _IMPORT_CHECK_FILES_FOR_openvino::frontend::onnx "${_IMPORT_PREFIX}/runtime/lib/intel64/libov_onnx_frontend.so" )

# Import target "openvino::frontend::paddle" for configuration "Release"
set_property(TARGET openvino::frontend::paddle APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openvino::frontend::paddle PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/runtime/lib/intel64/libov_paddle_frontend.so"
  IMPORTED_SONAME_RELEASE "libov_paddle_frontend.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS openvino::frontend::paddle )
list(APPEND _IMPORT_CHECK_FILES_FOR_openvino::frontend::paddle "${_IMPORT_PREFIX}/runtime/lib/intel64/libov_paddle_frontend.so" )

# Import target "openvino::runtime::c" for configuration "Release"
set_property(TARGET openvino::runtime::c APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openvino::runtime::c PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/runtime/lib/intel64/libinference_engine_c_api.so"
  IMPORTED_SONAME_RELEASE "libinference_engine_c_api.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS openvino::runtime::c )
list(APPEND _IMPORT_CHECK_FILES_FOR_openvino::runtime::c "${_IMPORT_PREFIX}/runtime/lib/intel64/libinference_engine_c_api.so" )

# Import target "openvino::runtime" for configuration "Release"
set_property(TARGET openvino::runtime APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openvino::runtime PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/runtime/lib/intel64/libov_runtime.so"
  IMPORTED_SONAME_RELEASE "libov_runtime.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS openvino::runtime )
list(APPEND _IMPORT_CHECK_FILES_FOR_openvino::runtime "${_IMPORT_PREFIX}/runtime/lib/intel64/libov_runtime.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
