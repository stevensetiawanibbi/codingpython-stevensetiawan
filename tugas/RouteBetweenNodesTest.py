#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        visited = []
        queue = []
        path = []
        queue.append(startNode)
        while queue:
            deVertex = queue.pop(0)
            path.append(deVertex)
            if deVertex == endNode:
                break
            if deVertex not in visited:
                visited.append(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    queue.append(adjacentVertex)
        return path


# In[7]:


customDict = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f"],
    "d": [],
    "e": ["f"],
    "f": ["j"],
    "j": []
}


# In[8]:


g = Graph(customDict)


# In[9]:


print(g.checkRoute("a", "j"))


# In[ ]:




