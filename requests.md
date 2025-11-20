**POST /register**
name: str
email: EmailStr
password: str

{
    "name": "",
    "email": "",
    "password": "",
}

curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"tes4\", \"email\":\"tes4@gmail.com\", \"password\": \"string\"}" http://127.0.0.1:5000/api/register

**POST /login**
email: EmailStr
password: str

{
    "email": "",
    "password": ""
}

curl -X POST -H "Content-Type: application/json" -d "{\"email\":\"tes4@gmail.com\", \"password\": \"string\"}" http://127.0.0.1:5000/api/login