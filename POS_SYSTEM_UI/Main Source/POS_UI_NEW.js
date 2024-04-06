var products = [
    {id: 1, name: 'Product 1', price: 10, image: 'product1.jpg'},
    {id: 2, name: 'Product 2', price: 20, image: 'product2.jpg'},
    {id: 3, name: 'Product 3', price: 30, image: 'product3.jpg'},
    {id: 4, name: 'Product 4', price: 40, image: 'Mineral Water.jpg'},
    {id: 5, name: 'Product 5', price: 50, image: 'watches.jpg'},
    {id: 6, name: 'Product 6', price: 60, image: 'panadol.jpg'}
];
var cart = [];

function addToCart(id, quantity) {
    var product = products.find(function(product) {
        return product.id === id;
    });

    // Check if the product is already in the cart
    var existingProduct = cart.find(function(item) {
        return item.id === id;
    });

    if (existingProduct) {
        // If the product is already in the cart, update its quantity
        existingProduct.quantity += parseInt(quantity);
    } else {
        // If the product is not in the cart, add it
        product.quantity = parseInt(quantity);
        cart.push(product);
    }

    renderCart();
}

function removeFromCart(id) {
    cart = cart.filter(function(product) {
        return product.id !== id;
    });

    renderCart();
}

function renderProducts() {
    var productList = document.getElementById('product-list');
    productList.innerHTML = '';

    products.forEach(function(product) {
        var productItem = document.createElement('div');
        productItem.className = 'product-item';
        productItem.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>Price: $${product.price}</p>
            <button onclick="addToCart(${product.id}, 1)">Add to Cart</button>
        `;
        productList.appendChild(productItem);
    });
}

function renderCart() {
    var cartList = document.getElementById('cart-list');
    cartList.innerHTML = '';

    var totalPrice = 0;
    cart.forEach(function(product) {
        var cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <div><h3>${product.name}</h3></div>
            <div><p>Price: $${product.price}</p></div>
            <div class="quantity-box"> <!-- Added class for quantity box -->
                <p>Quantity:</p> <!-- Label for quantity -->
                <div class="quantity-number">${product.quantity}</div> <!-- Quantity number box -->
            </div>
            <button onclick="removeFromCart(${product.id})">&#10060;</button>
        `;
        cartList.appendChild(cartItem);

        totalPrice += product.price * product.quantity;
    });

    document.getElementById('total-price-value').innerText = totalPrice;
}






renderProducts();
