import { useState } from "react";

interface SearchBarProps {
  onSearch: (query: string) => void;
}

export default function SearchBar({ onSearch }: SearchBarProps) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(query);
  };

  return (
    <form onSubmit={handleSubmit} className="flex items-center gap-2 mb-6">
      <input
        type="text"
        placeholder="Search by ingredient..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border border-gray-300 p-2 rounded-md w-full"
      />
      <button
        type="submit"
        className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700"
      >
        Search
      </button>
    </form>
  );
}
