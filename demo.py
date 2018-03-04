from pynode.main import *

# TODO 



characters = ["Percy",
        "Annabeth",
        "Zeus",
        "Poseidon",
        "Chiron",
        "Grover",
        "Luke",
        "Hermes",
        "Hades",
        "Athena",
        "Clarisse",
        "Tyson",
        "Kronos",
        "Nico",
        "Ares",
        "Apollo",
        "Dionysus",
        "Thalia",
        "Rachel"]

sizes = [90.6, 196.0, 26.7, 28.8, 63.1, 128.9, 75.2, 22.7, 24.8, 12.1, 35.5, 64.4, 44.0, 50.9, 24.8, 16.9, 33.8, 57.1,33.1]
originalsize = [906, 1960, 267, 288, 631, 1289, 752, 227, 248, 121, 355, 644, 440, 509, 248, 169, 338, 571, 331]
alliance = [Color.BLUE, Color.GREY, Color.YELLOW, Color.BLUE, Color.GREEN, Color.GREEN, Color.BLACK, Color.GREY, Color.RED, Color.GREY, Color.RED, Color.BLUE, Color.BLACK, Color.RED, Color.RED, Color.GREY, Color.GREEN, Color.YELLOW, Color.GREEN]
positions = [(0,0),(500,400),(400,300),(0,100),(300,200),(222,333),(123,333),(250,250),(111,111),(399,399),
(499,399),(231,400),(111,333),(444,222),(333,66),(66,99),(144,169),(255,7),(475,132),(199,245)
]
relations = {

    "Percy":[["Luke","Former friend"], ["Annabeth","Best friend, love interest"],["Grover","Best friend"],["Chiron","Student"],["Poseidon","son"],["Nico","Ally and friend"],["Tyson","Half brother and close friend"], ["Rachel","Friend and love interest"], ["Ares","Enemy"], ["Clarisse", "Bully victim"]   ],
    "Annabeth":[["Luke","Former love interest"], ["Athena","Daughter"], ["Clarisse","Rivals"], ["Grover","Friend"], ["Chiron","Friend"], ["Thalia", "Close friend"]],
    "Zeus":[["Hermes","Father"],["Apollo","Father"],["Poseidon","Brother and rivals"],["Hades","Brother on good terms"],["Kronos","Son, decapitated by Zeus"],["Dionysus","Father"], ["Ares", "Father"]],
    "Poseidon":[ ["Tyson","Father"], ["Kronos","Son and enemy"], ["Hades","Brother"]],
    "Chiron":[ ["Kronos","Son"], ["Dionysus","Old friend"], ["Grover","Colleague and friend"] ],
    "Grover":[ ["Dionysus", "Co-worker"], ["Tyson","Akward terms but friendly"] ],
    "Luke":[["Kronos", "enemy and host of body"], ["Thalia", "former friend"], ["Hermes", "Son"] ],
    "Hermes":[ ["Apollo","Half brother"], ["Athena","Half sister"] ],
    "Hades":[ ["Nico","Father"], ["Kronos", "Son, was consumed  by Kronos"]],
    "Athena":[ ["Percy","Cautious of"]  ],
    "Clarisse":[ ["Ares", "Daughter"], ["Luke", "Former friend"] ],
    "Tyson":[  ["Annabeth", "Friend"]],
    "Kronos":[["Percy", "Arch nemesis"], ["Ares", "Tricked to plan war"] ],
    "Nico":[  ["Annabeth", "acquaintance"], ["Luke", "Enemy"]  ],
    "Ares":[    ],
    "Apollo":[ ["Percy", "Friend"], ["Grover", "Ally"] ],
    "Dionysus":[["Percy", "Enjoys mocking"] ],
    "Thalia":[ ["Zeus","Daughter"], ["Percy", "Friendly rival"] ],
    "Rachel":[  ["Annabeth", "Friend"]]  
}


def begin_graph():
	for i in range(len(characters)):
	    graph.add_node(characters[i])
	    curr_node = graph.nodes()[i]
	    curr_node.set_size(sizes[i]) # will change back to sizes[i] or rescale completely
	    curr_node.set_value_style(40,Color.WHITE,Color.BLACK)
	    curr_node.set_color(alliance[i]) 
	    curr_node.set_position(positions[i][0], positions[i][1]) # May leave out locations entirely 
                     
	for s in range(len(characters)):
		for t in range(len(relations[characters[s]])):
			curr_edge = graph.add_edge(characters[s], relations[characters[s]][t][0], relations[characters[s]][t][1], True)
			curr_edge.set_weight_style(40)
			curr_edge.set_width(5) 




begin_pynode(begin_graph)

