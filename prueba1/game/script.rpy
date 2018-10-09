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
    m"¿Hoy no has hecho ningun commit? "
    show monika sad:
        ypos 20 xpos 100
    m"¿Como es eso posible?"
    hide monika
    show yuri happy:
        ypos 20 xpos 500
    with dissolve
    y"Hola UwU"
    show yuri d:
        ypos 20 xpos 500
    y"¿Como? ¿Que estás de flojo y no has programado nada?"
    y"Adios >:/"

    return