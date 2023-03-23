import React, { useState } from "react";

function BookForm() {
  const [bookName, setBookName] = useState("");
  const [description, setDescription] = useState("");
  const [genre, setGenre] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // handle form submission here
    console.log(`Book name: ${bookName}, Description: ${description}, Genre: ${genre}`);
    // you can replace this with actual form submission logic
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="bookName">Book Name:</label>
      <input
        type="text"
        id="bookName"
        value={bookName}
        onChange={(e) => setBookName(e.target.value)}
      />

      <label htmlFor="description">Description:</label>
      <textarea
        id="description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      ></textarea>

      <label htmlFor="genre">Genre:</label>
      <input
        type="text"
        id="genre"
        value={genre}
        onChange={(e) => setGenre(e.target.value)}
      />

      <button type="submit">Submit</button>
    </form>
  );
}

export default BookForm;
