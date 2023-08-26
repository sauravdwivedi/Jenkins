#!/bin/bash
python3 -m venv venv
source venv/bin/activate
export PYTHONPATH=`pwd`:`cd backend && pwd`:`cd backend/controllers && pwd`
cd backend
pip3 install -r requirements.txt
export FLASK_APP=app

echo "Waiting for database to be ready"
echo "Sleeping for 30 seconds"
sleep 30

echo "Apply database init"
flask db init 
echo "Sleeping for 30 seconds"
sleep 30

echo "Apply database migrations"
flask db migrate -m "Initial migration"
echo "Sleeping for 30 seconds"
sleep 30

echo "Apply database upgrade"
flask db upgrade
echo "Sleeping for 30 seconds"
sleep 30

echo "Start flask application"
screen python3 app.py > log.txt 2>&1 &