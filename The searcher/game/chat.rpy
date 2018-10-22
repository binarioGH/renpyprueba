#-*-coding: utf-8-*-
define n = Character(" ", kind=nvl)
label chat2:
    w"Ya sabes lo que tienes que hacer..."
    "..."
    "Algo le pasó a la computadora."
    "En el escritorio hay un archivo .txt"
    menu:
        "Abrir":
            n"Dejanos solos..."
    return
label chat:
    w"Hola"
    y"Hola"
    w"Ya tengo el paquete que me pediste"
    y"Iré por el mañana en la mañana"
    "Parece que por eso es que Will desapareció, ¿quien es este tal Wolf?"

    menu:
        "Seguir leyendo.":
            jump chat2
        "Seguir buscando en la habitación.":
            $tv = True