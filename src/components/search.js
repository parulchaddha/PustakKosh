import React, { useState } from "react";

function SearchBar(props) {
  const [searchTerm, setSearchTerm] = useState("");

  function handleSearch(event) {
    event.preventDefault();
    props.onSearch(searchTerm);
  }

  function handleInputChange(event) {
    setSearchTerm(event.target.value);
  }

  return (
    <form onSubmit={handleSearch}>
      <input
        type="text"
        placeholder="Search..."
        value={searchTerm}
        onChange={handleInputChange}
      />
      <button type="submit">Search</button>
    </form>
  );
}

export default SearchBar;
