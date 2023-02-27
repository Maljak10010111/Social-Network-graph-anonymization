import re

def anonymization(node_mapping):


    with open('dolphins.gml', 'r') as f:
        gml_string = f.read()

    def replace_node_id(match):
        node_id = int(match.group(1))
        if node_id in node_mapping:
            return str(node_mapping[node_id])
        else:
            return match.group(0)

# Define a function to replace the edge source and target IDs with tuples based on the mapping
    def replace_edge_id(match):
        source_id = int(match.group(1))
        target_id = int(match.group(2))
        if source_id in node_mapping and target_id in node_mapping:
             source_tuple = node_mapping[source_id]
             target_tuple = node_mapping[target_id]
             return 'source ' + str(source_tuple) + '\n    target ' + str(target_tuple)
        else:
            return match.group(0)

    # Replace the node IDs in the GML string with tuples based on the mapping
    gml_string = re.sub(r'id\s+(\d+)', replace_node_id, gml_string)

    # Replace the edge source and target IDs in the GML string with tuples based on the mapping
    gml_string = re.sub(r'source\s+(\d+)\s*\n\s*target\s+(\d+)', replace_edge_id, gml_string)


    with open('martina.gml', 'w') as f:
         f.write(gml_string)