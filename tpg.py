import pprint
from collections import defaultdict


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

class TPG:
    def __init__(self, world):

        self.dim_x = world.width
        self.dim_y = world.height
        self.agents = world.agents
        self.obstacles = {}
        self.other_agent_paths = []
        self.tpg = Graph()
    
    def createType1Edges (self):
        for id, agent in self.agents.items(): #starts at 1
            v = agent.path[0]
            for t, loc in agent.path.items():
                if t != 0:
                    if agent.path[t] != agent.path[t-1]:
                        self.tpg.add_edge((v, id, t-1), (loc,id, t), 1)
                        v = loc
    
    def createType2Edges (self):
        for id, agent in self.agents.items():
            for t, loc in agent.path.items():
                if (loc, id, t) in self.tpg.get_vertices():
                    for id_, agent_ in self.agents.items():
                        if id != id_:
                            for tk in range(t+1, len(agent.path.items())):
                                if (agent_.path[tk], id_, tk) in self.tpg.get_vertices() and agent_.path[tk] == agent.path[t]:
                                    self.tpg.add_edge((agent_.path[tk], id_, tk), (agent.path[t], id, t), 1)
                

#testing the graph data structure
connections = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
g = Graph()
g.add_vertex((30,1, 1, 0)) #pos_x, pos_y, agent_id, inst_tempo_path
g.add_vertex((30,2, 1, 0))

g.add_edge((30,1,1, 0), (30,2,1, 0), 4)
g.add_edge((30,1,2, 0), (30,2,2,0), 2) #para trocar o peso, criar novamente a aresta com novo peso

for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print ( str(vid), str(wid), v.get_weight(w))


print((30,1,1,0) in g.get_vertices()) #print True


