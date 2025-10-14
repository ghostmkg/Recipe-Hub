# Recipe Schema Documentation

## Overview
This document defines the data structure and validation rules for recipes in the Recipe Hub.

## Recipe Schema

### Main Recipe Object

```json
{
  "id": "string | number",           // Unique identifier
  "title": "string",                 // Recipe name (required, 3-100 chars)
  "description": "string",           // Brief description (optional, max 500 chars)
  "cuisine": "string",              // Cuisine type (optional)
  "difficulty": "Easy|Medium|Hard", // Difficulty level (required)
  "prep_time": "number",            // Preparation time in minutes (required)
  "cook_time": "number",            // Cooking time in minutes (required)
  "total_time": "number",           // Auto-calculated: prep_time + cook_time
  "servings": "number",             // Number of servings (required, 1-20)
  "ingredients": [],                // Array of ingredient objects (required)
  "instructions": [],               // Array of instruction strings (required)
  "tags": [],                       // Array of tag strings (optional)
  "nutrition": {},                  // Nutrition object (optional)
  "rating": "number",               // Average rating (0-5, auto-calculated)
  "review_count": "number",         // Number of reviews (auto-calculated)
  "image_url": "string",            // Recipe image URL (optional)
  "video_url": "string",            // Recipe video URL (optional)
  "created_by": "string",           // Username of creator (auto-set)
  "created_at": "ISO string",       // Creation timestamp (auto-set)
  "updated_at": "ISO string",       // Last update timestamp (auto-set)
  "is_public": "boolean",           // Visibility flag (default: true)
  "source": "string",               // Original source if adapted (optional)
  "notes": "string"                 // Additional notes (optional)
}
```

### Ingredient Object

```json
{
  "item": "string",                 // Ingredient name (required)
  "amount": "string",               // Quantity with unit (required)
  "notes": "string",                // Preparation notes (optional)
  "category": "string",             // Ingredient category (optional)
  "substitutes": []                 // Array of substitute options (optional)
}
```

### Nutrition Object

```json
{
  "calories": "number",             // Calories per serving
  "protein": "string",              // Protein content (e.g., "25g")
  "carbs": "string",               // Carbohydrate content
  "fat": "string",                 // Fat content
  "fiber": "string",               // Fiber content (optional)
  "sugar": "string",               // Sugar content (optional)
  "sodium": "string",              // Sodium content (optional)
  "cholesterol": "string",         // Cholesterol content (optional)
  "vitamins": {},                   // Vitamin content object (optional)
  "minerals": {}                    // Mineral content object (optional)
}
```

## Validation Rules

### Required Fields
- `title`: Must be 3-100 characters
- `difficulty`: Must be exactly "Easy", "Medium", or "Hard"
- `prep_time`: Positive integer, max 1440 (24 hours)
- `cook_time`: Non-negative integer, max 1440
- `servings`: Integer between 1 and 20
- `ingredients`: Array with at least 1 ingredient
- `instructions`: Array with at least 1 instruction

### Optional Field Constraints
- `description`: Max 500 characters
- `cuisine`: Max 50 characters
- `tags`: Max 10 tags, each max 30 characters
- `image_url`: Must be valid URL
- `video_url`: Must be valid URL
- `rating`: Float between 0.0 and 5.0
- `notes`: Max 1000 characters

### Tag Categories
Recommended tag categories for consistency:

**Dietary:**
- `vegetarian`, `vegan`, `gluten-free`, `dairy-free`, `nut-free`, `keto`, `paleo`

**Meal Type:**
- `breakfast`, `lunch`, `dinner`, `snack`, `dessert`, `appetizer`, `side-dish`

**Cooking Method:**
- `baked`, `grilled`, `fried`, `steamed`, `slow-cooker`, `instant-pot`, `no-cook`

**Time:**
- `quick` (under 30 min), `30-minute`, `1-hour`, `make-ahead`, `meal-prep`

**Cuisine:**
- `italian`, `mexican`, `indian`, `chinese`, `thai`, `mediterranean`, `american`

**Special:**
- `kid-friendly`, `budget`, `healthy`, `comfort-food`, `holiday`, `summer`, `winter`

## Example Complete Recipe

```json
{
  "id": "recipe_001",
  "title": "Classic Margherita Pizza",
  "description": "Traditional Italian pizza with fresh tomatoes, mozzarella, and basil",
  "cuisine": "Italian",
  "difficulty": "Medium",
  "prep_time": 120,
  "cook_time": 15,
  "total_time": 135,
  "servings": 4,
  "ingredients": [
    {
      "item": "Pizza dough",
      "amount": "500g",
      "notes": "Store-bought or homemade",
      "category": "base"
    },
    {
      "item": "San Marzano tomatoes",
      "amount": "400g can",
      "notes": "Crushed by hand",
      "category": "sauce",
      "substitutes": ["Regular crushed tomatoes"]
    },
    {
      "item": "Fresh mozzarella",
      "amount": "250g",
      "notes": "Torn into pieces",
      "category": "cheese"
    },
    {
      "item": "Fresh basil leaves",
      "amount": "20 leaves",
      "notes": "For garnish",
      "category": "herbs"
    },
    {
      "item": "Extra virgin olive oil",
      "amount": "3 tbsp",
      "notes": "For drizzling",
      "category": "oil"
    }
  ],
  "instructions": [
    "Preheat oven to 250°C (480°F) with pizza stone inside",
    "Let pizza dough come to room temperature (1 hour)",
    "Stretch dough into 4 individual pizzas on floured surface",
    "Spread crushed tomatoes evenly, leaving border for crust",
    "Add torn mozzarella pieces evenly across surface",
    "Slide pizza onto hot stone and bake 10-12 minutes",
    "Remove when crust is golden and cheese is bubbly",
    "Garnish with fresh basil and drizzle with olive oil",
    "Serve immediately while hot"
  ],
  "tags": ["italian", "pizza", "vegetarian", "comfort-food", "traditional"],
  "nutrition": {
    "calories": 420,
    "protein": "18g",
    "carbs": "52g",
    "fat": "16g",
    "fiber": "3g",
    "sodium": "680mg"
  },
  "rating": 4.7,
  "review_count": 156,
  "image_url": "https://example.com/images/margherita-pizza.jpg",
  "created_by": "chef_giovanni",
  "created_at": "2024-10-01T14:30:00Z",
  "updated_at": "2024-10-01T14:30:00Z",
  "is_public": true,
  "source": "Traditional Neapolitan recipe",
  "notes": "For best results, use a pizza stone and highest oven temperature"
}
```

## Database Considerations

### Indexing
- Index on `tags` for fast filtering
- Index on `cuisine` for cuisine-based searches
- Index on `difficulty` and `total_time` for filtering
- Full-text index on `title`, `description`, and `ingredients.item`

### Relationships
- Many-to-many relationship with users (favorites)
- One-to-many relationship with ratings/reviews
- Many-to-many relationship with meal plans