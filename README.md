# Boundless Moody Analytics
This project is a test project that visualizes a moody dataset file consisting of grades and other factors for students.
The application is deployed on Amazon EC2.

## Link for the application: http://ec2-54-211-1-83.compute-1.amazonaws.com:8080/

## To deploy the application: 
Download the zip. 

This contains two folders ## moody-backend and ## ui

## From CMD / Terminal 

cd into the ui folder and use ## npm start

## from a second CMD / Terminal 

cd into the moody-backend folder and use ## python3 app.py


## For the application webpage

The table is defined as grades. 
So while inserting a query use the format 

 ### "Select * from grades where condition;"

The following columns with unique values can be used for defining the conditions

Example Query: Select * from grades where DOZES_OFF ="always";

![image](https://user-images.githubusercontent.com/91026979/163110191-cf300ddb-aa58-4a75-8b15-31987b1cc553.png)

###Application:

https://user-images.githubusercontent.com/91026979/163437125-2e577076-3a76-4aa0-8ec8-813d6094ef9f.mp4


