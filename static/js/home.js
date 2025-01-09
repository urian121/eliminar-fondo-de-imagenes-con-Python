document.getElementById("image").addEventListener("change", function () {
  if (this.files.length >= 3) {
    alert("Puedes seleccionar un máximo de 3 imágenes.");
    this.value = ""; // Reinicia la selección
  }
});
