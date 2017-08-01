#!/bin/bash
sudo yum install patch -y
$PYTHON setup.py install --single-version-externally-managed --record record.txt
