import networkx as nx
import plotly.graph_objs as go
from plotly.offline import plot

def read_anonymized_gml(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    graph = nx.Graph()
    i = 0
    while i < len(lines):
        if lines[i].startswith('node'):
            node_id = tuple(map(int, lines[i+1].strip().split()[0].strip('()').split(',')))
            graph.add_node(node_id)
        elif lines[i].startswith('edge'):
            source_id = tuple(map(int, lines[i+1].strip().split()[1].strip('()').split(',')))
            target_id = tuple(map(int, lines[i+2].strip().split()[1].strip('()').split(',')))
            graph.add_edge(source_id, target_id)
        i += 1
    return graph

def plot_anonymized_graph(graph):
    pos = nx.kamada_kawai_layout(graph)
    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5,color='#888'),
        hoverinfo='none',
        mode='lines')
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    for node in graph.nodes():
        x, y = pos[node]
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Anonymized Graph',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    plot(fig, filename='anonymized_graph.html')