#!/bin/bash

# Ensure a clean build environment
rm -rf staticfiles_build  # Remove old build if exists
mkdir -p staticfiles_build  # Ensure directory exists

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear --verbosity 3

# Move collected static files to the correct directory
mv staticfiles staticfiles_build
