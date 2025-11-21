# API Documentation

**Base URL**
- All endpoints are prefixed with /api

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
Change user password (requires authentication token).

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

#### GET /me
current user

**Example response**
```
{
    "message": "Here's whatever the fuck you wanted to see:",
    "user": {
        "created_at": "Fri, 21 Nov 2025 04:26:36 GMT",
        "email": "tes5@gmail.com",
        "id": "8a29dccc-8240-4009-bdcc-f7898d2e86d6",
        "is_active": true,
        "name": "tes5"
    }
}
```

### Posts
#### POST /posts
Create a post (requires authentication token)

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
### POST /graphql
- Execute GraphQL queries and mutations.
- Base URL: http://localhost:5000/api/graphql

### Schema Overview
#### Main Query
```userAnalysisHistory``` Fetch a user's analysis records with filtering and pagination
#### Types
- ```User``` User Information
- ```Post``` User posts with content
- ```Analysis``` Sentiment analysis results

### Example query

#### GraphQL Query:
```
query GetUserAnalysis($userId: ID!, $limit: Int, $offset: Int) {
  userAnalysisHistory(userId: $userId, limit: $limit, offset: $offset) {
    id
    sentiment
    sentimentScore
    category
    categoryScore
    analyzedAt
    post {
      id
      content
      createdAt
      user {
        id
        name
        email
        createdAt
      }
    }
  }
}
```

#### Variables
```
{
  "userId": "0004ba55-877e-44f5-847f-77ae6b05c8a1",
  "limit": 5,
  "offset": 0
}
```

## File Structure Reference
- ```src/api/routes``` rest endpoints
- ```src/api/documentation``` swagger ui, gakepake wkw
- ```src/api/graphql``` graphql resolver, schema, and endpoint
- ```src/database``` database connection
- ```src/ml_model``` transformer models inference
- ```src/schemas``` request/response pydantic schemas
- ```src/models``` database model

