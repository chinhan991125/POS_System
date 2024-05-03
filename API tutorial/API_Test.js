fetch('http://localhost:5000/checkout', { // Update the URL to match your Flask app's location
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
    // Handle success (e.g., show a confirmation message)
})
.catch((error) => {
    console.error('Error:', error);
    // Handle errors here
});