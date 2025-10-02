// Recipe Hub Types

// User interface
export interface User {
  id: number;
  username: string;
  email: string;
  joined_at: string;
}

// Recipe interface
export interface Recipe {
  id: number;
  title: string;
  description: string;
  ingredients: string[];
  steps: string[];
  tags: string[];
  image_url?: string;
  created_by: number;
  created_at: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  prep_time: number; // in minutes
  cook_time: number; // in minutes
  servings: number;
  category: string;
}

// Rating interface
export interface Rating {
  id: number;
  user_id: number;
  recipe_id: number;
  stars: number;
  comment?: string;
  timestamp: string;
}

// Recipe with user info and ratings
export interface RecipeWithDetails extends Recipe {
  author: User;
  average_rating: number;
  total_ratings: number;
  user_rating?: Rating;
}

// Search filters
export interface SearchFilters {
  query?: string;
  category?: string;
  difficulty?: string;
  max_prep_time?: number;
  tags?: string[];
}

// API Response types
export interface ApiResponse<T> {
  data: T;
  message?: string;
  success: boolean;
}

export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  limit: number;
  has_next: boolean;
  has_prev: boolean;
}

// 2. Configure Axios instance
const API_BASE_URL = 'https://jsonplaceholder.typicode.com'; // Example API
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

// 3. Define API functions
export const api = {
  // User related API calls
  users: {
    getAll: async (): Promise<User[]> => {
      const response: AxiosResponse<User[]> = await axiosInstance.get('/users');
      return response.data;
    },
    getById: async (id: number): Promise<User> => {
      const response: AxiosResponse<User> = await axiosInstance.get(`/users/${id}`);
      return response.data;
    },
    create: async (userData: Omit<User, 'id'>): Promise<User> => {
      const response: AxiosResponse<User> = await axiosInstance.post('/users', userData);
      return response.data;
    },
  },

  // Post related API calls
  posts: {
    getAll: async (): Promise<Post[]> => {
      const response: AxiosResponse<Post[]> = await axiosInstance.get('/posts');
      return response.data;
    },
    getById: async (id: number): Promise<Post> => {
      const response: AxiosResponse<Post> = await axiosInstance.get(`/posts/${id}`);
      return response.data;
    },
    create: async (postData: Omit<Post, 'id'>): Promise<Post> => {
      const response: AxiosResponse<Post> = await axiosInstance.post('/posts', postData);
      return response.data;
    },
  },
};