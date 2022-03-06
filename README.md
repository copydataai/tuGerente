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

## Endpoints
Los Endpoints son genericos, estos endpoints se hicieron, con la mentalidad de que la API se consume solo en el hotel, es decir personal administrativo, considerando que solo en el hotel se puede reservar.
### Postman
las requests mas usadas se encuentran con el nombre de just-hotel.postman_collection.json
# Clients

- clients/ __GET__ __POST__ __PUT__ __PATCH__

``` json
{
    "first_name": "Example",
    "last_name": "POST",
    "dni": "20220305",
    "country": "BO"
    /*Por default es BO, no es requerido country*/
}
```

## Reserves
- reserves/ __GET__ __POST__ __PUT__ __PATCH__

``` json
{
    "client": 2,/*Id del cliente*/
    "room": 2, /*Id del Room*/
    "start_date": "2022-03-05",
    "end_date": "2022-04-01",
    /*Optional Values with default values*/
    "payment_status": "Pending",
    "payment_method": "Check"
}
```

- rooms/ __GET__
