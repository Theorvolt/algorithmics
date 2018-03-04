
import random
import queue
from pynode.main import *

def create_model():
    #random.seed(42) #Sets rng to seed 42 for test case

    # Builds up the graph
    building_info = {0:["Church", 100, 0], 1:["Police station",100,0]} #Stores building info and various percentages

    connection_matrix = [[0,4],
                        [3,0],] # Stores all distances between buildings as a matrix, with 0 indicating no connection
    
    heuristics = [] # ¯\_(ツ)_/¯

    #people_states = {0:"alive",1:"alive",2:"alive",3:"alive",4:"alive",5:"alive",6:"alive",7:"alive",8:"alive",9:"alive"} # list of people and their states

    states = ["dead","alive","zombie"]


    people_states = {}
    for p in range(300):
        people_states[p] = random.choice(states)


    # Generates all buildings with info attributes
    for h in range(len(building_info)):
        node = graph.add_node(h)
        number = node.id()
        buildtype, zombie_death, survive_chance = building_info[number][0], building_info[number][1], building_info[number][2]

        node.set_label(str(buildtype)+ "\n" + "Infect chance: " + str(zombie_death) + "\n" + "Survive chance: " + str(survive_chance), 1)
        node.set_attribute("info", [ buildtype, zombie_death, survive_chance])
        node.set_attribute("people", [])


    # Generates the edges, uses x vector to navigate rows and y vector to navigate columns
    for u in range(len(connection_matrix)):
        for y in range(len(connection_matrix)):
            pos2 = connection_matrix[u][y]
            if pos2 == 0: # If it is 0, then no connection
                continue
            graph.add_edge(u, y, weight=pos2, directed=True) # Add the connection otherwise


    # Populates the town
    for t in range(len(people_states)):
        node = random.choice(graph.nodes()) # chooses a random building
        node.attribute("people").append(t) # adds them to the building


    for i in range(len(building_info)): # Attaches the label that writes the number of people present
        node = graph.nodes()[i] # Grabs all nodes in order
        people = node.attribute("people")
        dead, alive, zombie = 0, 0, 0

        # One of the essential checks
        for j in range(len(people)): # Runs a loop for all the people in the attribute people list and tally up the different types of people
            a = people[j]
            if people_states[a] == "dead": dead += 1
            if people_states[a] == "alive": alive += 1
            if people_states[a] == "zombie": zombie += 1

        node.set_label("Alive: " + str(alive) + "\n" + "Dead: " + str(dead) + "\n" + "Zombie: " + str(zombie),0) # Writes the label


# You dont see anything here. Totally nothing its just your imagination. Dont touch!
def infection_algorithm(building,zombie_power):
    # Initial infection goes here, will choose a person to infect


    # Loop 0 logic goes here, determines infections

    Loop2 = queue.Queue()
    Loop3 = queue.PriorityQueue()

    # Begins Loop 1 
    for i in range(len(building_info)):
        node = graph.nodes()[i]
        for t in range(len(node.attribute("people"))):

            if people_states[node.attribute("people")[t]] == "dead":
                continue
            nextElement = node.attribute("people").pop()
            nextElement.append(i) # Adds the building number
            # so now the nextElement should look like : ["person_x","building_number"]
            Loop2.put(nextElement)

    # Begins Loop 2
    while not Loop2.empty():
        info = Loop2.get()
        nodes = graph.nodes()[info[2]]
        e = nodes.adjacent_nodes()

    # Loop 3 logic goes here

begin_pynode(create_model)
