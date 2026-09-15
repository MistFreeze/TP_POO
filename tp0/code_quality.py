##Nommage des variables à refaire : 
## aucun commentaire dans le code.
# trop d'arguments dans la fonction f, il faut les réduire et les rendre plus clairs.
#Copilot, modifie le code pour qu'il soit plus lisible et plus compréhensible.



def f(terrain, x_depart, y_depart, x_arrivee, y_arrivee):
    """
    Calcule le coût d'un trajet selon le type de route.
    """
    #Calcul de la distance entre deux points
    distance = ((x_arrivee - x_depart) ** 2 + (y_arrivee - y_depart) ** 2) ** 0.5

    if terrain == 'Road':
        cout = distance * 1.0
    elif terrain == 'Highway':
        cout = distance * 1.5
    elif terrain == 'Street':
        cout = distance * 2.0
    else:
        cout = distance * 3.0

    print("cout:", cout)
    return cout