# Proyecto: Red de Drones Autónomos para Reparto Urbano

## 🎯 Objetivo

Diseñar y simular un sistema de reparto con **drones autónomos** en una ciudad.  
El sistema gestionará:

- **Flota** (modelos de drones con distintas capacidades).  
- **Pedidos** (peso, prioridad, plazos).  
- **Rutas simples** (distancias Manhattan).  
- **Baterías** (consumo y recarga).  
- **Estrategias de asignación** (implementadas con polimorfismo y Strategy Pattern).  

El objetivo es practicar **POO de nivel medio**, incluyendo **herencia**, **composición**, **excepciones propias**, **persistencia JSON** y **patrones de diseño**.

---

## 🧰 Librerías necesarias

Todo se puede resolver con la **librería estándar de Python**:  

- `dataclasses`  
- `abc`  
- `typing`  
- `json`  
- `pathlib`  
- `random`  
- `datetime`  
- `uuid`

*(Opcional)*: `pytest` para tests unitarios.

---

## 🧱 Estructura recomendada del proyecto

/drones
├── models.py          # Clases de drones (abstracta y concretas)
├── battery.py         # Lógica de batería y consumo
├── strategy.py        # Estrategias de asignación (Strategy Pattern)
├── orders.py          # Pedidos y estados
├── city.py            # Ciudad y utilidades de distancia
├── fleet.py           # Flota, registro y orquestación
├── repository.py      # Persistencia en JSON
├── exceptions.py      # Excepciones propias del dominio
└── main.py            # Script de simulación (CLI mínima)

---

## 🧩 Clases y métodos principales

### `exceptions.py`
- `DomainError`: Excepción base.  
- `CapacityExceeded`: Pedido excede capacidad.  
- `LowBattery`: No hay batería suficiente.  
- `UnassignableOrder`: Ningún drone puede asumir el pedido.  

---

### `orders.py`
#### `Order`
- Atributos: `id`, `weight_kg`, `priority`, `pickup`, `dropoff`, `deadline`, `status`.  
- Métodos:  
  - `distance()`: Calcula distancia Manhattan.  
  - `mark_assigned()`: Marca como asignado.  
  - `mark_delivered()`: Marca como entregado.  
  - `mark_failed(reason)`: Marca como fallido con motivo.  

#### `OrderBook`
- Métodos:  
  - `add(order)`: Añadir pedido.  
  - `pending(priority_first=True)`: Lista pedidos pendientes.  
  - `update(order)`: Actualiza estado.  
  - `clear()`: Limpia pedidos.  

---

### `battery.py`
#### `Battery`
- Atributos: `capacity_wh`, `current_wh`, `recharge_rate_w`.  
- Métodos:  
  - `level()`: Devuelve % de carga.  
  - `can_consume(wh)`: Comprueba si hay energía suficiente.  
  - `consume(wh)`: Resta energía.  
  - `recharge(minutes)`: Simula recarga.  

---

### `models.py` (drones)
#### `Drone (abstracta)`
- Atributos: `id`, `max_payload_kg`, `speed_mps`, `battery`, `pos`, `busy`.  
- Métodos:  
  - `can_carry(kg)`: Comprueba si puede llevar la carga.  
  - `estimate_energy(distance, payload)`: **Abstracto**, estima consumo.  
  - `travel_time_s(distance)`: Calcula tiempo de viaje.  
  - `move_and_deliver(order, city)`: Ejecuta entrega y consume batería.  
  - `available()`: Verifica disponibilidad.  

#### `LightDrone`  
- Optimizado para cargas pequeñas (más eficiente).  

#### `HeavyDrone`  
- Optimizado para cargas pesadas (más consumo).  

---

### `city.py`
#### `City`
- Atributos: `name`, `width`, `height`, `depot`.  
- Métodos:  
  - `manhattan(a, b)`: Distancia Manhattan.  
  - `meters(distance)`: Conversión a metros.  
  - `inside(p)`: Verifica si coordenada está dentro de la ciudad.  
  - `nearest_charger(p)`: Devuelve el cargador más cercano.  

