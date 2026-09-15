#Gestion and ensemble operation

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

#Return a new ensemble without modify the original
def robots_toutes_missions(robots_exploration, robots_transport):
    return robots_exploration.union(robots_transport)


def robots_double_mission(robots_exploration, robots_transport):
    return robots_exploration.intersection(robots_transport)

def robots_exploration_seule(robots_exploration, robots_transport):
    return robots_exploration.difference(robots_transport)


#
double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seule(robots_exploration, robots_transport)





assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}

#Return a new ensemble without modify the original
def ajouter_robot_mission(mission, num_robot):
    return mission.union({num_robot}) #utilisation de {} permet de créer un ensemble avec un seul élément

def retirer_robot_mission(mission, num_robot):
    return mission.difference({num_robot})

ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")