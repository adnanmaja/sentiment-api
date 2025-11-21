
This document describes the GraphQL schema, resolvers, and HTTP route for the GraphQL endpoint found in this repository.

Files referenced
- `src/api/graphql/schema.graphql` — GraphQL type definitions and `Query`.
- `src/api/graphql/resolvers.py` — Resolver functions used by the schema.
- `src/api/graphql/route.py` — Flask route that exposes the GraphQL endpoint and Playground.

Overview

- The schema exposes a single query: `userAnalysisHistory`.
- The Flask Blueprint registers `/graphql` for both GET (Playground) and POST (query execution).

Schema: `userAnalysisHistory`

- Signature:
  - `userAnalysisHistory(userId: ID!, sentiment: String, category: String, minSentimentScore: Float, maxSentimentScore: Float, limit: Int = 10, offset: Int = 0): [Analysis!]!`
- Purpose: fetch a user's analysis records with optional filters and pagination.
- Filters:
  - `sentiment` — string (e.g. "positive", "negative", "neutral") to filter `Analysis.sentiment`.
  - `category` — string category to filter `Analysis.category`.
  - `minSentimentScore` / `maxSentimentScore` — numeric bounds on `Analysis.sentimentScore`.
  - `limit` / `offset` — pagination controls (defaults: `limit=10`, `offset=0`).

Types (high level)
- `User` — `id`, `name`, `email`, `createdAt` (ISO datetime string).
- `Post` — `id`, `content`, `createdAt`, `user` (nested `User`).
- `Analysis` — `id`, `sentiment`, `sentimentScore`, `category`, `categoryScore`, `analyzedAt`, `post` (nested `Post`).

Resolvers (what they do)

- `resolve_user_analysis_history` (in `resolvers.py`)
  - Builds a SQLAlchemy query joining `Analysis`, `Post`, and `User`.
  - Applies optional filters (`sentiment`, `category`, `min_sentiment_score`, `max_sentiment_score`).
  - Orders by `analyzed_at` descending and applies `offset` / `limit`.
  - Returns a list of `Analysis` objects.

- `resolve_datetime_field`
  - Generic helper to convert datetime attributes to ISO 8601 strings for fields like `createdAt` and `analyzedAt`.

- `resolve_post_analysis` and `resolve_post_user`
  - Return nested related objects: `analysis.post` and `post.user` respectively.

HTTP routes and usage

- GET `/graphql` — serves an HTML GraphQL Playground that can be used for interactive queries.
- POST `/graphql` — executes GraphQL requests. Expects a JSON body with at least `query` (and optional `variables`).

Example GraphQL query

Query (GraphQL):

```graphql
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

Variables (example JSON):

```json
{
  "userId": "0004ba55-877e-44f5-847f-77ae6b05c8a1",
  "limit": 5,
  "offset": 0
}
```

Example cURL (Linux/macOS) POST request

```bash
curl -X POST http://localhost:5000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"query { userAnalysisHistory(userId:\"123\") { id sentiment sentimentScore } }"}'
```

Example PowerShell POST request (Windows PowerShell 5.1)

```powershell
$body = @{ query = 'query { userAnalysisHistory(userId:"123") { id sentiment sentimentScore } }' }
Invoke-RestMethod -Uri http://localhost:5000/graphql -Method Post -ContentType 'application/json' -Body ($body | ConvertTo-Json)
```

Notes and tips

- Ensure the Flask app is running and the database is initialized before calling the endpoint.
- The resolvers rely on SQLAlchemy models named `Analysis`, `Post`, and `User` (see `src/models/model.py`).
- Date/time fields are returned as ISO strings by `resolve_datetime_field`.
- If you want to add more queries or mutations, add types to `schema.graphql`, write resolvers in `resolvers.py`, and register them in `route.py`.

Want changes?

- I did not modify any existing source files. If you want this doc moved, split into multiple files, or expanded (examples, response shapes, auth notes), tell me and I can update it.

-- End of file
