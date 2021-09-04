# Pizza Databse, Django
CRUD APIs for pizza db, in django

## Installation
These were my python configs at the time of making this project:
```
python version: 3.8.10
pip version: 20.0.2
```
Clone this repo and run the following commands on your terminal:
```
$ pip install -r requirements.txt
$ python3 manage.py runserver
```
If the server does not start, try the following commands:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

If the server still does not start, google your error :)

### Login Credentials for SuperUser:
After your server starts, visit ```localhost:8000/admin``` and use the following credentials to checkout the database
```
username: admin
password: internship@2021
```


## About the Database:
The 'Pizza' db has the following fields:
1. ```title```  : string; stores the title of the pizza
2. ```type```   : string; stores the type of the pizza; "Regular" or "Square"
3. ```size```   : string; stores the size of the pizza; "Small" or "Medium" or "Large"
4. `toppings`   : string; stores the toppings on the pizza; stored in a list of strings
5. ```slug```   : string; auto-generated; stores a unique name for each pizza; used to search a pizza in the db

## About the APIs:
There are in total 7 apis in this project.

1. GET | (all)<br />
   ```http://127.0.0.1:8000/pizzas```<br />
Expects: Nothing<br />
Response: Lists all the pizzas in the database<br />

2. GET | (individual)<br />
```http://127.0.0.1:8000/pizza/<slug>```<br />
Expects: The slug of the pizza you want to see instead of the "< slug >" part above mentioned api.<br />
(Eg.: ```http://127.0.0.1:8000/pizza/paneer-pizza-square```)<br />
Response: Displays the details of the individual Pizza

3. GET | (filtered by size)<br />
```http://127.0.0.1:8000/all_size/<size>```<br />
Expects: The size of the pizza<br />
{Currently, only "Small", "Medium", "Large" are supported, entering a size any other than this will return an error 400}<br />
Response: Returns all the pizzas with the requested size

4. GET | (filtered by type)<br />
```http://127.0.0.1:8000/all_type/<type>```<br />
Expects: The 'type' of the pizza<br />
{Currently, only "Regular" and "Small" types are supported, sending any other type other than these will return a 400 error}<br />
Response: Returns all pizzas with the requested type

5. PUT | (Edit/Update)<br />
```http://12.0.0.1:8000/update/<slug>```<br />
Expects: The slug of the pizza you want to update should replace the "< slug >" in the above mentioned api. The body should consist of the following fields:
```
title       (str)
type        (str)
size        (str)
toppings    (str)
```
Response: Returns the updated value of the Pizza

6. DELETE | (Delete a pizza)<br />
```http://127.0.0.1:8000/delete/<slug>```<br />
Expects: The slug of the pizza you want to delete should replace the "< slug >" in the above mentioned api.<br />
Response: "Delete Succesfull" if the pizza is deleted, "Delete Failed" if the pizzas was not found in the database.

7. POST | (Create)<br />
```http://127.0.0.1:8000/createPizza```<br />
Expects: The following fields in the body of the api request:
```
title       (str)
type        (str)
size        (str)
toppings    (str)
```
Response: Returns the details of the created pizza, if the creation was succesfull. 


<b>You can test the above mentioned APIs in Postman or anywhere you like! :) </b>

## Made By: 

Kushagra Wadhwa<br />
Delhi Technological University (DTU)<br />
( wadhwakushagra01@gmail.com )<br />

```print("Happy Coding!)```

