document.addEventListener('DOMContentLoaded', function() {
    // Initialize each slider
    initializeSlider('productSlider1', 'prevBtn1', 'nextBtn1');
    initializeSlider('productSlider2', 'prevBtn2', 'nextBtn2');
    initializeSlider('productSlider3', 'prevBtn3', 'nextBtn3');

    // Get all product card images
    const productImages = document.querySelectorAll('.product-card img');
    
    // Update each image with a unique random Picsum photo
    productImages.forEach((img, index) => {
        img.src = `https://picsum.photos/300/200?random=${index + 1}`;
        img.alt = 'Product Image';
        
        // Add error handling
        img.onerror = function() {
            this.src = '/static/img/default-product.png'; // Fallback image path
        };
    });
});

function initializeSlider(sliderId, prevBtnId, nextBtnId) {
    const slider = document.getElementById(sliderId);
    const prevBtn = document.getElementById(prevBtnId);
    const nextBtn = document.getElementById(nextBtnId);
    
    let scrollAmount = 0;
    const scrollStep = 300; // Adjust this value to control scroll distance

    nextBtn.addEventListener('click', function() {
        scrollAmount += scrollStep;
        if (scrollAmount > slider.scrollWidth - slider.clientWidth) {
            scrollAmount = slider.scrollWidth - slider.clientWidth;
        }
        slider.scrollTo({
            left: scrollAmount,
            behavior: 'smooth'
        });
    });

    prevBtn.addEventListener('click', function() {
        scrollAmount -= scrollStep;
        if (scrollAmount < 0) {
            scrollAmount = 0;
        }
        slider.scrollTo({
            left: scrollAmount,
            behavior: 'smooth'
        });
    });
}