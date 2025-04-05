// You can use this if loading from an external file:
// fetch('products.json')
//   .then(response => response.json())
//   .then(products => renderProducts(products))
//   .catch(error => console.error('Error loading products:', error));

// Example inline data (can replace with fetch):
const products = [
    {
        name: "Wireless Headphones",
        price: 59.99,
        image: "https://via.placeholder.com/200"
    },
    {
        name: "Smart Watch",
        price: 129.99,
        image: "https://via.placeholder.com/200"
    },
    {
        name: "Bluetooth Speaker",
        price: 89.99,
        image: "https://via.placeholder.com/200"
    },
    {
        name: "VR Headset",
        price: 249.99,
        image: "https://via.placeholder.com/200"
    }
];

function renderProducts(products) {
    const container = document.querySelector('.product-grid');

    products.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';

        card.innerHTML = `
      <img src="${product.image}" alt="${product.name}">
      <h2>${product.name}</h2>
      <p>$${product.price.toFixed(2)}</p>
      <button>Add to Cart</button>
    `;

        container.appendChild(card);
    });
}

// Load products
renderProducts(products);
