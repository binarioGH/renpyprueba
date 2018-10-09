#-*-coding: utf-8-*-
image monika default= "mon.png"
image monika sad="mon2.png"
image backg = "imagenrandom.jpg"
define cgc = Character("Monika", color = "#ED7DF1")
label start:
    play music "musicarandom.mp3"
    scene backg with fade
    show monika default
    with dissolve
    cgc"¿Hoy no has hecho ningun comit? "
    show monika sad
    cgc"¿Como es eso posible?"
    return