---

### `strategy.py` (Strategy Pattern)
#### `AssignmentStrategy (abstracta)`
- `assign(order, fleet, city)`: Decide qué drone asignar.  

#### `GreedyNearest`  
- Elige el drone más cercano y disponible.  

#### `PriorityFirst`  
- Elige en base a prioridad y tiempo estimado de entrega.  

---

### `fleet.py`
#### `Fleet`
- Métodos:  
  - `register(drone)`: Añadir drone.  
  - `available()`: Lista de drones libres.  
  - `dispatch(order, strategy, city)`: Asigna un pedido usando una estrategia.  
  - `recharge_all(minutes, city)`: Recarga todos los drones libres.  
  - `relocate_to_depot(city)`: Mueve drones al depósito.  
  - `report()`: Devuelve informe textual.  

---

### `repository.py`
#### `JsonRepository`
- Métodos:  
  - `save_fleet(fleet)`: Guarda drones y estado.  
  - `save_orders(orders)`: Guarda pedidos.  
  - `load_orders()`: Carga pedidos desde JSON.  
  - `load_fleet()`: Carga flota desde JSON.  

---

### `main.py`
- `seed_scenario()`: Crea ciudad, flota y pedidos iniciales.  
- `simulate(strategy, steps)`: Corre la simulación paso a paso.  
- `main()`: Punto de entrada.  

---

## 📏 Reglas de negocio

1. Un pedido no puede superar la capacidad del drone.  
2. El consumo de batería debe considerar toda la ruta.  
3. Si un drone no tiene batería suficiente, el pedido falla.  
4. Estrategias deben justificar su selección (distancia, prioridad, etc.).  
5. Los drones pueden recargarse en ciclos de simulación.  
6. Pedidos prioritarios deben intentarse asignar primero.  

---

## 🔬 Casos de uso básicos

- Registrar drones de diferentes tipos.  
- Cargar pedidos desde JSON.  
- Asignar pedidos con `GreedyNearest`.  
- Reintentar pedidos fallidos con `PriorityFirst`.  
- Guardar reporte final de estado.  

---

## 🚀 Ejemplo de ejecución

