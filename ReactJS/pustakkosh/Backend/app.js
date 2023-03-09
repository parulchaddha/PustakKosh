// Require the necessary modules
const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

// Create the connection pool
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'pustakkosh',
});

// Create the Express app
const app = express();

// Enable CORS
app.use(cors());

// Create a route that queries the database and returns the data as JSON
app.get('/api/item', (req, res) => {
  // Get a connection from the pool
  pool.getConnection((err, connection) => {
    if (err) {
      console.error(err);
      res.status(500).send('Internal server error');
      return;
    }

    // Run the query
    connection.query('SELECT * FROM items', (err, results) => {
      // Release the connection back to the pool
      connection.release();

      if (err) {
        console.error(err);
        res.status(500).send('Internal server error');
        return;
      }

      // Send the data as JSON
      res.json(results);
    });
  });
});

// Start the server
app.listen(5000, () => {
  console.log('Server started on port 5000');
});