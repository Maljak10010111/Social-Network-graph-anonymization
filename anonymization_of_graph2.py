
def change_also_labels(graph,mapping):
    with open("igor7.gml", "w") as f:
        f.write("graph [\n")

        for node in graph.nodes():
            f.write("  node [\n")
            f.write("    id {}\n".format(mapping[node]))
            f.write("    label {}\n".format(node))
            f.write("  ]\n")

        for edge in graph.edges():
            f.write("  edge [\n")
            f.write("    source {}\n".format(mapping[edge[0]]))
            f.write("    target {}\n".format(mapping[edge[1]]))
            f.write("  ]\n")

            f.write("]\n")