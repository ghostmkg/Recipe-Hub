import React, { useState, ChangeEvent } from 'react';

interface SearchBarProps {
  placeholder?: string;
  onSearch: (query: string) => void;
}

const SearchBar: React.FC<SearchBarProps> = ({ placeholder = "Search...", onSearch }) => {
  const [query, setQuery] = useState<string>("");

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setQuery(value);
    onSearch(value); // Call the parent function when user types
  };

  return (
    <div style={styles.container}>
      <input
        type="text"
        value={query}
        placeholder={placeholder}
        onChange={handleChange}
        style={styles.input}
      />
    </div>
  );
};

export default SearchBar;

// Inline styles (you can move them to a CSS file if preferred)
const styles: Record<string, React.CSSProperties> = {
  container: {
    display: "flex",
    justifyContent: "center",
    margin: "1rem 0",
  },
  input: {
    width: "250px",
    padding: "8px 12px",
    fontSize: "16px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    outline: "none",
  },
};
