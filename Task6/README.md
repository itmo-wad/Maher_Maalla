# Task 6
## Basic part
Create docker-compose.yml and Dockerfile to run your application in Docker
Move your sources to src directory. Don’t forget to create requirements.txt file
In docker-compose.yml there are gonna be two containers named: mongodb, flask-simple
Setup port forwarding and run docker-compose up. Check that website works on http://localhost:5000
## Optimal part
Add persistent volume for MongoDB
Mount upload directory to upload directory inside flask-simple container
## Challenging part
Add Nginx which will proxy requests to flask application
Add Redis cache for uploaded images
