#!/bin/bash
set -x
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install boto3