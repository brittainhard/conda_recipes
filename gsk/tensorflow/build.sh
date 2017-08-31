#!/bin/bash

set -ex

mkdir -p ./bazel_output_base
export BAZEL_OPTS="--batch --output_base=./bazel_output_base"

# Compile tensorflow from source
export PYTHON_BIN_PATH=${PYTHON}
export PYTHON_LIB_PATH=${SP_DIR}
export CC_OPT_FLAGS="-march=nocona"
export TF_NEED_GCP=0
export TF_NEED_HDFS=0
export TF_NEED_OPENCL=0
export TF_NEED_CUDA=0
./configure

# build using bazel
bazel ${BAZEL_OPTS} build --jobs 2 --config=opt //tensorflow/tools/pip_package:build_pip_package

# build a whl file
mkdir -p $SRC_DIR/tensorflow_pkg
bazel-bin/tensorflow/tools/pip_package/build_pip_package $SRC_DIR/tensorflow_pkg

# install using pip from the whl file
pip install --no-deps $SRC_DIR/tensorflow_pkg/*.whl
