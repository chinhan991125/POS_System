const mysql = require('mysql');
const express = require('express');
const path = require('path');
const app = express();
const port = 3306; // You can use any port number

// MySQL connection pool
const pool = mysql.createPool({
    connectionLimit: 10, // Maximum number of connections in the pool
    host: 'localhost', // Database host
    user: 'root', // Database user
    password: 'Intel@123', // Database password
    database: 'pos_system' // Database name
});

// Serve static files from the 'Main Source' directory
app.use(express.static('Main Source'));
app.use(express.json()); // Middleware to parse JSON bodies

// API endpoint for getting products from MySQL
app.get('/api/products', (req, res) => {
    pool.query('SELECT * FROM products', (error, results) => {
        if (error) {
            return res.status(500).json({ error: 'Internal server error' });
        }
        res.json(results);
    });
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/Main Source/POS_UI_NEW.html'));
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

app.post('/api/checkout', (req, res) => {
  const { cartItems, totalPrice } = req.body;
  // Process the checkout here (validation, payment, etc.)
  // For demonstration, we'll just log the received data and respond
  console.log('Received checkout data:', cartItems, totalPrice);
  res.json({ success: true, message: 'Checkout processed successfully' });
});