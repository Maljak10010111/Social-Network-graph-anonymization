import re

def anonymization(node_mapping):
    with open('dolphins.gml', 'r') as f:
        gml_string = f.read()

    def replace_node_id(match):
        node_id = int(match.group(1))
        if node_id in node_mapping:
            return "(" + ",".join(str(i) for i in node_mapping[node_id]) + ")"
        else:
            return match.group(0)

    def replace_edge_id(match):
        source_id = int(match.group(1))
        target_id = int(match.group(2))
        if source_id in node_mapping and target_id in node_mapping:
            source_tuple = "(" + ",".join(str(i) for i in node_mapping[source_id]) + ")"
            target_tuple = "(" + ",".join(str(i) for i in node_mapping[target_id]) + ")"
            return 'source ' + source_tuple + '\n    target ' + target_tuple
        else:
            return match.group(0)

    gml_string = re.sub(r'id\s+(\d+)', replace_node_id, gml_string)
    gml_string = re.sub(r'source\s+(\d+)\s*\n\s*target\s+(\d+)', replace_edge_id, gml_string)

    with open('updated_graph11.gml', 'w') as f:
         f.write(gml_string)