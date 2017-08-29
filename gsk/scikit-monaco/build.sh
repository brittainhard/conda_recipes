#!/bin/bash
${PYTHON} setup.py install  --single-version-externally-managed --record=record.txt
pushd skmonaco/tests
${PYTHON} miser_data_generator.py
cp miser_data.pkl $SRC_DIR
popd
${PYTHON} runtests.py
