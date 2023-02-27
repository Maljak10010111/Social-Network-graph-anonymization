import time
import matplotlib.pyplot as plt
import dividing_nodes
import numpy as np
import anonymization_of_graph
import networkx as net

import main

"""
evaluation:
    select graph
    how much time algorithm takes to execute (plot the time in function of the parameters)
    change parameters (k or m) and see how the algorithm performs if you vary the parameters
    """


def evaluate_division(V, E):
    varying_parameters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    times = []

    for param in varying_parameters:
        start_time = time.time()
        #my_method(param)
        dividing_nodes.divide_nodes(V, param, E)
        # substitution function
        end_time = time.time()
        execution_time = end_time - start_time
        times.append(execution_time)

    plt.plot(varying_parameters, times)
    plt.xlabel('Parameter value')
    plt.ylabel('Execution time (s)')
    plt.title('Execution time VS Parameter value')
    plt.show()

# function to see the difference of applying divide_nodes on graph of different sizes


def evaluate_division_nodes_different_graphs(nodes, edges):
    m = 5
    times = []
    start_time = time.time()
    dividing_nodes.divide_nodes(nodes, m, edges)
    end_time = time.time()
    execution_time = end_time - start_time
    times.append(execution_time)
    num_nodes = len(nodes)
    plt.hist(num_nodes, bins=10, weights=times)
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution time VS Number of nodes')
    plt.show()

