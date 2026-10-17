// Show a message when the page loads
console.log("AI Language Translator Loaded Successfully");

// Confirmation before submitting the form
document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            alert("Your translation is being processed...");

        });

    }

});