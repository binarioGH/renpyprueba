#-*-coding: utf-8-*-
image yuri d = "yuri.png"
image yuri s = "yuri2.png"
image monika d= "mon.png"
image monika s="mon2.png"
image backg = "imagenrandom.jpg"
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
    return