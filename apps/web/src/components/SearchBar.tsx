import React, { useState, useCallback } from 'react';
import { SearchFilters } from '../lib/types';

interface SearchBarProps {
  onSearch: (filters: SearchFilters) => void;
  onClear?: () => void;
  placeholder?: string;
  className?: string;
  showFilters?: boolean;
  initialFilters?: SearchFilters;
}

const SearchBar: React.FC<SearchBarProps> = ({
  onSearch,
  onClear,
  placeholder = "Search recipes...",
  className = '',
  showFilters = true,
  initialFilters = {}
}) => {
  const [query, setQuery] = useState(initialFilters.query || '');
  const [category, setCategory] = useState(initialFilters.category || '');
  const [difficulty, setDifficulty] = useState(initialFilters.difficulty || '');
  const [maxPrepTime, setMaxPrepTime] = useState(initialFilters.max_prep_time || '');
  const [showAdvancedFilters, setShowAdvancedFilters] = useState(false);

  const categories = [
    'All',
    'Breakfast',
    'Lunch',
    'Dinner',
    'Dessert',
    'Snack',
    'Appetizer',
    'Beverage',
    'Soup',
    'Salad',
    'Main Course',
    'Side Dish'
  ];

  const difficulties = ['All', 'Easy', 'Medium', 'Hard'];

  const handleSearch = useCallback(() => {
    const filters: SearchFilters = {
      query: query.trim() || undefined,
      category: category && category !== 'All' ? category : undefined,
      difficulty: difficulty && difficulty !== 'All' ? difficulty : undefined,
      max_prep_time: maxPrepTime ? parseInt(maxPrepTime) : undefined,
    };

    onSearch(filters);
  }, [query, category, difficulty, maxPrepTime, onSearch]);

  const handleClear = useCallback(() => {
    setQuery('');
    setCategory('');
    setDifficulty('');
    setMaxPrepTime('');
    if (onClear) {
      onClear();
    }
  }, [onClear]);

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <div className={`w-full max-w-4xl mx-auto ${className}`}>
      {/* Main Search Input */}
      <div className="relative">
        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg
            className="h-5 w-5 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </div>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder={placeholder}
          className="block w-full pl-10 pr-20 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-lg"
        />
        <div className="absolute inset-y-0 right-0 flex items-center">
          <button
            onClick={handleClear}
            className="px-3 py-2 text-gray-400 hover:text-gray-600 transition-colors"
            title="Clear search"
          >
            <svg className="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <button
            onClick={handleSearch}
            className="ml-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
          >
            Search
          </button>
        </div>
      </div>

      {/* Advanced Filters */}
      {showFilters && (
        <div className="mt-4">
          <button
            onClick={() => setShowAdvancedFilters(!showAdvancedFilters)}
            className="flex items-center text-sm text-blue-600 hover:text-blue-800 transition-colors"
          >
            <svg
              className={`h-4 w-4 mr-1 transition-transform ${showAdvancedFilters ? 'rotate-180' : ''}`}
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
            </svg>
            Advanced Filters
          </button>

          {showAdvancedFilters && (
            <div className="mt-3 p-4 bg-gray-50 rounded-lg grid grid-cols-1 md:grid-cols-3 gap-4">
              {/* Category Filter */}
              <div>
                <label htmlFor="category" className="block text-sm font-medium text-gray-700 mb-1">
                  Category
                </label>
                <select
                  id="category"
                  value={category}
                  onChange={(e) => setCategory(e.target.value)}
                  className="block w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                >
                  {categories.map((cat) => (
                    <option key={cat} value={cat === 'All' ? '' : cat}>
                      {cat}
                    </option>
                  ))}
                </select>
              </div>

              {/* Difficulty Filter */}
              <div>
                <label htmlFor="difficulty" className="block text-sm font-medium text-gray-700 mb-1">
                  Difficulty
                </label>
                <select
                  id="difficulty"
                  value={difficulty}
                  onChange={(e) => setDifficulty(e.target.value)}
                  className="block w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                >
                  {difficulties.map((diff) => (
                    <option key={diff} value={diff === 'All' ? '' : diff}>
                      {diff}
                    </option>
                  ))}
                </select>
              </div>

              {/* Max Prep Time Filter */}
              <div>
                <label htmlFor="prepTime" className="block text-sm font-medium text-gray-700 mb-1">
                  Max Prep Time (minutes)
                </label>
                <input
                  type="number"
                  id="prepTime"
                  value={maxPrepTime}
                  onChange={(e) => setMaxPrepTime(e.target.value)}
                  placeholder="e.g., 30"
                  min="0"
                  className="block w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default SearchBar;