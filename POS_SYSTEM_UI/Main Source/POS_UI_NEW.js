// Define products and cart arrays
var products = [
    { id: 1, name: 'Product 1', price: 10, image: 'Product Image/product1.jpg' },
    { id: 2, name: 'Product 2', price: 20, image: 'Product Image/product2.jpg' },
    { id: 3, name: 'Product 3', price: 30, image: 'Product Image/product3.jpg' },
    { id: 4, name: 'Product 4', price: 40, image: 'Product Image/Mineral Water.jpg' },
    { id: 5, name: 'Product 5', price: 50, image: 'Product Image/watches.jpg' },
    { id: 6, name: 'Product 6', price: 60, image: 'Product Image/panadol.jpg' }
];
var cart = [];

// Function to add product to cart
function addToCart(id, quantity) {
    // Find the product by id
    var product = products.find(product => product.id === id);
    if (!product) {
        console.error('Product not found');
        return;
    }

    // Check if the product is already in the cart
    var existingProduct = cart.find(item => item.id === id);
    if (existingProduct) {
        // If the product is already in the cart, update its quantity
        existingProduct.quantity += parseInt(quantity);
    } else {
        // If the product is not in the cart, add a deep copy of it
        var productCopy = { ...product, quantity: parseInt(quantity) };
        cart.push(productCopy);
    }

    // Render the updated cart
    renderCart();
}

// Function to remove product from cart
function removeFromCart(id) {
    cart = cart.filter(product => product.id !== id);
    renderCart();
}

// Function to render products on page load
function renderProducts() {
    var productList = document.getElementById('product-list');
    productList.innerHTML = '';

    products.forEach(product => {
        var productItem = document.createElement('div');
        productItem.className = 'product-item';
        productItem.innerHTML = `
            <img src="${product.image}" alt="${product.name}" style="width:100px; height:auto;">
            <h3>${product.name}</h3>
            <p>Price: $${product.price}</p>
            <button onclick="addToCart(${product.id}, 1)">Add to Cart</button>
        `;
        productList.appendChild(productItem);
    });
}

// Function to render the shopping cart
function renderCart() {
    var cartList = document.getElementById('cart-list');
    cartList.innerHTML = '';

    var totalPrice = 0;
    cart.forEach(product => {
        var cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <div><h3>${product.name}</h3></div>
            <div><p>Price: $${product.price}</p></div>
            <div class="quantity-box">
                <p>Quantity:</p>
                <div class="quantity-number">${product.quantity}</div>
            </div>
            <button onclick="removeFromCart(${product.id})">&#10060;</button>
        `;
        cartList.appendChild(cartItem);

        totalPrice += product.price * product.quantity;
    });

    document.getElementById('total-price-value').innerText = totalPrice.toFixed(2);
}

function checkout() {
    // Assuming `cart` is your shopping cart array and you have a way to calculate `total_price`
    let total_price = cart.reduce((acc, item) => acc + (item.price * item.quantity), 0);

    // Prepare the data in the format expected by your API
    let data = {
        user_name: "John Doe", // You might want to dynamically set this based on user input or session
        transaction_date: new Date().toISOString().slice(0, 19).replace('T', ' '), // Current date-time in 'YYYY-MM-DD HH:MM:SS' format
        region: "North America", // This could also be dynamically set or selected by the user
        total_price: total_price,
        products: cart.map(item => ({ product_name: item.name, quantity: item.quantity }))
    };

    // Send the data to your API
    fetch('http://localhost:5000/upload-transaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Handle success - maybe clear the cart or show a success message
    })
    .catch((error) => {
        console.error('Error:', error);
        // Handle errors here, such as showing an error message to the user
    });
}
// Initial render of products on page load
renderProducts();
