#-*-coding: utf-8-*-
image yuri happy = "yuri.png"
image yuri d = "yuri2.png"
image monika default= "mon.png"
image monika sad="mon2.png"
image backg = "imagenrandom.jpg"
define m = Character("Monika", color = "#ED7DF1")
define y = Character("Yuri", color = "#B533FF")

label start:
    play music "musicarandom.mp3"
    scene backg with fade
    show monika default:
        ypos 20 xpos 100
    with dissolve
    m"Ven aquí Yuri."
    show yuri happy:
        ypos 20 xpos 500
    with dissolve
    y"Hola UwU."
    m"Te hablo para decirte que estamos creando un mod genial :3."
    y"{i}Prueba de texto en italica{/i}"
    m"{b}prueba de texto en bold{/b}"
    y"{s}prueba de texto tachado{/s}"
    m"{u}prueba de texto subrayado{/u}"
    y"Texto pausado {w}... Jejejeje."
    m"Ocupo que te vayas un momento Yuri."
    menu:
        "No, está bien, que se quede":
            y"Está bien, me quedaré."
            $ gby = 1
        "...":
            hide yuri
            $ gby = 0
            m"Ahora estamos solos UwU"
    if gby == 1:
        jump uno
    else:
        jump dos

label uno:
    m"Saltaste a la parte 1."


label dos:
    m"Saltaste a la parte 2."