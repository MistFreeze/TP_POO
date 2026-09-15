#Journal de bord d'un robot avec des tuples

releve1 = ("laser_avant", 2.35, "m")
releve2 =("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")

releves = [releve1, releve2, releve3]

def afficher_releve(releve):
    nom_capteur = releve[0]
    valeur = releve[1]
    unite = releve[2]
    return f"Capteur {nom_capteur} : {valeur} {unite}"

#can use : nom_capteur, valeur, unite = releve 

#assert, bouleans to know if variable are true or false
#verify the date inside variable. The code does not continue if the assert is false
assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"



def recalibrer(releves, nom_capteur, nouvelle_valeur):
    for i in range(0, len(releves)):
        if releves[i][0] == nom_capteur:
            # Create a new tuple with the updated value
            releves[i] = (releves[i][0], nouvelle_valeur, releves[i][2])
    return releves
nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3