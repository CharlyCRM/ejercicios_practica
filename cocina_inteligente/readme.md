# Proyecto: Cocina Inteligente (Cocina Fantasma)

## 🎯 Objetivo

Diseñar y simular un sistema de gestión para una **cocina fantasma inteligente** que optimice la preparación y entrega de pedidos.
El diseño practica **POO de nivel medio** con herencia, composición, excepciones personalizadas, persistencia JSON y el patrón Strategy para asignación de tareas.

---

## 📁 Estructura del proyecto (corregida y coherente)

```
/cocina_inteligente
├── modelos.py         # Entidades transversales: Ingrediente, Receta
├── inventario.py      # Gestión de stock (sobre Ingrediente) 
├── estaciones.py      # Estaciones de cocina (abstracta y concretas)
├── asignacion.py      # Estrategias de asignación de pedidos (Strategy)
├── pedidos.py         # Pedido y LibroPedidos (gestor de cola)
├── repositorio.py     # Persistencia JSON
├── excepciones.py     # Excepciones de dominio
└── main.py            # Simulación/CLI mínima
```

> **Nota**: Se elimina cualquier mención a `ingredientes.py`. Los ingredientes se definen en `modelos.py`.

---

## 🧰 Librerías necesarias

Solo librería estándar: `dataclasses`, `abc`, `typing`, `json`, `pathlib`, `datetime`, `uuid`, `random`.

---

## 🧩 Especificación por fichero (clases, atributos y métodos)

### 1) `excepciones.py`
- **`ErrorDominio`** (base): excepción genérica del dominio.
- **`StockInsuficiente`**: no hay stock suficiente para preparar una receta.
- **`EstacionOcupada`**: una estación no puede aceptar más tareas.
- **`PedidoInasignable`**: ninguna estación puede asumir el pedido con la estrategia actual.
- **`RecetaInviable`**: la receta está mal definida (ingredientes faltantes o cantidades ≤ 0).

---

### 2) `modelos.py`
Entidades reutilizables por todo el dominio.

- **`Ingrediente`**
  - **Atributos**: `id:str`, `nombre:str`, `unidad:str` (p.ej. "g", "ml", "unidad"), `descripcion:str|None`.
  - **Métodos**:
    - `__str__()`: representación legible.

- **`Receta`**
  - **Atributos**: `id:str`, `nombre:str`, `tiempo_preparacion_min:int`, `ingredientes: dict[str, float]` (mapa `id_ingrediente → cantidad`), `categoria:str|None` (p.ej. "plancha", "horno").
  - **Métodos**:
    - `validar() -> None`: valida que los ingredientes y tiempos sean correctos; si no, lanza `RecetaInviable`.
    - `ingredientes_requeridos() -> dict[str,float]`: devuelve el mapeo crudo (copia defensiva).
    - `multiplicar(cantidad:int) -> dict[str,float]`: devuelve requerimientos escalados para `cantidad` raciones.

> Las clases de **estaciones** y **pedido** NO van aquí para evitar ambigüedad. Ver ficheros dedicados abajo.

---

### 3) `inventario.py`
Maneja existencias de `Ingrediente`.

- **`Inventario`**
  - **Atributos**: `stock: dict[str, float]` (mapa `id_ingrediente → cantidad_disponible`).
  - **Métodos**:
    - `cantidad_disponible(id_ingrediente:str) -> float`: consulta.
    - `reponer(id_ingrediente:str, cantidad:float) -> None`: incrementa stock (cantidad > 0).
    - `puede_satisfacer(receta:Receta, cantidad:int) -> bool`: verifica si hay stock suficiente para todos los ingredientes requeridos.
    - `consumir_para(receta:Receta, cantidad:int) -> None`: descuenta stock según receta×cantidad; si falta algo, lanza `StockInsuficiente`.
    - `to_json() -> dict` / `from_json(data:dict) -> Inventario`: serialización.

---

### 4) `estaciones.py`
Modelo de estaciones de cocina.

- **`EstacionCocina`** *(abstracta)*
  - **Atributos**: `id:str`, `nombre:str`, `especialidades:set[str]` (categorías que puede preparar), `capacidad:int` (tareas simultáneas), `ocupadas:int`.
  - **Métodos**:
    - `acepta_receta(receta:Receta) -> bool`: comprueba si la receta entra en sus especialidades.
    - `disponible() -> bool`: `ocupadas < capacidad`.
    - `asignar() -> None`: incrementa `ocupadas` si hay hueco; si no, `EstacionOcupada`.
    - `liberar() -> None`: decrementa `ocupadas` (no baja de 0).
    - `tiempo_estimado(receta:Receta, cantidad:int) -> int`: devuelve minutos estimados (implementación por defecto: `receta.tiempo_preparacion_min * cantidad`).

- **`EstacionPlancha`** *(concreta)*
  - **Comportamiento**: puede aplicar un factor de **+10%** de rapidez para recetas de categoría "plancha" (si decides modelarlo así en `tiempo_estimado`).

- **`EstacionHorno`** *(concreta)*
  - **Comportamiento**: penalización de **+20%** si la receta no es de "horno".

