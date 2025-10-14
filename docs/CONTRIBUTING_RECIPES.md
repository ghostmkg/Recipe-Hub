# Recipe Contribution Guidelines

## 🍳 How to Add New Recipes

Thank you for contributing to the Open Recipe Hub! Here's how you can add your delicious recipes to our community.

### Recipe Format

All recipes should follow our standardized JSON format:

```json
{
  "id": "unique_id",
  "title": "Recipe Name",
  "description": "Brief description of the dish",
  "cuisine": "Cuisine type (e.g., Italian, Mexican, Indian)",
  "difficulty": "Easy | Medium | Hard",
  "prep_time": 15,  // minutes
  "cook_time": 30,  // minutes
  "servings": 4,
  "ingredients": [
    {
      "item": "Ingredient name",
      "amount": "Quantity with unit",
      "notes": "Optional preparation notes"
    }
  ],
  "instructions": [
    "Step 1: Detailed instruction",
    "Step 2: Next step..."
  ],
  "tags": ["tag1", "tag2", "tag3"],
  "nutrition": {
    "calories": 350,
    "protein": "25g",
    "carbs": "40g",
    "fat": "12g"
  }
}
```

### Required Fields

- **title**: Clear, descriptive recipe name
- **ingredients**: Complete list with measurements
- **instructions**: Step-by-step cooking directions
- **difficulty**: Easy, Medium, or Hard
- **prep_time** & **cook_time**: In minutes
- **servings**: Number of people served

### Optional Fields

- **description**: Brief overview of the dish
- **cuisine**: Cultural origin
- **tags**: Searchable keywords
- **nutrition**: Nutritional information
- **notes**: Additional tips or variations

### Categories

Place your recipe in the appropriate category folder:
- `/data/categories/breakfast.json`
- `/data/categories/lunch.json`
- `/data/categories/dinner.json`
- `/data/categories/desserts.json`
- `/data/categories/vegetarian.json`
- `/data/categories/vegan.json`
- `/data/categories/gluten-free.json`

### Submission Process

1. **Fork** the repository
2. **Create** a new branch for your recipe
3. **Add** your recipe to the appropriate category file
4. **Test** the JSON format (use a JSON validator)
5. **Submit** a pull request with a clear description

### Quality Guidelines

- **Accuracy**: Test your recipe before submitting
- **Clarity**: Write clear, easy-to-follow instructions
- **Completeness**: Include all necessary ingredients and steps
- **Originality**: Credit sources if adapting existing recipes

### Example Tags

Use relevant tags to make recipes discoverable:
- **Dietary**: `vegetarian`, `vegan`, `gluten-free`, `dairy-free`
- **Meal Type**: `breakfast`, `lunch`, `dinner`, `snack`, `dessert`
- **Cooking Method**: `baked`, `grilled`, `no-cook`, `one-pot`
- **Time**: `quick`, `30-minute`, `slow-cooker`, `meal-prep`
- **Cuisine**: `Italian`, `Mexican`, `Asian`, `Mediterranean`

### Need Help?

- Check existing recipes for format examples
- Join our community discussions
- Open an issue if you have questions

Happy cooking! 🍽️