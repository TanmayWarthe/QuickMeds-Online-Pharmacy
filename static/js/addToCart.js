// Cart functionality
let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

function updateCartCount() {
    const cartCount = document.getElementById('cartCount');
    if (cartCount) {
        cartCount.textContent = cartItems.length;
    }
}

function addToCart(productId, productName, price) {
    const item = {
        id: productId,
        name: productName,
        price: price,
        quantity: 1
    };
    
    const existingItem = cartItems.find(item => item.id === productId);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cartItems.push(item);
    }
    
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    updateCartCount();
}

// Initialize cart count when page loads
document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
});