# Historias de Usuario - StockIA

Este documento recopila las historias de usuario iniciales para el desarrollo del sistema de inventarios con alertas predictivas orientado a pequeños comercios de barrio.

## HU-01: Registro y Control de Entradas y Salidas de Mercancía
* **Como** tendero o administrador del comercio,
* **Quiero** registrar de forma ágil la entrada de nuevos productos y la salida por ventas diarias,
* **Para** mantener actualizado el stock en tiempo real y evitar descuadres físicos.

### Criterios de Aceptación:
1. El sistema debe permitir registrar el nombre, categoría, cantidad, precio de compra y precio de venta del producto.
2. Cada venta o reposición debe actualizar automáticamente el inventario disponible.
3. Se debe generar un registro de auditoría (historial de movimientos) con fecha y hora.

---

## HU-02: Módulo de Alertas Predictivas de Desabastecimiento
* **Como** comerciante minorista,
* **Quiero** recibir alertas automáticas cuando un producto esté próximo a agotarse según su ritmo histórico de ventas,
* **Para** realizar pedidos a proveedores a tiempo y no perder ventas por desabastecimiento.

### Criterios de Aceptación:
1. El sistema debe analizar el promedio de ventas diarias de los últimos 30 días.
2. Debe calcular el stock mínimo recomendado utilizando la fórmula:
   $$Stock_{min} = V_{diaria} \times T_{entrega}$$
   (Donde $V_{diaria}$ es la velocidad de venta diaria y $T_{entrega}$ el tiempo estimado de reposición en días).
3. Si el stock actual es menor o igual al $Stock_{min}$, la interfaz debe mostrar una alerta visual destacada (color rojo) en el panel principal.

---

## HU-03: Dashboard de Estadísticas de Rotación
* **Como** administrador del negocio,
* **Quiero** visualizar gráficos estadísticos sobre los productos de alta y baja rotación,
* **Para** tomar decisiones informadas sobre qué productos comprar más o cuáles liquidar.

### Criterios de Aceptación:
1. El panel principal (Dashboard) debe incluir gráficos de barras o pastel interactivos.
2. Debe mostrar el Top 5 de productos más vendidos en el mes.
3. Debe permitir filtrar los reportes por rangos de fechas personalizados.