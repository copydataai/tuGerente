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
3. No se elabora tanto la logica de negocio de un hotel, la gran mayoria son CRUD's para que el desarrollo haya sido rapido

## Local

para crear el venv
``` sh
make create-env
```

para hacer las migrations y correr en local

``` sh
make make-migrate-run
```

## EndPoints
En la mayoria de los endpoints usan mixins, por que son requests genericas, excepto por clients que son Class APIView.
Las requests __GET__ no requieren autentication(Token), las 
### Postman 
La collection main esta exportado en json, nombre de file main.postman_collection.json
### Clients
- clients/signup/ __POST__

``` json
{
    "first_name": "example",
    "last_name": "last",
    "email": "example@email.com",
    "password": "example123"
}
```
- clients/login/ __POST__

``` json
{
    "email": "example@email.com",
    "password": "example123"
}
```

### Rooms
Solo un superuser puede crear cuartos usando `make make-migrate-run` se crearan las migraciones y la insercion de rooms.
- rooms/ __GET__
- rooms/{id} __GET__
### Reserves
Basandome en que usamos Token como authentication, el Token almacena el id del usuario,
- reserves/ __GET__
- reserves/{id} __GET__
- reserves/ __POST__

``` json
{
    "room": 3,
    "start_date": "2022-03-05",
    "end_date": "2022-04-01"
}
```

- reserves/{id} __PUT__ __PATCH__

### Bills
- bills/ __GET__
- bills/{id} __GET__
- bills/{id} __PUT__ __PATCH__
En el caso de editar un bill sera para agregar el nit o dni del cliente, esta opcion es descartable.
