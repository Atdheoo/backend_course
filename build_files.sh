#!/bin/bash

# Ensure a clean build environment
rm -rf staticfiles_build
mkdir -p staticfiles_build

# Explicitly use Python 3.9
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear --verbosity 3

# Move collected static files to the correct directory
mv staticfiles staticfiles_build
