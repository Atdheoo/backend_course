echo "Build Start"
python3 -m pip install requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "Build End"