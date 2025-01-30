echo "Build Start"

# Ensure Python and pip are available
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "Error: Python is not installed!"
    exit 1
fi

# Upgrade pip
$PYTHON -m pip install --upgrade pip

# Check if requirements.txt exists before installing
if [ -f "requirements.txt" ]; then
    $PYTHON -m pip install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

# Collect static files
$PYTHON manage.py collectstatic --noinput --clear --verbosity 3

echo "Build End"
