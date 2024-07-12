document.addEventListener("DOMContentLoaded", function() {
    // Obtener el token del localStorage
    const token = localStorage.getItem("DataEstado");

    // Mostrar el token en el elemento HTML con id="token"
    const tokenElement = document.getElementById("token");
    if (token) {
        tokenElement.textContent = token;
    } else {
        tokenElement.textContent = "No se encontró ningún token.";
    }
});
