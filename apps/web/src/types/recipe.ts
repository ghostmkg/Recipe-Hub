export interface Recipe {
  id: number;
  title: string;
  description?: string;
  ingredients: string;
  steps: string;
  tags?: string;
  image?: string;
  created_by?: number;
  created_at: string;
}

export interface RecipeCreate {
  title: string;
  description?: string;
  ingredients: string;
  steps: string;
  tags?: string;
  image?: string;
}
