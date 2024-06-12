document.addEventListener('DOMContentLoaded', function() {
    renderOrderSummary();
});

function renderOrderSummary() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    let total = 0;
    let orderSummaryHtml = '';

    cart.forEach(item => {
        total += item.price * item.quantity;
        orderSummaryHtml += `
            <div class="cart-item">
                <div><h3>${item.name}</h3></div>
                <div><p>Price: $${item.price}</p></div>
                <div><p>Quantity: ${item.quantity}</p></div>
            </div>
        `;
    });

    orderSummaryHtml += `<h3>Total: $${total.toFixed(2)}</h3>`;
    document.getElementById('order-summary').innerHTML = orderSummaryHtml;
}

function processPayment() {
    console.log('Processing payment...');

    // For demonstration, let's just clear the cart and redirect to a success page
    localStorage.removeItem('cart');
    // Assuming the success page exists at 'success.html' in the same directory
    window.location.href = 'success.html';
}

function selectPaymentMethod(selectedMethod) {
    // Log the selected payment method for debugging
    console.log('Selected payment method:', selectedMethod);

    // Get all payment method elements
    const paymentMethods = document.querySelectorAll('.payment-method');

    // Loop through all payment methods
    paymentMethods.forEach(method => {
        // Check if the method matches the selected one
        if(method.getAttribute('data-method') === selectedMethod) {
            // Add the 'selected' class to highlight the method
            method.classList.add('selected');
        } else {
            // Remove the 'selected' class from other methods
            method.classList.remove('selected');
        }
    });
}