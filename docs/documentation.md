# API Documentation

**Base URL**
All endpoints are prefixed with /api

**Authentication**
- Most endpoints require JWT Bearer token authentication
- Token should be included in the ```Authorization``` header: ```Bearer <your_token>```

## REST Endpoints
### Authetication
#### POST /register
Register a new user

**Request Body**
```
    {
    "name": "string",
    "email": "string",
    "password": "string"
    }
```

**Example cURL**
```
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"tes4\", \"email\":\"tes4@gmail.com\", \"password\": \"string\"}" http://127.0.0.1:5000/api/register
```

#### POST /login
Login and receive authentication token

**Request Body**
```
    {
    "email": "string",
    "password": "string"
    }
```

**Example cURL**
```
curl -X POST -H "Content-Type: application/json" -d "{\"email\":\"tes4@gmail.com\", \"password\": \"string\"}" http://127.0.0.1:5000/api/login
```

#### POST /change-password
Change user password (requires authentication).

**Request Body**
```
    {
    "current_password": "string",
    "new_password": "string"
    }
```

**Example cURL**
```
curl -X POST -H "Content-Type: application/json" \
-H "Authorization: Bearer <your_token>" \
-d "{\"current_password\":\"string\", \"new_password\": \"striing\"}" \
http://127.0.0.1:5000/api/change-password

```

### Posts
#### POST /posts
Create a post (upload the content, require token)

**Request Body**
```
    {
    "content": "string"
    }

```

**Example cURL**
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MzY2MTc4MCwianRpIjoiZmY2NjY1MTAtNGRjNC00OTliLTg4NDgtNGFhNTNhMzcyOWYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjAwMDRiYTU1LTg3N2UtNDRmNS04NDdmLTc3YWU2YjA1YzhhMSIsIm5iZiI6MTc2MzY2MTc4MCwiY3NyZiI6ImRiMzVlOTAzLTczODYtNDU1Ni1hMDkzLWU4NDJhZWJkMWNiZCIsImV4cCI6MTc2MzY2NTM4MCwidG9rZW5fdmVyc2lvbiI6InYxIn0.i7bvxsgmB9VAXAWoQ3lC7xz0NfA_xWf3q9YkObCyDLM" -d "{\"content\":\"halo semuanya apa kabar\"}" http://127.0.0.1:5000/api/post
```

## GraphQL Endpoints