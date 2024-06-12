// Modified products array with region-specific prices
var products = [
    { id: 1, name: 'Toy', prices: { BA: 10, DF: 11, ES: 9, GO: 10, MG: 12, MS: 10, MT: 11, PB: 9, PR: 10, RJ: 12, RS: 11, SP: 10, SC: 9 }, image: 'Product Image/toy.jpg' },
    { id: 2, name: 'Aircon', prices: { BA: 20, DF: 22, ES: 19, GO: 20, MG: 25, MS: 20, MT: 21, PB: 19, PR: 20, RJ: 23, RS: 21, SP: 20, SC: 19 }, image: 'Product Image/aircon.jpg' },
    { id: 3, name: 'Perfume', prices: { BA: 30, DF: 33, ES: 29, GO: 30, MG: 35, MS: 30, MT: 31, PB: 29, PR: 30, RJ: 33, RS: 31, SP: 30, SC: 29 }, image: 'Product Image/perfume.jpg' },
    { id: 4, name: 'Watches', prices: { BA: 40, DF: 44, ES: 39, GO: 40, MG: 45, MS: 40, MT: 41, PB: 39, PR: 40, RJ: 44, RS: 41, SP: 40, SC: 39 }, image: 'Product Image/watches.jpg' },
    { id: 5, name: 'Flower', prices: { BA: 50, DF: 55, ES: 49, GO: 50, MG: 60, MS: 50, MT: 51, PB: 49, PR: 50, RJ: 55, RS: 51, SP: 50, SC: 49 }, image: 'Product Image/flower.jpg' },
    { id: 6, name: 'Drink', prices: { BA: 60, DF: 66, ES: 59, GO: 60, MG: 70, MS: 60, MT: 61, PB: 59, PR: 60, RJ: 66, RS: 61, SP: 60, SC: 59 }, image: 'Product Image/Mineral Water.jpg' }
];
var cart = [];
var selectedRegion = 'BA'; // Default region

// Function to add product to cart
function addToCart(id, quantity) {
    var product = products.find(product => product.id === id);
    if (!product) {
        console.error('Product not found');
        return;
    }

    var existingProduct = cart.find(item => item.id === id);
    if (existingProduct) {
        existingProduct.quantity += parseInt(quantity);
    } else {
        var productCopy = { ...product, quantity: parseInt(quantity), price: product.prices[selectedRegion] };
        cart.push(productCopy);
    }

    renderCart();
}

// Function to remove product from cart
function removeFromCart(id) {
    cart = cart.filter(product => product.id !== id);
    renderCart();
}

// Function to render products based on selected region
function renderProducts() {
    var productList = document.getElementById('product-list');
    productList.innerHTML = '';

    products.forEach(product => {
        var productItem = document.createElement('div');
        productItem.className = 'product-item';
        productItem.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>Price: $${product.prices[selectedRegion]}</p>
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

// Function to handle region selection
function handleRegionChange(region) {
    selectedRegion = region;
    renderProducts();
    cart = []; // Optionally clear the cart or update prices in the cart
    renderCart();
}

document.getElementById('update-prices-button').addEventListener('click', function() {
    // Assuming 'selectedRegion' holds the current region
    products.forEach(product => {
        getDynamicPricing(selectedRegion, product.id);
    });
});

function getDynamicPricing(region, productId) {
    fetch('http://localhost:5000/get_dynamic_pricing', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ region: region, product_id: productId }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Dynamic price for product', productId, ':', data.price);
        // Update the UI with the received price
        // This requires a way to find the product's price element in the DOM and update it
        updateProductPrice(productId, data.price);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function updateProductPrice(productId, newPrice) {
    // Implement this function to find the product's price element in the DOM and update it with the new price
    // This is an example; adjust it to match your actual DOM structure
    document.querySelector(`#product-price-${productId}`).innerText = `$${newPrice}`;
}

// Initial render of products and fetch predicted prices
document.addEventListener('DOMContentLoaded', function() {
    renderProducts();
    // Add event listener for region selection (assuming a select element with id 'region-select')
    document.getElementById('region-select').addEventListener('change', function(e) {
        handleRegionChange(e.target.value);
    });
});

function checkout() {
    // Validate if the cart is empty
    if (cart.length === 0) {
        alert("Your cart is empty. Please add some products before checking out.");
        return;
    }

    // Calculate total price
    let total_price = cart.reduce((acc, item) => acc + (item.price * item.quantity), 0);

    // Prepare the data in the format expected by your API
    let data = {
        user_name: "John Doe", // Dynamically set based on user input or session
        transaction_date: new Date().toISOString().slice(0, 19).replace('T', ' '), // Current date-time in 'YYYY-MM-DD HH:MM:SS' format
        region: "North America", // Dynamically set or selected by the user
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
        
        // Store the cart data in localStorage for the payment page to access
        localStorage.setItem('cart', JSON.stringify(cart));
        console.log('Cart stored:', JSON.stringify(cart));

        // Optionally, clear the cart after successful transaction
        cart = [];

        // Show a success message
        alert('Transaction successful! Redirecting to payment page...');

        // Redirect to the payment page
        window.location.href = 'payment.html';
    })
    .catch((error) => {
        console.error('Error:', error);
        // Show an error message to the user
        alert('Transaction failed. Please try again.');
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // This ensures the DOM is fully loaded before trying to find the button

    var checkoutButton = document.getElementById('checkout-button');
    if (checkoutButton) {
        checkoutButton.addEventListener('click', function() {
            window.location.href = 'payment.html'; // Adjust the path to your payment page as necessary
        });
    } else {
        console.error('Checkout button not found');
    }
});
// Initial render of products on page load