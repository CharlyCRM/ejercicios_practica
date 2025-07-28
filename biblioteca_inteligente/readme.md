 # Proyecto: Sistema de Gestión de una Biblioteca Inteligente

### 🎯 Objetivo:

Simular el funcionamiento de una biblioteca moderna que incluye préstamos, devoluciones, gestión de usuarios, seguimiento de historial y catálogo. La idea es que cada entidad sea compleja y tenga sus propios métodos bien definidos.

---

### 🧱 Estructura modular del proyecto:

1. libro.py

Clase Libro
	•	Atributos: título, autor, ISBN, año, género, disponible (bool).
	•	Métodos:
	•	marcar_como_prestado()
	•	marcar_como_disponible()
	•	__str__() para mostrar la información.
	•	(Opcional) método para comprobar si es “nuevo” (menos de 2 años) o “antiguo”.

---

2. usuario.py

Clase Usuario
	•	Atributos: nombre, ID, lista de libros prestados (máximo 3), historial de préstamos.
	•	Métodos:
	•	prestar_libro(libro: Libro)
	•	devolver_libro(libro: Libro)
	•	mostrar_historial()
	•	(Opcional) bloqueo si tiene libros sin devolver en más de X días.

---

3. biblioteca.py

Clase Biblioteca
	•	Atributos: catálogo de libros (lista), usuarios registrados.
	•	Métodos:
	•	agregar_libro()
	•	registrar_usuario()
	•	buscar_libro_por_titulo(), buscar_por_autor()
	•	prestar_libro_a_usuario(usuario_id, isbn)
	•	devolver_libro_de_usuario(usuario_id, isbn)
	•	mostrar_catalogo(), mostrar_libros_disponibles()

---

4. main.py
	•	Interfaz del sistema (modo texto simple).
	•	Simulación de flujos: registro, búsqueda, préstamo, devolución, estado del catálogo.