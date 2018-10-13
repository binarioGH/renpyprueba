#-*-coding: utf-8-*-
image yuri d = "yuri.png"
image yuri s = "yuri2.png"
image monika d= "mon.png"
image monika s="mon2.png"
image backg = "imagenrandom.jpg"
image backg2 = "hab.jpg"
define m = Character("Monika", color = "#ED7DF1")
define y = Character("Yuri", color = "#B533FF")

label start:
    play music "musicarandom.mp3"
    scene backg with fade
    menu:
        "Monika":
            jump mon
        "Yuri":
            jump yur

label im:
    scene backg2 with fade
    "..."
    "Oh no, he sido teletransportado, debe de ser porque estoy en el mundo de las pruebas."
    window hide None
    $ result = renpy.imagemap("hab_ground.jpg", "hab_hover.jpg",[(600, 525, 739,607, "caja"),(658,251,721,452,"avion"),(1095,211, 1266,550, "plano")])
    if result == "caja":
        jump caja
    elif result == "avion":
        "¿Como llegó ese avión ahí?"
    else:
        "Seguramete esos planos están relacionados con el avión."

    return