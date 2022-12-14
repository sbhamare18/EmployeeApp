# EmployeeApp
### Employee App is created in this project in which all the CRUD operations can be performed
All the profile pictures will be stored in media folder

## Columns in database:
<b>emp_id: int</b>         (This is the mandatory field of type Int, primary key, auto generated),</br>
<b>first_name: str </b>  (This is the mandatory field of type char),</br>
<b>last_name: str </b>   (This is the mandatory field of type char),</br>
<b>emp_salary: float </b>(This is the mandatory field of type float),</br>
<b>emp_profile_picture: image </b> (This is the mandatory field of type image),</br>
<b>phone_number: str </b>(This is the mandatory field of type char),</br>
<b>address: str  </b>    (This is the mandatory field of type char)</br>
<br>
## Authentication:
Basic auth is required to run these APIs
Please add username and password in header.

## Get method
URL: http://127.0.0.1:8000/employees/,</br>
method: GET</br>
output: All employees present in database

URL: http://127.0.0.1:8000/employees/{id}</br>
method: GET</br>
output: Employee with requested ID present in database</br>

## POST Method
URL: http://127.0.0.1:8000/employees/,</br>
method: POST</br>
output: Add new Employee in database

Request Body:
{
    "first_name": "Steve",
    "last_name": "Rogers",
    "emp_salary": 60000.0,
    "emp_profile_picture": "http://127.0.0.1:8000/profilepic.jpg",
    "phone_number": "12345657541",
    "address": " "
}

## PUT Method
URL: http://127.0.0.1:8000/employees/{id}/,</br>
method: PUT</br>
output: Update existing Employee in database

Request Body:
{
    "emp_id": 7,
    "first_name": "Steve",
    "last_name": "Rogers",
    "emp_salary": 60000.0,
    "emp_profile_picture": "http://127.0.0.1:8000/profilepic.jpg",
    "phone_number": "12345657541",
    "address": " "
}

## DELETE Method
URL: http://127.0.0.1:8000/employees/{id}/,</br>
method: DELETE</br>
output: Delete Employee from database