class UnionFind:
    def __init__(self, vertices):
        self.ids = dict(zip(vertices, range(len(vertices))))

    def union(self, p, q):
        """connect two components, connect two vertices p and q"""
        value = self.ids[p]
        for i in self.ids.keys():
            if self.ids[i] == value:
                self.ids[i] = self.ids[q]

    def is_connected(self, p, q):
        """return true if p and q are connected, false otherwise"""
        return self.ids[p] == self.ids[q]


    def find(self, p):
        """return id number of vertex p"""
        return self.ids[p]

    def number_of_component(self):
        """return the number of connected components"""
        return len(set(self.ids.values()))
        
uf = UnionFind('abcdefg')