- **`EstacionFritos`** *(concreta)*
  - **Comportamiento**: rendimiento constante; sin ajustes por categoría.

> Los ajustes son sugerencias para introducir polimorfismo; puedes afinarlos.

---

### 5) `pedidos.py`
Cola y ciclo de vida de pedidos.

- **`Pedido`**
  - **Atributos**: `id:str`, `receta:Receta`, `cantidad:int`, `estado:str` ("pendiente"|"en_preparacion"|"listo"|"cancelado"), `fecha_limite:datetime|None`.
  - **Métodos**:
    - `marcar_en_preparacion()`, `marcar_listo()`, `marcar_cancelado()`.

- **`LibroPedidos`**
  - **Atributos**: `pedidos:list[Pedido]`.
  - **Métodos**:
    - `agregar(pedido:Pedido) -> None`.
    - `pendientes() -> list[Pedido]`: filtra por estado.
    - `siguientes(n:int|None=None) -> list[Pedido]`: devuelve los próximos `n` pendientes (p.ej. ordenados por `fecha_limite`).
    - `actualizar(pedido:Pedido) -> None`.
    - `limpiar() -> None`.

---

### 6) `asignacion.py` (Patrón Strategy)
Decide **a qué estación** va cada pedido y **cuándo**.

- **`EstrategiaAsignacion`** *(abstracta)*
  - `asignar(pedido:Pedido, estaciones:list[EstacionCocina], inventario:Inventario) -> EstacionCocina`: devuelve estación o lanza `PedidoInasignable`.

- **`AsignacionPorEspecialidad`**
  - Prioriza estaciones que **aceptan** la receta y estén `disponible()`.

- **`AsignacionBalanceada`**
  - Selecciona la estación con **menor carga** (`ocupadas/capacidad`) que acepte la receta; si empate, el menor `tiempo_estimado`.

> Cualquier estrategia debe **validar stock** antes de asignar; en caso contrario, `StockInsuficiente`.

---

### 7) `repositorio.py`
Persistencia JSON.

- **`RepositorioJSON`**
  - **Métodos**:
    - `guardar_inventario(inventario:Inventario) -> Path`.
    - `guardar_pedidos(libro:LibroPedidos) -> Path`.
    - `cargar_inventario() -> Inventario`.
    - `cargar_pedidos() -> LibroPedidos`.

> Puedes añadir helpers `to_json()/from_json()` en las entidades cuando lo necesites.

---

### 8) `main.py`
Simulación sin menús largos.

- **Funciones sugeridas**:
  - `inicializar_escenario() -> tuple[Inventario, list[EstacionCocina], LibroPedidos]`.
  - `simular(estrategia:EstrategiaAsignacion, ciclos:int) -> None`: en cada ciclo: tomar siguientes pedidos → validar stock → asignar estación → consumir inventario → marcar estados → liberar estaciones.
  - `main() -> None`: CLI con flags `--estrategia (especialidad|balanceada)`, `--ciclos`, `--pedidos`, `--inventario`.

---

## 📏 Reglas de negocio

1. No se puede preparar un pedido sin `Inventario` suficiente (`StockInsuficiente`).
2. Una estación solo asume recetas de **sus especialidades** y si `disponible()`.
3. Al asignar, la estrategia **debe** verificar stock y disponibilidad; si no, `PedidoInasignable`.
4. La estación aumenta `ocupadas` al recibir tarea y la reduce al finalizar.
5. Los pedidos con `fecha_limite` más próxima **deben priorizarse** en `LibroPedidos.siguientes()`.

---

## 🔬 Casos de uso (mínimos)

- Alta de ingredientes y reposición de stock en `Inventario`.
- Alta de recetas y validación (`Receta.validar`).
- Alta de estaciones (plancha/horno/fritos) con capacidades distintas.
- Alta de pedidos y paso de estados.
- Asignación por especialidad; simulación balanceada.
- Persistencia/carga de inventario y pedidos via `RepositorioJSON`.

---

## 🚀 Ejemplo de ejecución

```bash
python -m cocina_inteligente.main --estrategia especialidad --ciclos 10 --pedidos datos/pedidos.json --inventario datos/inventario.json
```

```bash
python -m cocina_inteligente.main --estrategia balanceada --ciclos 20 --aleatorio 15 --semilla 1234
```

---

## 🏆 Extensiones (bonus)

- Patrón **Observer** para logs de eventos (asignado, iniciado, finalizado, error).
- Cálculo de **SLA** y penalizaciones por retraso.
- **Caducidad** de ingredientes y rotación de stock (FIFO/FEFO).
- **Planificador** simple de tiempos (cola de trabajos por estación).

---

## ✅ Criterios de evaluación

- Cohesión por fichero (cada módulo con una responsabilidad clara).
- Uso correcto de **herencia y polimorfismo** en estaciones y estrategias.
- Manejo de **excepciones de dominio**.
- Persistencia **JSON** funcional con pruebas básicas.
- Código tipado y documentado.
- Simulación reproducible desde CLI.
