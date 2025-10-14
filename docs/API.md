# API Documentation

## Recipe Hub API Endpoints

### Base URL
```
http://localhost:8000/api/v1
```

## Authentication

### POST /auth/register
Register a new user account.

**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure_password"
}
```

**Response:**
```json
{
  "user_id": 123,
  "username": "john_doe",
  "token": "jwt_token_here"
}
```

### POST /auth/login
Authenticate user and receive access token.

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "secure_password"
}
```

## Recipes

### GET /recipes
Retrieve all recipes with optional filtering.

**Query Parameters:**
- `cuisine` (optional): Filter by cuisine type
- `difficulty` (optional): Filter by difficulty level
- `tags` (optional): Filter by tags (comma-separated)
- `max_time` (optional): Maximum total cooking time
- `page` (optional): Page number for pagination
- `limit` (optional): Number of results per page

**Example Request:**
```
GET /recipes?cuisine=Italian&difficulty=Easy&page=1&limit=10
```

**Response:**
```json
{
  "recipes": [
    {
      "id": 1,
      "title": "Spaghetti Carbonara",
      "description": "Traditional Italian pasta dish",
      "cuisine": "Italian",
      "difficulty": "Medium",
      "prep_time": 15,
      "cook_time": 20,
      "servings": 4,
      "rating": 4.8,
      "created_by": "chef_mario",
      "created_at": "2024-10-01T10:30:00Z"
    }
  ],
  "total": 45,
  "page": 1,
  "limit": 10
}
```

### GET /recipes/{id}
Get detailed information about a specific recipe.

**Response:**
```json
{
  "id": 1,
  "title": "Spaghetti Carbonara",
  "description": "Traditional Italian pasta dish",
  "cuisine": "Italian",
  "difficulty": "Medium",
  "prep_time": 15,
  "cook_time": 20,
  "servings": 4,
  "ingredients": [
    {
      "item": "Spaghetti",
      "amount": "400g",
      "notes": "Use high-quality pasta"
    }
  ],
  "instructions": [
    "Bring a large pot of salted water to boil",
    "Cook pancetta until crispy..."
  ],
  "tags": ["Italian", "Pasta", "Traditional"],
  "nutrition": {
    "calories": 520,
    "protein": "22g",
    "carbs": "65g",
    "fat": "18g"
  },
  "rating": 4.8,
  "reviews": 234,
  "created_by": "chef_mario",
  "created_at": "2024-10-01T10:30:00Z"
}
```

### POST /recipes
Create a new recipe (requires authentication).

**Headers:**
```
Authorization: Bearer jwt_token_here
Content-Type: application/json
```

**Request Body:**
```json
{
  "title": "My Amazing Recipe",
  "description": "A delicious dish",
  "cuisine": "International",
  "difficulty": "Easy",
  "prep_time": 10,
  "cook_time": 20,
  "servings": 4,
  "ingredients": [
    {
      "item": "Ingredient 1",
      "amount": "2 cups",
      "notes": "Optional notes"
    }
  ],
  "instructions": [
    "Step 1: Do this",
    "Step 2: Do that"
  ],
  "tags": ["tag1", "tag2"]
}
```

### PUT /recipes/{id}
Update an existing recipe (requires authentication and ownership).

### DELETE /recipes/{id}
Delete a recipe (requires authentication and ownership).

## Search

### GET /search
Search recipes by various criteria.

**Query Parameters:**
- `q` (required): Search query
- `in` (optional): Search in specific fields (title, ingredients, instructions)
- `cuisine` (optional): Filter by cuisine
- `max_time` (optional): Maximum total time

**Example:**
```
GET /search?q=chicken&in=ingredients&cuisine=Indian&max_time=60
```

## Ratings

### POST /recipes/{id}/ratings
Rate a recipe (requires authentication).

**Request Body:**
```json
{
  "rating": 5,
  "comment": "Absolutely delicious!"
}
```

### GET /recipes/{id}/ratings
Get all ratings for a recipe.

## User Profile

### GET /users/profile
Get current user's profile (requires authentication).

### PUT /users/profile
Update user profile (requires authentication).

### GET /users/{id}/recipes
Get recipes created by a specific user.

## Favorites

### POST /users/favorites/{recipe_id}
Add recipe to favorites (requires authentication).

### DELETE /users/favorites/{recipe_id}
Remove recipe from favorites (requires authentication).

### GET /users/favorites
Get user's favorite recipes (requires authentication).

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request",
  "details": "Specific error details"
}
```

### 401 Unauthorized
```json
{
  "error": "Authentication required"
}
```

### 404 Not Found
```json
{
  "error": "Recipe not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

## Rate Limiting

- 100 requests per minute for authenticated users
- 30 requests per minute for anonymous users

## Data Validation

All recipe fields are validated:
- `title`: 3-100 characters
- `prep_time`, `cook_time`: Positive integers
- `servings`: 1-20 people
- `difficulty`: Must be "Easy", "Medium", or "Hard"
- `ingredients`: At least one ingredient required
- `instructions`: At least one step required