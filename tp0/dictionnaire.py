#Dictionnaire de gestion de stocks
#suivit du stock pour chaque robot 

pieces_stock = {
    "ModeleA": {"moteurs": 10, "capteurs": 25, "roues" : 40},
    "ModeleB": {"moteurs": 6, "capteurs": 15, "roues" : 24},
}


def quantite_piece(pieces_stock, robot_modele, piece):
    """
    Retourne la quantité de pièces disponibles pour un modèle de robot.
    """
    if robot_modele in pieces_stock:
        if piece in pieces_stock[robot_modele]:
            return pieces_stock[robot_modele][piece]
    return -1


assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

def consommer_piece(pieces_stock, model, piece, quantite):
    """
    Consomme une quantité de pièces pour un modèle de robot.
    Retourne True si la consommation a été effectuée avec succès, False sinon.
    """
    if model in pieces_stock:
        if piece in pieces_stock[model]:
            if pieces_stock[model][piece] >= quantite:
                pieces_stock[model][piece] -= quantite
                return True
    return False

def ajouter_modele(pieces_stock, model, moteurs = 0, capteurs = 0, roues = 0):
    """
    Ajoute un nouveau modèle de robot au dictionnaire des stocks.
    Retourne True si le modèle a été ajouté avec succès, False sinon.
    """
    if model not in pieces_stock :
        pieces_stock[model] = {"moteurs": moteurs, "capteurs": capteurs, "roues" : roues}
        return True
    return False

def total_pieces(pieces_stock):
    """
    Retourne le total des pièces disponibles pour chaque piece.
    """
    total_moteurs, total_capteurs, total_roues = 0, 0, 0
    for model in pieces_stock:
        total_moteurs += pieces_stock[model]["moteurs"]
        total_capteurs += pieces_stock[model]["capteurs"]
        total_roues += pieces_stock[model]["roues"]
    return {"moteurs": total_moteurs, "capteurs": total_capteurs, "roues" : total_roues}

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

ajouter_modele(pieces_stock, "ModeleC", moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == \
{"moteurs": 4, "capteurs": 10, "roues": 16}

totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}