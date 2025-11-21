# Rough api schmas
semua endpoint diawali dengan prefix /api

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

**POST /change-password**
current_password: str
new_password: str

{
    "current_password":"",
    "new_password": ""
}

curl -X POST -H "Content-Type: application/json" -d "{\"current_password\":\string\", \"new_password\": \"striing\"}" http://127.0.0.1:5000/api/login

**POST /post**
content: str

{
    "content":"halo semuanya apa kabar"
}

curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MzY2MTc4MCwianRpIjoiZmY2NjY1MTAtNGRjNC00OTliLTg4NDgtNGFhNTNhMzcyOWYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjAwMDRiYTU1LTg3N2UtNDRmNS04NDdmLTc3YWU2YjA1YzhhMSIsIm5iZiI6MTc2MzY2MTc4MCwiY3NyZiI6ImRiMzVlOTAzLTczODYtNDU1Ni1hMDkzLWU4NDJhZWJkMWNiZCIsImV4cCI6MTc2MzY2NTM4MCwidG9rZW5fdmVyc2lvbiI6InYxIn0.i7bvxsgmB9VAXAWoQ3lC7xz0NfA_xWf3q9YkObCyDLM" -d "{\"content\":\"halo semuanya apa kabar\"}" http://127.0.0.1:5000/api/post

**POST /graphql**

curl -X POST -H "Content-Type: application/json" --data @query.json http://localhost:5000/api/graphql