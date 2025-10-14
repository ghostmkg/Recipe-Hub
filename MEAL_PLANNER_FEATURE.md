# 🍽️ Meal Planner Feature

## Overview
A comprehensive meal planning system that allows users to:
- Create and manage weekly meal plans
- Add specific recipes to planned meals with serving sizes
- Auto-generate shopping lists from meal plans
- Track nutritional information for planned meals
- Share meal plans with others

## New Features Added

### Backend Components

#### 1. Database Models (`app/models/meal_plan.py`)
- **MealPlan**: Core meal plan with name, description, date range, and public/private settings
- **PlannedMeal**: Individual meals in a plan (breakfast, lunch, dinner, snack) with recipe links
- **ShoppingList**: Auto-generated shopping lists from meal plans
- **ShoppingListItem**: Individual items in shopping lists with purchase tracking

#### 2. API Schemas (`app/schemas/meal_plan.py`)
- Pydantic models for request/response validation
- Support for CRUD operations on meal plans and planned meals
- Shopping list and nutrition summary schemas

#### 3. Service Layer (`app/services/meal_plan_service.py`)
- Business logic for meal plan management
- Shopping list generation with ingredient aggregation
- Nutrition calculation (mock implementation ready for real data)
- Permission-based access control

#### 4. API Endpoints (`app/api/v1/meal_plans.py`)
- `POST /meal-plans` - Create new meal plan
- `GET /meal-plans` - List user's meal plans
- `GET /meal-plans/{id}` - Get specific meal plan
- `PUT /meal-plans/{id}` - Update meal plan
- `DELETE /meal-plans/{id}` - Delete meal plan
- `POST /meal-plans/{id}/meals` - Add meal to plan
- `POST /meal-plans/{id}/shopping-list` - Generate shopping list
- `GET /meal-plans/{id}/nutrition` - Get nutrition summary

### Frontend Components

#### 1. Meal Planner Dashboard (`src/components/MealPlannerDashboard.tsx`)
- Complete meal planning interface
- Calendar-based meal scheduling
- Shopping list management with purchase tracking
- Nutrition summary display
- Responsive design with Tailwind CSS

#### 2. API Integration (`src/lib/meal-plan-api.ts`)
- TypeScript API client for all meal planning endpoints
- Type-safe request/response handling
- Authentication support

#### 3. Updated Main App (`src/App.tsx`)
- Added navigation to meal planner
- Feature showcase on home page

## Key Features

### 1. Meal Planning
- Create weekly/custom date range meal plans
- Add recipes to specific days and meal types
- Specify serving sizes for accurate shopping lists
- Add notes for meal customizations

### 2. Smart Shopping Lists
- Automatically aggregate ingredients from all planned meals
- Group items by category (Produce, Dairy, Meat, etc.)
- Track purchase status
- Prevent duplicate ingredients

### 3. Nutrition Tracking
- Calculate total calories, protein, carbs, and fat
- Per-meal and total plan summaries
- Visual nutrition dashboard

### 4. Social Features
- Make meal plans public to share with community
- Private meal plans for personal use

## Technical Implementation

### Database Schema
```sql
-- Core tables for meal planning
meal_plans (id, name, description, user_id, start_date, end_date, is_public, created_at, updated_at)
planned_meals (id, meal_plan_id, recipe_id, meal_date, meal_type, servings, notes, created_at)
shopping_lists (id, meal_plan_id, name, created_at, updated_at)
shopping_list_items (id, shopping_list_id, ingredient_name, quantity, unit, category, is_purchased, notes)
```

### API Architecture
- RESTful API design
- JWT authentication
- Input validation with Pydantic
- Error handling and proper HTTP status codes

### Frontend Architecture
- React with TypeScript
- Component-based architecture
- State management with React hooks
- Responsive design with Tailwind CSS

## Future Enhancements
1. **Recipe Integration**: Connect with actual recipe database for ingredient extraction
2. **Grocery Store Integration**: Map ingredients to store locations/prices
3. **Meal Plan Templates**: Pre-made meal plans for different dietary preferences
4. **Collaborative Planning**: Family/household meal planning features
5. **Mobile App**: React Native implementation
6. **AI Suggestions**: ML-powered meal recommendations based on preferences

## Installation Notes
The feature requires:
- Backend: FastAPI, SQLAlchemy, Pydantic
- Frontend: React, TypeScript, Tailwind CSS, Lucide React icons
- Database: PostgreSQL or SQLite

This feature significantly enhances the Recipe Hub platform by adding practical meal planning functionality that goes beyond simple recipe sharing, making it a comprehensive cooking and meal management solution.