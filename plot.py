import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl


def ploting_function(graph):
    seed = 13648  # Seed random number generators for reproducibility
    pos = nx.spring_layout(graph, seed=seed)

    node_sizes = [1 + 2 * i for i in range(len(graph))]
    M = graph.number_of_edges()
    edge_colors = range(2, M + 2)
    edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
    cmap = plt.cm.plasma

    nodes = nx.draw_networkx_nodes(graph, pos, node_size=node_sizes, node_color="indigo")
    edges = nx.draw_networkx_edges(
         graph,
         pos,
         node_size=node_sizes,
         arrowstyle="->",
         arrowsize=10,
         edge_color=edge_colors,
         edge_cmap=cmap,
         width=2,
         arrows=True
    )
    # set alpha value for each edge
    for i in range(M):
         edges[i].set_alpha(edge_alphas[i])

    pc = mpl.collections.PatchCollection(edges, cmap=cmap)
    pc.set_array(edge_colors)

    ax = plt.gca()
    ax.set_axis_off()
    plt.colorbar(pc, ax=ax)
    plt.show()