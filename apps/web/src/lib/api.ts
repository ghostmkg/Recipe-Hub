// Recipe Hub API Client

import axios, { AxiosInstance, AxiosResponse } from 'axios';
import { 
  Recipe, 
  RecipeWithDetails, 
  User, 
  Rating, 
  SearchFilters, 
  ApiResponse, 
  PaginatedResponse 
} from './types';

// Configure Axios instance
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';
const axiosInstance: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Optional: Add request/response interceptors for common tasks like error handling or authentication
axiosInstance.interceptors.request.use(
  (config) => {
    // Add authorization token if available
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle specific error codes, e.g., redirect on 401 Unauthorized
    if (error.response && error.response.status === 401) {
      console.error('Unauthorized access. Redirecting to login...');
      // window.location.href = '/login'; // Example redirection
    }
    return Promise.reject(error);
  }
);

// Define API functions
export const api = {
  // Recipe related API calls
  recipes: {
    getAll: async (page = 1, limit = 10): Promise<PaginatedResponse<RecipeWithDetails>> => {
      const response: AxiosResponse<PaginatedResponse<RecipeWithDetails>> = 
        await axiosInstance.get(`/recipes?page=${page}&limit=${limit}`);
      return response.data;
    },
    getById: async (id: number): Promise<RecipeWithDetails> => {
      const response: AxiosResponse<RecipeWithDetails> = await axiosInstance.get(`/recipes/${id}`);
      return response.data;
    },
    create: async (recipeData: Omit<Recipe, 'id' | 'created_at' | 'created_by'>): Promise<Recipe> => {
      const response: AxiosResponse<Recipe> = await axiosInstance.post('/recipes', recipeData);
      return response.data;
    },
    update: async (id: number, recipeData: Partial<Recipe>): Promise<Recipe> => {
      const response: AxiosResponse<Recipe> = await axiosInstance.put(`/recipes/${id}`, recipeData);
      return response.data;
    },
    delete: async (id: number): Promise<void> => {
      await axiosInstance.delete(`/recipes/${id}`);
    },
    search: async (filters: SearchFilters): Promise<PaginatedResponse<RecipeWithDetails>> => {
      const response: AxiosResponse<PaginatedResponse<RecipeWithDetails>> = 
        await axiosInstance.get('/recipes/search', { params: filters });
      return response.data;
    },
  },

  // User related API calls
  users: {
    getProfile: async (): Promise<User> => {
      const response: AxiosResponse<User> = await axiosInstance.get('/users/profile');
      return response.data;
    },
    updateProfile: async (userData: Partial<User>): Promise<User> => {
      const response: AxiosResponse<User> = await axiosInstance.put('/users/profile', userData);
      return response.data;
    },
    register: async (userData: { username: string; email: string; password: string }): Promise<User> => {
      const response: AxiosResponse<User> = await axiosInstance.post('/users/register', userData);
      return response.data;
    },
    login: async (credentials: { email: string; password: string }): Promise<{ user: User; token: string }> => {
      const response: AxiosResponse<{ user: User; token: string }> = 
        await axiosInstance.post('/users/login', credentials);
      return response.data;
    },
  },

  // Rating related API calls
  ratings: {
    rateRecipe: async (recipeId: number, rating: { stars: number; comment?: string }): Promise<Rating> => {
      const response: AxiosResponse<Rating> = await axiosInstance.post(`/ratings/${recipeId}`, rating);
      return response.data;
    },
    updateRating: async (ratingId: number, rating: { stars: number; comment?: string }): Promise<Rating> => {
      const response: AxiosResponse<Rating> = await axiosInstance.put(`/ratings/${ratingId}`, rating);
      return response.data;
    },
    deleteRating: async (ratingId: number): Promise<void> => {
      await axiosInstance.delete(`/ratings/${ratingId}`);
    },
  },
};