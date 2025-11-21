# API Documentation

**Base URL**
- Base URL: https://sentiment-api.orangesand-df480b09.southeastasia.azurecontainerapps.io
- All endpoints are prefixed with /api
- Postman config ada di ```./docs```
- Note: cold start bisa membuthkan waktu 30 detik, mohon bersabar menunggu respon :)

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

**Example Response**
```
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MzcyMjk4MiwianRpIjoiMTI4OTY2NzUtOTZjZC00OTU2LThhMWMtZGNiODc0MzdmYTA5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkNDcxNTViLWU5YzktNDIxMi1hYTdjLTc4ODFhN2ZkMTI4NCIsIm5iZiI6MTc2MzcyMjk4MiwiY3NyZiI6IjM1Zjg5ODdlLTJkMTUtNDU4MC1iZTU0LTI1NzI4MzI3Yjk4MCIsImV4cCI6MTc2MzcyNjU4MiwidG9rZW5fdmVyc2lvbiI6InYxIn0.1jGvPsPTxWdDrHvejoU-fg25MupsXbN4wWRZHdL_oYQ",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MzcyMjk4MiwianRpIjoiNGNiM2M5NTMtMjgxZi00YWU2LThjMTgtMjM1OTlhYmJmZjA2IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJhZDQ3MTU1Yi1lOWM5LTQyMTItYWE3Yy03ODgxYTdmZDEyODQiLCJuYmYiOjE3NjM3MjI5ODIsImNzcmYiOiJlYTgwYjJiZC1kMzhkLTRjNTktODEwNy04ODlkNWYzYWYzYWEiLCJleHAiOjE3NjM4MDkzODIsInRva2VuX3ZlcnNpb24iOiJ2MSJ9.O2Pr9Hu9XrM2lOHL4J2mM7oSVB4dWNB00Dfu-eITG_w",
    "user": {
        "created_at": "Fri, 21 Nov 2025 11:02:43 GMT",
        "email": "tes6@gmail.com",
        "id": "ad47155b-e9c9-4212-aa7c-7881a7fd1284",
        "is_active": true,
        "name": "tes6"
    }
}
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

**Example Response**
```
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MzcyMzAzMSwianRpIjoiZDY4ZDU0NjAtYmM0OS00OGVjLWEyODYtYWQzYWNmYmY5MDlmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhMjlkY2NjLTgyNDAtNDAwOS1iZGNjLWY3ODk4ZDJlODZkNiIsIm5iZiI6MTc2MzcyMzAzMSwiY3NyZiI6IjMxYWU2MWIwLTJkNmUtNGM5Mi1iNzc2LWQxMGVkN2I1NjY0OCIsImV4cCI6MTc2MzcyNjYzMSwidG9rZW5fdmVyc2lvbiI6ImExYThiNDkxLWMifQ.ftDxL_DbbQjZGgv3MjVe2_qy0XSEKrIdM-Z8D_LTffk",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MzcyMzAzMSwianRpIjoiMzExMGNiMDAtYTViOS00ZGFjLTgyMDktZmY0ZjUwNmQ2ODVkIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiI4YTI5ZGNjYy04MjQwLTQwMDktYmRjYy1mNzg5OGQyZTg2ZDYiLCJuYmYiOjE3NjM3MjMwMzEsImNzcmYiOiJkMGQ4MWIwMC02Mjc1LTQ5ZDAtYTlmZC1iYzU3YTExZDQwNWUiLCJleHAiOjE3NjM4MDk0MzEsInRva2VuX3ZlcnNpb24iOiJhMWE4YjQ5MS1jIn0.JMXcpgFxbCgzFxiioLNy57Bcvz-aQE2-nsTPIWZnvcI",
    "user": {
        "created_at": "Fri, 21 Nov 2025 04:26:36 GMT",
        "email": "tes5@gmail.com",
        "id": "8a29dccc-8240-4009-bdcc-f7898d2e86d6",
        "is_active": true,
        "name": "tes5"
    }
}
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

**Example Response**
```
{
    "message": "Password berhasil diganti"
}

```

#### GET /me
current user

**Example response**
```
{
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

**Example Response**
```
{
    "analyzed_at": "Fri, 21 Nov 2025 11:02:44 GMT",
    "category": "Others",
    "category_score": 0.8,
    "content": "Hi guys how r yall",
    "created_at": "Fri, 21 Nov 2025 11:02:43 GMT",
    "id": "2990a8b4-1f8f-4144-8273-ec4c1fe2bb89",
    "sentiment": "NEUTRAL",
    "sentiment_score": 0.8
}
```

## GraphQL Endpoints
### POST /graphql
- Execute GraphQL queries and mutations.
- Base URL: https://sentiment-api.orangesand-df480b09.southeastasia.azurecontainerapps.io/api/graphql

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

#### Example response
```
{
    "data": {
        "userAnalysisHistory": [
            {
                "id": "040c899c-0837-4c2a-aaed-755ae9a4d974",
                "post": {
                    "content": "halo semuanya apa kabar",
                    "id": "8f35d0fb-fd8c-46f3-99e6-b75d59fe3dec"
                },
                "sentiment": "POSITIVE",
                "sentimentScore": null
            },
            {
                "id": "8b03931a-4727-43cb-ba3b-707106ec6fd6",
                "post": {
                    "content": "halo semuanya apa kabar",
                    "id": "0d528b7e-b5ba-41ed-aa72-c0de46a2845f"
                },
                "sentiment": "POSITIVE",
                "sentimentScore": null
            },
            {
                "id": "45ecb304-efee-4198-bb54-845428fc2aae",
                "post": {
                    "content": "man fuck off",
                    "id": "c58fe07c-10e1-436c-b7c2-80daf8c6d048"
                },
                "sentiment": "NEGATIVE",
                "sentimentScore": null
            }
        ]
    }
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

