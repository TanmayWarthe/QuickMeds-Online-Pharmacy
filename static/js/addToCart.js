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


function toggleCart() {
    const sidebar = document.getElementById('cartSidebar');
    sidebar.classList.toggle('active');
}

function updateQuantity(itemId, action) {
    // Add AJAX call to update quantity
}

function removeItem(itemId) {
    // Add AJAX call to remove item
}