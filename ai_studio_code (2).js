// Add to Cart Simulation
let cartCount = 0;
function addToCart() {
    cartCount++;
    const countElement = document.getElementById('cartCount');
    countElement.innerText = cartCount;
    countElement.style.transform = 'scale(1.3)';
    setTimeout(() => {
        countElement.style.transform = 'scale(1)';
    }, 200);
    alert('প্রোডাক্টটি সফলভাবে কার্টে যোগ করা হয়েছে!');
}

// Flash Sale Countdown Logic
function updateCountdown() {
    const timers = document.querySelectorAll('.countdown-timer');

    timers.forEach(timer => {
        let secSpan = timer.querySelector('.seconds');
        let minSpan = timer.querySelector('.minutes');
        let hourSpan = timer.querySelector('.hours');

        let sec = parseInt(secSpan.innerText);
        let min = parseInt(minSpan.innerText);
        let hr = parseInt(hourSpan.innerText);

        if (sec > 0) {
            sec--;
        } else {
            sec = 59;
            if (min > 0) {
                min--;
            } else {
                min = 59;
                if (hr > 0) {
                    hr--;
                }
            }
        }

        secSpan.innerText = sec < 10 ? '0' + sec : sec;
        minSpan.innerText = min < 10 ? '0' + min : min;
        hourSpan.innerText = hr < 10 ? '0' + hr : hr;
    });
}
setInterval(updateCountdown, 1000);

// Scroll to Top Button Logic
const scrollTopBtn = document.getElementById('scrollToTopBtn');

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        scrollTopBtn.style.display = 'flex';
    } else {
        scrollTopBtn.style.display = 'none';
    }
});

scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Search input interaction
document.getElementById('searchInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        alert('Searching for: ' + this.value);
    }
});