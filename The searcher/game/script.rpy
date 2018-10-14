#-*-coding: utf-8-*-
define w = Character("Wolf",kind = nvl,color="#3383FF")
define y = Character("Fox", kind = nvl, color ="#FF9933")
image bg = "h.jpg"
label start:
    $ password = "ABCD123" 
    $ psw = 1
    $ llave = False
    scene bg with fade
    "Tengo que encontrar la contraseña de la computadora..."
    while True:
        window hide None
        $r = renpy.imagemap("h_ground.jpg", "h_hover.jpg",[(5,276,195,458,"tv"),(155,82,316,414,"mueble"),(525,323,609,386,"pc"),(677,429,757,489,"cajon")])
        if r == "tv":
            "No creo que sea momento de ver la Televisión."
        elif r == "mueble":
            "Encontré una llave, quizá despues me sea util."
            $llave = True
        elif r == "cajon":
            if llave == True:
                "Encontré una nota que parece que tiene una contraseña ´ABCD123´"
            else:
                "Está cerrado con llave"
        elif r == "pc":
            if psw == 1:
                $inp = renpy.input("Contraseña: ")
                if inp == password:
                    "Parece que esa es la contraseña."
                    $psw = False
            else:
                jump chat 




