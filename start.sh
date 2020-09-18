#!/bin/bash

if [ ! -d ./venv ]; then
  echo Creating virtual environment...
  python3 -m venv venv
fi

source ./venv/bin/activate

echo Installing dependencies...
pip install --upgrade pip
pip install -r ./requirements.txt

cd ./stask
python ./cli.py
