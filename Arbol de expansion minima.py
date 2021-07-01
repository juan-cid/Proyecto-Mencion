#!/usr/bin/python3
# -*- coding: utf-8 -*-
import networkx as nx
import random
import matplotlib.pyplot as plt


def Muestra_grafo(G, pos):
    labels = nx.get_edge_attributes(G, 'weight')
    # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=300)
    # edges
    nx.draw_networkx_edges(G, pos, width=2)
    # labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
    plt.show()

G = nx.Graph() #Se crea el grafo

#Diccionario con todas las conexiones y sus respectivas distancias
dic = [(1,2, 23.2),(1,4, 22.3),(1,9, 27.3),
       (2,1, 23.2),(2,4, 23.3),(2,7, 11.6),(2,9, 31.9),(2,16, 13.6),
       (3,4, 20.7),(3,6, 32.2),(3,9, 5.9),(3,10, 5.5),(3,11, 17.3),
       (4,1, 22.3),(4,2, 23.3),(4,3, 20.7),(4,7, 11.8),(4,8, 8.2),(4,11, 12.7),
       (5,7, 8.1),(5,8, 7.8),(5,11, 16.3),(5,17, 22.6),(5,18, 30.8),
       (6,3, 32.2),(6,9, 27.4),(6,10, 35.3),(6,12, 40.7),
       (7,2, 11.6),(7,4, 11.8),(7,5, 8.1),(7,8, 4.6),(7,16, 25.1),
       (8,4, 8.2),(8,5, 7.8),(8,7, 4.6),(8,11, 11.7),
       (9,1, 27.3),(9,2, 31.9),(9,3, 5.9),(9,6, 27.4),
       (10,3, 5.1),(10,6, 35.3),(10,11, 18.1),(10,12, 15.6),
       (11,3, 17.3),(11,4, 12.7),(11,8, 11.5),(11,10, 18.2),(11,13, 27.0),(11,15, 18.5),
       (12,6, 40.7),(12,10, 15.6),(12,13, 15.4),(12,14, 22.4),
       (13,11, 27.0),(13,12, 15.4),(13,14, 13.4),(13,15, 25.4),(13,20, 25.4),
       (14,12, 22.4),(14,13, 13.4),
       (15,11, 18.5),(15,13, 25.4),(15,17, 18.2),(15,19, 10.7),(15,20, 7.1),
       (16,2, 13.6),(16,7, 23.0),(16,18, 12.1),
       (17,5, 22.6),(17,18, 32.0),(17,15, 18.2),
       (18,5, 30.8),(18,16, 13.4),(18,17, 31.2),
       (19,15, 10.8),(19,20, 14.4),
       (20,13, 35.9),(20,15, 7.9),(20,19, 14.4)
       ]

print(dic)

capacidades = []
for u,v,w in dic:
    G.add_edge(str(u),str(v), weight=w)
    capacidades.append(1)

pos = nx.spring_layout(G)

# dibujo el grafo
Muestra_grafo(G, pos)

#Resuelve por método de Spanning tree
T = nx.minimum_spanning_tree(G)
Muestra_grafo(T, pos)
print(sorted(T.edges(data=True)))
