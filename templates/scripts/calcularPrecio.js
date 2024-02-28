function actualizarTotal() {
  var precioBase = 15; // Precio base por ticket
  var precioTotal = precioBase;

  var persona = document.querySelector('input[name="persona"]:checked');
  var ruta = document.querySelector('input[name="ruta"]:checked');
  var cantidadTickets = document.getElementById('cantidad_tickets').value;

  if (persona && ruta && cantidadTickets) {
    // Calcular precio total basado en la elección de estudiante/docente, ruta y cantidad de tickets
    precioTotal = precioBase * cantidadTickets;

    if (persona.value === "docente") {
      precioTotal += 5 * cantidadTickets; // Los docentes pagan 5 Bs. más por ticket
    }

    if (ruta.value === "Valera") {
      precioTotal += 5 * cantidadTickets; // La ruta a Valera cuesta 5 Bs. más por ticket
    }
  }

  document.getElementById('totalPrecio').textContent = precioTotal;
}