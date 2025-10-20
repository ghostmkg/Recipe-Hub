"""
RECIPE MANAGEMENT APP - Python
A simple application to manage, add, and search recipes
"""

import json
import os

class RecipeManager:
    def __init__(self, filename="recipes.json"):
        self.filename = filename
        self.recipes = self.load_recipes()
    
    def load_recipes(self):
        """Load recipes from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_recipes(self):
        """Save recipes to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.recipes, f, indent=2)
    
    def add_recipe(self, name, ingredients, instructions, prep_time, servings):
        """Add a new recipe"""
        if name.lower() in [r.lower() for r in self.recipes]:
            print("❌ Recipe already exists!")
            return False
        
        self.recipes[name] = {
            "ingredients": ingredients,
            "instructions": instructions,
            "prep_time": prep_time,
            "servings": servings
        }
        self.save_recipes()
        print(f"✅ Recipe '{name}' added successfully!")
        return True
    
    def view_recipe(self, name):
        """View a specific recipe"""
        for recipe_name in self.recipes:
            if recipe_name.lower() == name.lower():
                recipe = self.recipes[recipe_name]
                print("\n" + "=" * 50)
                print(f"🍳 {recipe_name.upper()}")
                print("=" * 50)
                print(f"⏱️  Prep Time: {recipe['prep_time']} minutes")
                print(f"👥 Servings: {recipe['servings']}")
                print("\n📝 INGREDIENTS:")
                for ingredient in recipe['ingredients']:
                    print(f"  • {ingredient}")
                print("\n📖 INSTRUCTIONS:")
                for i, instruction in enumerate(recipe['instructions'], 1):
                    print(f"  {i}. {instruction}")
                print("=" * 50 + "\n")
                return True
        
        print("❌ Recipe not found!")
        return False
    
    def list_recipes(self):
        """List all recipes"""
        if not self.recipes:
            print("❌ No recipes found!")
            return
        
        print("\n" + "=" * 50)
        print("📚 ALL RECIPES")
        print("=" * 50)
        for i, recipe_name in enumerate(self.recipes, 1):
            recipe = self.recipes[recipe_name]
            print(f"{i}. {recipe_name} ({recipe['prep_time']} min, {recipe['servings']} servings)")
        print("=" * 50 + "\n")
    
    def search_recipe(self, keyword):
        """Search recipes by keyword"""
        found = []
        for name in self.recipes:
            if keyword.lower() in name.lower():
                found.append(name)
        
        if found:
            print(f"\n🔍 Search results for '{keyword}':")
            for recipe in found:
                print(f"  • {recipe}")
            print()
        else:
            print(f"❌ No recipes found for '{keyword}'")
    
    def delete_recipe(self, name):
        """Delete a recipe"""
        for recipe_name in list(self.recipes.keys()):
            if recipe_name.lower() == name.lower():
                del self.recipes[recipe_name]
                self.save_recipes()
                print(f"✅ Recipe '{name}' deleted!")
                return True
        
        print("❌ Recipe not found!")
        return False
    
    def edit_recipe(self, name):
        """Edit an existing recipe"""
        for recipe_name in self.recipes:
            if recipe_name.lower() == name.lower():
                print(f"\n✏️ Editing '{recipe_name}'")
                print("Leave empty to keep current value")
                
                new_ingredients = input("New ingredients (comma-separated) or skip: ").strip()
                if new_ingredients:
                    self.recipes[recipe_name]['ingredients'] = [i.strip() for i in new_ingredients.split(',')]
                
                new_instructions = input("New instructions (use | to separate steps) or skip: ").strip()
                if new_instructions:
                    self.recipes[recipe_name]['instructions'] = new_instructions.split('|')
                
                new_time = input("New prep time (minutes) or skip: ").strip()
                if new_time:
                    self.recipes[recipe_name]['prep_time'] = int(new_time)
                
                new_servings = input("New servings or skip: ").strip()
                if new_servings:
                    self.recipes[recipe_name]['servings'] = int(new_servings)
                
                self.save_recipes()
                print("✅ Recipe updated!")
                return True
        
        print("❌ Recipe not found!")
        return False

def main():
    """Main application loop"""
    manager = RecipeManager()
    
    print("=" * 50)
    print("🍽️  WELCOME TO RECIPE MANAGER")
    print("=" * 50)
    
    while True:
        print("\n📋 MENU:")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. List All Recipes")
        print("4. Search Recipe")
        print("5. Edit Recipe")
        print("6. Delete Recipe")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            print("\n➕ ADD NEW RECIPE")
            name = input("Recipe name: ").strip()
            
            ingredients_input = input("Ingredients (comma-separated): ").strip()
            ingredients = [i.strip() for i in ingredients_input.split(',')]
            
            instructions_input = input("Instructions (use | to separate steps): ").strip()
            instructions = instructions_input.split('|')
            
            prep_time = int(input("Prep time (minutes): ").strip())
            servings = int(input("Servings: ").strip())
            
            manager.add_recipe(name, ingredients, instructions, prep_time, servings)
        
        elif choice == '2':
            recipe_name = input("Enter recipe name: ").strip()
            manager.view_recipe(recipe_name)
        
        elif choice == '3':
            manager.list_recipes()
        
        elif choice == '4':
            keyword = input("Enter search keyword: ").strip()
            manager.search_recipe(keyword)
        
        elif choice == '5':
            recipe_name = input("Enter recipe name to edit: ").strip()
            manager.edit_recipe(recipe_name)
        
        elif choice == '6':
            recipe_name = input("Enter recipe name to delete: ").strip()
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                manager.delete_recipe(recipe_name)
        
        elif choice == '7':
            print("\n👋 Thanks for using Recipe Manager! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()