#-*-coding: utf-8-*-
image monika = "mon.png"
image backg = "imagenrandom.jpg"
define cgc = Character("Monika", color = "#ED7DF1")
label start:
    play music "musicarandom.mp3"
    scene backg with fade
    cgc "Gracias por empezarme a crear un mod uwu"
    cgc "Los quiero mucho UwU"
    show monika 
    with dissolve
    cgc "Prueba"
    return