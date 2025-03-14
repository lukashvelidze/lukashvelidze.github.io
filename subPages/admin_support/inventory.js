document.addEventListener("DOMContentLoaded", function () {
    loadInventory();
});

// Fetch products from Flask API
function loadInventory() {
    fetch("http://127.0.0.1:5000/products")
        .then(response => response.json())
        .then(data => renderTable(data))
        .catch(error => console.error("Error loading inventory:", error));
}

// Render inventory in table
function renderTable(data) {
    const tableBody = document.querySelector("#productTable tbody");
    tableBody.innerHTML = "";

    data.forEach(item => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.category}</td>
            <td>${item.name}</td>
            <td>${item.model}</td>
            <td>${item.stock}</td>
            <td>$${item.price.toFixed(2)}</td>
            <td>
                <button class="edit-btn" onclick="editProduct(${item.id})">Edit</button>
                <button class="delete-btn" onclick="deleteProduct(${item.id})">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// Delete product
function deleteProduct(id) {
    fetch(`http://127.0.0.1:5000/products/${id}`, { method: "DELETE" })
        .then(response => response.json())
        .then(() => loadInventory()) // Refresh the table
        .catch(error => console.error("Error deleting product:", error));
}
