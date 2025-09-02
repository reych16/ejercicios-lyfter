#1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    #- `nombre`
    #- `numero_de_estrellas`
    #- `habitaciones`
#El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    #- `numero`
    #- `piso`
    #- `precio_por_noche`

hotel_dict = {
    'name' : 'Hotel Royal Cancun',
    'number_of_stars' : 4,
    'rooms' : [
        {
        'room_number' : 101,
        'floor' : 1,
        'price_night' : 350,
        },

        {
        'room_number' : 202,
        'floor' : 2,
        'price_night' : 300,
        },

        {
        'room_number' : 303,
        'floor' : 3,
        'price_night' : 285
        }
    ]
}

print(f"El precio por noche de la habitación {hotel_dict['rooms'][1]['room_number']} es de: {hotel_dict['rooms'][1]['price_night']}")