```bash
python -m drones.main --strategy greedy --orders data/orders.json --steps 20
# o
python -m drones.main --strategy priority --random 30 --seed 42

---

🏆 Extensiones (bonus)
	•	Patrón Observer/Logger para eventos.
	•	Penalizaciones por clima aleatorio.
	•	Mantenimiento de drones tras N vuelos.
	•	Dashboard textual con estado de baterías y pedidos.

⸻

✅ Criterios de evaluación
	•	Diseño OO claro y extensible.
	•	Uso de herencia, composición y polimorfismo.
	•	Manejo de excepciones personalizadas.
	•	Persistencia en JSON funcional.
	•	Código con typing y docstrings.
	•	Simulación reproducible desde main.py.

# Proyecto: Red de Drones Autónomos para Reparto Urbano

## 🎯 Objetivo

Diseñar y simular un sistema de reparto con **drones autónomos** en una ciudad.  
El sistema gestionará:

- **Flota** (modelos de drones con distintas capacidades).  
- **Pedidos** (peso, prioridad, plazos).  
- **Rutas simples** (distancias Manhattan).  
- **Baterías** (consumo y recarga).  
- **Estrategias de asignación** (implementadas con polimorfismo y Strategy Pattern).  

El objetivo es practicar **POO de nivel medio**, incluyendo **herencia**, **composición**, **excepciones propias**, **persistencia JSON** y **patrones de diseño**.

---

## 🧰 Librerías necesarias

Todo se puede resolver con la **librería estándar de Python**:  

- `dataclasses`  
- `abc`  
- `typing`  
- `json`  
- `pathlib`  
- `random`  
- `datetime`  
- `uuid`

*(Opcional)*: `pytest` para tests unitarios.

---

## 🧱 Estructura recomendada del proyecto

```text
/drones_inteligentes
├── modelos.py         # Clases de drones (abstracta y concretas)
├── bateria.py         # Lógica de batería y consumo
├── estrategias.py     # Estrategias de asignación (Patrón Strategy)
├── pedidos.py         # Pedidos y estados
├── ciudad.py          # Ciudad y utilidades de distancia
├── flota.py           # Flota, registro y orquestación
├── repositorio.py     # Persistencia en JSON
├── excepciones.py     # Excepciones propias del dominio
└── main.py            # Script de simulación (CLI mínima)
```

> Nota: se ha alineado la estructura con el nombre de carpeta **`drones_inteligentes`** que usas en tu ruta local.

---

## 🧩 Clases y métodos principales

### `excepciones.py`
- `ErrorDominio`: Excepción base.  
- `CapacidadExcedida`: El pedido excede la capacidad del dron.  
- `BateriaBaja`: No hay batería suficiente.  
- `PedidoInasignable`: Ningún dron puede asumir el pedido.  

---

### `pedidos.py`
#### `Pedido`
- **Atributos**: `id`, `peso_kg`, `prioridad`, `recogida`, `entrega`, `fecha_limite`, `estado`.  
- **Estados válidos**: `"pendiente" | "asignado" | "entregado" | "fallido"`.  
- **Métodos**:  
  - `distancia_manhattan()`: Calcula distancia Manhattan.  
  - `marcar_asignado()`: Marca como asignado.  
  - `marcar_entregado()`: Marca como entregado.  
  - `marcar_fallido(motivo)`: Marca como fallido con motivo.  

#### `LibroDePedidos`
- **Métodos**:  
  - `agregar(pedido)`: Añade un pedido.  
  - `pendientes(primero_por_prioridad=True)`: Devuelve lista de pendientes (puede ordenar por prioridad/plazo).  
  - `actualizar(pedido)`: Actualiza estado del pedido.  
  - `limpiar()`: Limpia el libro.

---

### `bateria.py`
#### `Bateria`
- **Atributos**: `capacidad_wh`, `carga_wh_actual`, `tasa_recarga_wh_min`.  
- **Métodos**:  
  - `nivel()`: Devuelve % de carga en [0,1].  
  - `puede_consumir(wh)`: Comprueba si hay energía suficiente.  
  - `consumir(wh)`: Resta energía (lanza `BateriaBaja` si no alcanza).  
  - `recargar(minutos)`: Simula recarga.  

---

### `modelos.py` (drones)
#### `Dron` *(abstracta)*
- **Atributos**: `id`, `carga_maxima_kg`, `velocidad_mps`, `bateria`, `posicion`, `ocupado`.  
- **Métodos**:  
  - `puede_cargar(kg)`: Comprueba si puede llevar la carga.  
  - `estimar_energia(distancia_m, carga_kg)`: **Abstracto**, estima consumo en Wh.  
  - `tiempo_viaje_s(distancia_m)`: Calcula tiempo de viaje.  
  - `mover_y_entregar(pedido, ciudad)`: Ejecuta entrega (posición → recogida → entrega) consumiendo batería.  
  - `disponible()`: Verifica disponibilidad.  
  - `establecer_ocupado(valor)`: Marca ocupación.  

#### `DronLigero`  
- Optimizado para cargas pequeñas (más eficiente).  
- Sobrescribe `estimar_energia(...)` con penalización si la carga se acerca al máximo.  

#### `DronPesado`  
- Optimizado para cargas pesadas (más consumo base, menor penalización por peso relativo).  
- Sobrescribe `estimar_energia(...)`.

---

### `ciudad.py`
#### `Ciudad`
- **Atributos**: `nombre`, `ancho`, `alto`, `deposito`.  
- **Métodos**:  
  - `manhattan(a, b)`: Distancia Manhattan.  
  - `metros(distancia_manhattan)`: Conversión de “cuadras” a metros.  
  - `dentro(p)`: Verifica si la coordenada está dentro de la ciudad.  
  - `cargador_mas_cercano(p)`: Devuelve el punto de carga más cercano (por simplicidad, `deposito`).

---

### `estrategias.py` (Patrón Strategy)
#### `EstrategiaAsignacion` *(abstracta)*
- `asignar(pedido, flota, ciudad)`: Decide qué dron asignar o lanza `PedidoInasignable`.  

#### `VorazMasCercano`  
- Elige el dron **más cercano** a `recogida` que cumpla capacidad y batería.  

#### `PrioridadPrimero`  
- Pondera `prioridad` y **tiempo estimado de entrega** (ETA) para seleccionar.  

---

### `flota.py`
#### `Flota`
- **Métodos**:  
  - `registrar(dron)`: Añade un dron a la flota.  
  - `disponibles()`: Devuelve los drones libres con batería suficiente.  
  - `despachar(pedido, estrategia, ciudad)`: Aplica la estrategia, marca ocupación, llama a `mover_y_entregar`, registra y libera. Devuelve tiempo total en segundos.  
  - `recargar_todos(minutos, ciudad)`: Recarga drones libres.  
  - `reubicar_al_deposito(ciudad)`: Mueve drones al depósito cuando estén libres.  
  - `informe()`: Resumen legible (tasa de entrega, ETA medio, batería media, etc.).

---

### `repositorio.py`
#### `RepositorioJSON`
- **Métodos**:  
  - `guardar_flota(flota)`: Serializa drones/baterías/posiciones.  
  - `guardar_pedidos(pedidos)`: Serializa pedidos y estados.  
  - `cargar_pedidos()`: Carga pedidos desde JSON.  
  - `cargar_flota()`: Carga flota desde JSON.  

---

### `main.py`
- `inicializar_escenario()`: Crea ciudad, flota y libro de pedidos.  
- `simular(estrategia, ciclos)`: Ejecuta la simulación por ciclos: asignar → mover/entregar → recargar.  
- `main()`: Punto de entrada (CLI).  

---

## 📏 Reglas de negocio

1. Un pedido no puede superar la **carga máxima** del dron.  
2. El consumo de batería considera la ruta completa `(posición → recogida → entrega)` y el **peso**.  
3. Si no hay energía suficiente, se lanza `BateriaBaja` y el pedido queda `fallido` (o se reintenta con otro dron).  
4. La estrategia debe **justificar** su selección (distancia, prioridad, ETA).  
5. En cada ciclo de simulación los drones libres pueden **recargar**.  
6. Los pedidos con `prioridad=1` deben **intentarse** primero (en `PrioridadPrimero`).  

---

## 🔬 Casos de uso básicos

- Registrar drones de diferentes tipos (`DronLigero`, `DronPesado`).  
- Cargar pedidos desde JSON.  
- Asignar pedidos con `VorazMasCercano`.  
- Reintentar pedidos fallidos con `PrioridadPrimero`.  
- Guardar reporte final y estado con `RepositorioJSON`.  

---

## 🚀 Ejemplo de ejecución

```bash
python -m drones_inteligentes.main --estrategia voraz --pedidos datos/pedidos.json --ciclos 20
# o
python -m drones_inteligentes.main --estrategia prioridad --aleatorios 30 --semilla 42
```

---

## 🏆 Extensiones (bonus)
- Patrón **Observer/Logger** para eventos.  
- Penalizaciones por **clima** aleatorio.  
- **Mantenimiento** de drones tras N vuelos.  
- **Dashboard** textual con estado de baterías y pedidos.  

---

## ✅ Criterios de evaluación
- Diseño OO claro y extensible.  
- Uso de **herencia, composición y polimorfismo**.  
- Manejo de **excepciones** personalizadas.  
- Persistencia en **JSON** funcional.  
- Código con **typing** y **docstrings**.  
- Simulación reproducible desde `main.py`.  