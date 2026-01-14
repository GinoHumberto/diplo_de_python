1. El Sistema de Precios y Tipos de Sala

No todas las entradas valen lo mismo. Podemos implementar lógica para que el precio cambie según:

    El tipo de sala: Salas 2D, 3D o VIP (esto requerirá que tu clase Sala tenga un atributo tipo).

    Horarios y Días: Aplicar descuentos automáticos (ej. "Miércoles de cine") o precios de "Matiné".

2. Gestión de Inventario (El Candy Bar)

Un cine no vive solo de entradas. Podríamos crear un módulo de Venta de Productos:

    Crear una tabla productos (Popcorn, Gaseosas, Nachos).

    Gestionar el Stock: Que el sistema te avise si te estás quedando sin bolsas de pochoclo.

    Registrar una "Venta Completa" que incluya entradas y comida en un solo ticket.

3. Estadísticas y Reportes (El "Modo Jefe")

Como ya tienes una tabla de ventas, el siguiente paso es explotar esos datos:

    Recaudación Total: ¿Cuánto dinero ganamos hoy?

    Película Estrella: ¿Cuál es la película que más asientos ha llenado?

    Ocupación por Sala: Un reporte que diga qué porcentaje de los 10 asientos de cada sala está ocupado.


Si un cliente quiere devolver una entrada porque se arrepintió, ¿cómo harías para "liberar" ese asiento y borrar la venta en la base de datos?
