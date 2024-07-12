document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("login-form");
    form.addEventListener("submit", async function(event) {
        event.preventDefault();
        
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        
        const response = await fetch("/api/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        });
        
        if (response.ok) {
            const data = await response.json(); // Convertir la respuesta a JSON
            console.log(data.access_token); // Mostrar el token en la consola
            localStorage.setItem('DataEstado', data.access_token); // Guardar el token en localStorage
            window.location.href = "/home";  // Redirigir a la página de inicio
        } else {
            const errorMessage = document.getElementById("error-message");
            errorMessage.textContent = "Credenciales incorrectas. Inténtalo de nuevo.";
        }
    });
});
