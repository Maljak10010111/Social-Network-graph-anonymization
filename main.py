import networkx as net
import csv
import pyvis.network as py
import matplotlib.pyplot as plt
import anonym
import anonymization_of_graph
import anonymization_of_graph2
import dividing_nodes
import evaluation
import loading_edges
import plot
import numpy as np
import plot_anonym_graph

if __name__ == '__main__':

    graph = net.read_gml('dolphins.gml',label='id')
    reduced_graph = net.read_gml('dolphins_reduced.gml', label='id')

    # making the list of nodes, because I have to use sort function in dividing_nodes.py class
    nodes = list(graph.nodes)
    reduced_nodes = list(reduced_graph.nodes)

    # extraction of the arcs from gml file
    #net.write_edgelist(graph, 'edgeList3.csv',delimiter=',')

    csv_filename = 'edgeList3.csv'
    with open(csv_filename) as file:
        reader = csv.reader(file)
        lst = list(tuple(line) for line in reader)

    # reduced edges
    csv_filename = 'edgeList_reduced.csv'
    with open(csv_filename) as file:
        reader = csv.reader(file)
        lst_reduced = list(tuple(line) for line in reader)

    new_list = dividing_nodes.divide_nodes(nodes,3,lst)


    tuple_list_of_nodes = [tuple(elem) for elem in new_list]
    mapping = {node: lst for lst in tuple_list_of_nodes for node in lst}
    #print(mapping)


    # ploting of the original graph

    #plot.ploting_function(graph)


    # transformation of the id of nodes with the tuples!
    """
    graph2 = graph.copy()
    net.set_node_attributes(graph2, mapping, "tuples")
    for i in range(len(graph2.nodes)):
        node_tuple =  graph2.nodes[i]["tuples"]
        print(node_tuple)
    """

    #G = plot_anonym_graph.read_anonymized_gml('updated_graph.gml')
    #plot_anonym_graph.plot_anonymized_graph(G)

    # anonymization with original algorithm
    #anonymization_of_graph.anonymization(mapping)

    # anonymization with additional algorithm which deletes the labels(attributes) of the nodes!
    #anonymization_of_graph2.change_also_labels(graph,mapping)

    # statistics
    evaluation.evaluate_division(nodes,lst)
    evaluation.evaluate_division_nodes_different_graphs(nodes,lst)
    evaluation.evaluate_division_nodes_different_graphs()







