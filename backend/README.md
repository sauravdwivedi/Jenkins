## Run flask backend
```bash
python3 -m venv venv
source venv/bin/activate
export PYTHONPATH=`pwd`:`cd backend && pwd`:`cd backend/controllers && pwd`
cd backend
pip3 install -r requirements.txt
export FLASK_APP=app
flask db init 
flask db migrate -m "Initial migration"
flask db upgrade
python3 app.py
```

## Run unit tests against endpoints 
```bash
python3 test/test_default_controller.py
```

## API documentation
- http://127.0.0.1:5000/api/v1/ui/