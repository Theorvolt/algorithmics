
# This code is to be run with the offline rendition of pynode
# To make this work with the online version, comment out the pynode.main import and begin_pynode(begin() and uncomment begin()
# Essentially reuses Alex Sochas code by utlising a queue but with different constraints for trolls and fairies
from pynode.main import *
import queue
import random

def begin():
        seen = [False] * 128 # Sets a seen flag to prevent dupe node adding
        # There are 2^7 possibilities as binary can be 0 or 1 and with seven elemeents, you have 2^7 possibilites
        
        bfs_queue = queue.Queue()

        # Create the next situation by adding a new node and/or edge
        def next_situation(node, data):
            binary_id = int (''.join(map(str, data)),2) # Conversion to base 10 actually has merit in that you can easily flag that respective element of a list
            new_node = None
    
            # Add a new node, or connect to an existing one
            if seen[binary_id]:
                if not graph.adjacent(node, binary_id):
                    graph.add_edge(node, binary_id, directed=True) # Essentially adds another connection via that node
            else:
                new_node = graph.add_node(binary_id, "".join(map(str, data))).set_attribute("data", data) # Adds the node and flags it as seen
                graph.add_edge(node, new_node, directed=True)
                seen[binary_id] = True
                return new_node

        start = graph.add_node(0, "0000000").set_attribute("data", [0, 0, 0, 0, 0, 0, 0]) 
        end = None
        seen[0] = True
        bfs_queue.put(start)
        # This puts the first situation through the queue

        # This queue will be filled after each time a node is completed until all valid solutions are exhausted
        while not bfs_queue.empty():
                node = bfs_queue.get()
                node.set_color(Color.RED)
                node.highlight()
                data = node.attribute("data")

                # Fills the end node if found
                if data == [1, 1, 1, 1, 1, 1, 1]:
                        end = node

                # Begins first round of validity checks, starts by defining both sides of the boat
                boat_side = data[6]
                new_boat_side = (data[6] + 1) % 2

                # Simply checks if the troll elements match the boat element and add accordingly to the resepective side
                curr_trolls = (1 if data[0] == data[6] else 0) + (1 if data[1] == data[6] else 0) + (1 if data[2] == data[6] else 0) 
                curr_other = 3 - curr_trolls

                # Checks if all goats are on the same side as their troll and if not, check again to see if there are trolls on the goat's side and set validity to False if so
                for i in range(0,3):
                        if data[i+3] == boat_side and data[i] != data[i+3]:
                                if curr_other > 0:
                                        valid = False
                for i in range(0,3):
                        if data[i+3] == new_boat_side and data[i] != data[i+3]:
                                if curr_trolls > 0:
                                        valid = False

                # Generates all the possible movements between 2 people
                for p1 in range(6):
                        for p2 in range(6):
                                # check if person 1 and person 2 are on the boat side and if they are, reset the loop
                                # Since that situation has already been retrieved by the queue, it goes over a new situation
                                
                                if data[p1] != boat_side or data[p2] != boat_side:
                                        continue

                                # Assigns the new scenario to a list
                                new_data = list(data)
                                new_data[6] = new_boat_side
                                new_data[p1] = new_boat_side
                                new_data[p2] = new_boat_side
                                valid = True

                                # Performs a second validity check to see if the situation is valid like the other checker and set flag valid to False if so
                                number_trolls = (1 if new_data[0] == new_data[6] else 0) + (1 if new_data[1] == new_data[6] else 0) + (1 if new_data[2] == new_data[6] else 0) 
                                other_trolls = 3 - number_trolls

                                for i in range(0,3):
                                        if new_data[i+3] == new_boat_side and new_data[i] != new_data[i+3]:
                                                if number_trolls > 0:
                                                        valid = False
                                for i in range(0,3):
                                        if new_data[i+3] == boat_side and new_data[i] != new_data[i+3]:
                                                if other_trolls > 0:
                                                        valid = False
                                # Removes any invalid scenarios
                                if valid == False:
                                        continue
                                # Puts the data and the node through the situation handler to either add a new node and/or a new conenction
                                new_node = next_situation(node,new_data)
                                if new_node != None:
                                        bfs_queue.put(new_node) # Continues feeding scenarios to the queuue untill all valid solutions are exhausted


        # Reset node color
        for node in graph.nodes():
            node.set_color(Color.DARK_GREY)

        # Color start and end
        start.set_color(Color.GREEN)
        end.set_color(Color.GREEN)
        
        # Randomly choose path
        path = []
        node = end
        while node is not start:
            edge = node.incoming_edges()[random.randint(0, len(node.incoming_edges()) - 1)]
            path.append(edge)
            node = edge.source()

        # Traverse the path
        for edge in reversed(path):
            edge.traverse(color=Color.GREEN)


begin_pynode(begin)
# begin()
