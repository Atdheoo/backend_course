echo "Build Start"
pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "Build End"