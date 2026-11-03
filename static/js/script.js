document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("boton-tema");
    const html = document.documentElement;

    function actualizarTexto() {
        const actual = html.getAttribute("data-bs-theme");
        btn.textContent = actual === "dark" ? "Cambiar a claro ☀️" : "Cambiar a oscuro 🌑";
    }

    actualizarTexto();

    btn.addEventListener("click", function (){
        const actual = html.getAttribute("data-bs-theme");
        const siguiente = actual === "dark" ? "light" : "dark";
        html.setAttribute("data-bs-theme", siguiente);
        actualizarTexto();
    });
});