# Definición de Hecho (Definition of Done - DoD)

Para que una tarea o historia de usuario dentro del proyecto **StockIA** se considere completamente terminada en cada iteración del ciclo de desarrollo ADSO, debe cumplir con los siguientes criterios de calidad:

1. **Código Fuente:**
   * El código está escrito siguiendo las buenas prácticas de la arquitectura elegida (MVC con Flask/Django).
   * El código está debidamente comentado y respeta las convenciones de nomenclatura (PEP 8 para Python).
   * Se encuentra versionado correctamente en el repositorio Git con commits limpios y descriptivos.

2. **Base de Datos:**
   * Las tablas y relaciones en MySQL están normalizadas y optimizadas.
   * Los scripts de migración o volcado de datos iniciales se ejecutan sin errores.

3. **Pruebas y Validación:**
   * Se han realizado pruebas funcionales manuales de los formularios y flujos de usuario principales.
   * No existen errores críticos (bugs bloqueantes) en la funcionalidad desarrollada.

4. **Documentación:**
   * Las rutas de la API o vistas implementadas están documentadas de forma básica en el repositorio.