# Prueba Tecnica TuGerente

## Requerimientos
Utilizando Django REST Framework, desarrollá los endpoints para el sistema de reservas de habitación de un hotel.
CONDICIONES:

- Las reservas pueden tener 3 estados: Pendiente, Pagado y Eliminado.
- Los datos a almacenar para la reserva son: los detalles del cuarto reservado, los días de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago.
- Proponé los endpoints a crearse para tratar de cubrir el flujo normal de operación de reserva y explicar por qué.
Luego que tengas ya todo el código
- Crear un repositorio para la entrega del código y en un readme del repositorio la justificación de los endpoints creados

## Solucion
1. Donde todos los procesos de registro se hace en el hotel, o en alguna parte del hotel, donde este django corriendo, solo un superuser puede crear rooms y eliminarlos. Esta solucion esta en el branch just-hotel
2. Una API REST donde un usuario puede registrarse la habitacion y la reserva, una tabla distinta para la facturación. Esta solucion esta en el branch main


## Local

para crear el venv
``` sh
make create-env
```

para hacer las migrations y correr en local

``` sh
make make-migrate-run
```

