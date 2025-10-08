// api.ts

import axios, { AxiosInstance, AxiosResponse } from 'axios';

// 1. Define API endpoint types (optional but good practice)
interface User {
  id: number;
  name: string;
  email: string;
}

interface Post {
  id: number;
  userId: number;
  title: string;
  body: string;
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