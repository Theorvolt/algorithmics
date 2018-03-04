from pynode.main import *
import queue
s = begin_pynode()
#Chapter 1 Visual Summary


# ADT purposes
# ADT's are a way of representing information.
# They are useful for modelling real life problems.
# This proccedure is called abstractation where unecessary information is removed.
# It creates a general model that works for variants of that problem.
# An example of this is a train network map in which the size and location are not to scaled, it represents a basic graph of locations.
# If a certain part of a problem can be replicated and is used often, it can be put into a function and this is called modularisation.

# Graph Theory
def g_t(x):
	graph.clear()
	graph.add_node(0)
	print("This is a node, or a vertex")
	graph.add_node(1)
	pause(x)
	graph.add_edge(graph.nodes()[0], graph.nodes()[1])
	print("This is two nodes connected by an edge")
	print("These two nodes each have a degree one.")
	pause(x)
	
	graph.clear()
	pause(x)
	graph.add_node(0)
	graph.add_node(1)
	graph.add_node(2)
	graph.add_edge(graph.nodes()[0],graph.nodes()[1])
	graph.add_edge(graph.nodes()[0],graph.nodes()[2])
	print("node 0 has a degree of 2")
	pause(x)
	print("each outgoing edge a node has indicates it degree.")
	print("A graph is a collection of nodes and edges.")
	
	graph.clear()
	pause(x)
	graph.add_node(0)
	graph.add_node(1)
	graph.add_node(2)
	graph.add_edge(graph.nodes()[0],graph.nodes()[1])
	graph.add_edge(graph.nodes()[0],graph.nodes()[2])
	graph.add_edge(graph.nodes()[1],graph.nodes()[2])
	print("This is a connected graph. It is possible to access all nodes by traversing edges.")
	pause(x)

	graph.clear()
	graph.add_node(0)
	graph.add_node(1)
	graph.add_edge(graph.nodes()[0],graph.nodes()[1],weight=4.2)
	print("the number on the edge indicates an edges weight. This can indicate the strength or cost of a connection.")
	pause(x)

	graph.clear()
	pause(x)
	graph.add_node(0)
	graph.add_node(1)
	graph.add_node(2)
	graph.add_edge(graph.nodes()[0],graph.nodes()[1])
	graph.add_edge(graph.nodes()[0],graph.nodes()[2])
	graph.add_edge(graph.nodes()[1],graph.nodes()[2])
	print("This graph contains a circuit. This is because there are more than one edges that connect two nodes.")
	pause(x)

	graph.clear()
	pause(x)
	graph.add_node(0)
	graph.add_node(1)
	graph.add_node(2)
	graph.add_node(3)
	graph.add_edge(graph.nodes()[0],graph.nodes()[1])
	graph.add_edge(graph.nodes()[0],graph.nodes()[2])
	graph.add_edge(graph.nodes()[0],graph.nodes()[3])
	print("this is a tree. A tree does not contain any circuits and connects all nodes.")

	graph.clear()
	pause(x)
	graph.add_node(0)
	graph.add_node(1)
	graph.add_node(2)
	graph.add_node(3)
	graph.add_node(4)
	graph.add_node(5)
	graph.add_node(6)
	graph.add_edge(graph.nodes()[0],graph.nodes()[1])
	graph.add_edge(graph.nodes()[0],graph.nodes()[2])
	graph.add_edge(graph.nodes()[0],graph.nodes()[3])
	graph.add_edge(graph.nodes()[1],graph.nodes()[4])
	graph.add_edge(graph.nodes()[1],graph.nodes()[5])
	graph.add_edge(graph.nodes()[1],graph.nodes()[6])
	print("A forest is a collection of trees.")
	print("By connecting one node to two trees, you make a bigger tree.")
	print("It is a tree as trees are defined as having n-1 edges where n = number of nodes.")
	print("i.e a tree with 5 nodes and 4 edges and a tree with 6 nodes and 5 edges join to make a tree with 11 nodes and 10 edges.")
	pause(x)

	graph.clear()
	print("the width of a map refers to the minimum distance required to ensure you can travel from any node to any other node.")
	print("This goes for all pairs of nodes in the graph and minimum means there cannot be pointless loops.")
	print("The highest of these distances is refered to as the width.")
	print("If there is no weighting, then its the number of edges. Otherwise edges are factored in.")

	print("A minimal spanning tree is a tree of a connected graph that connects all nodes in the shortest distance possible.")


def b_k(x):
	print("A graph with a circuit that can be traversed with no edge being landed on twice is an Eulerian circuit.")
	print("In response to a problem, Euler deduced that there was no solution.")
	print("In order for a Eulerian path to exist, there must be either 0 or 2 odd degree nodes.")
	print("This is because only the start and end can be odd. This is because in order to traverse an edge, you must enter and exist (only even degree).")
	print("Graphs can be represented as a matrix like so:")
	a = [[0,1,2],[1,2,0],[2,0,0]]
	print(a)
	print("The entries signify how much steps are required to get from one node to another.")
	print("By raising the matrix to the nth power, you can determine how many ways you can travel from node a to node b.")

def adt_spec(x):
	pass

