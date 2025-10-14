// types.ts

export interface Recipe {
  id: number;
  title: string;
  description: string;
  ingredients: string[];
  instructions: string[];
  prep_time: number; // in minutes
  cook_time: number; // in minutes
  servings: number;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  cuisine: string;
  image_url?: string;
  created_at: string;
  updated_at: string;
  author_id: number;
  author_name?: string;
  average_rating?: number;
  total_ratings?: number;
}

export interface Rating {
  id: number;
  recipe_id: number;
  user_id: number;
  rating: number; // 1-5 stars
  comment?: string;
  created_at: string;
  user_name?: string;
}

export interface User {
  id: number;
  name: string;
  email: string;
  avatar_url?: string;
}

export interface SearchFilters {
  query?: string;
  cuisine?: string;
  difficulty?: string;
  max_prep_time?: number;
  max_cook_time?: number;
  min_rating?: number;
}