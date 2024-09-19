@echo off
title Test
pip install -q flake8 flake8-cognitive-complexity
echo The quality of our server is:
python -m pylint server.py
echo The quality of our client is:
python -m pylint client.py

pip install -q requests flask
START serverStart.bat
echo Wait for the server to start up on the separate CMD 
pause 
curl -d "{\"message\": \"First\"}" -H "Content-Type: application/json" -X post http://127.0.0.1:5000/messages 
curl -d "{\"message\": \"Second\"}" -H "Content-Type: application/json" -X post http://127.0.0.1:5000/messages 
curl -d "{\"message\": \"Third\"}" -H "Content-Type: application/json" -X post http://127.0.0.1:5000/messages 

curl http://127.0.0.1:5000/messages/count
echo Now kill the server, we will turn it on again
pause

START serverStart.bat
echo Wait for the server to start up on the separate CMD 
pause

curl http://127.0.0.1:5000/messages/count
echo In here the count should be 0 since this server has forgotten all the information
echo Time to ping server is:
powershell -Command "Measure-Command {curl http://127.0.0.1:5000/messages/count}"
pause
