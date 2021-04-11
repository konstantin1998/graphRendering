import xml.dom.minidom


def parse(graph_file):
    doc = xml.dom.minidom.parse(graph_file)
    edges = doc.getElementsByTagName('edge')
    return list(map(lambda edge: {'source': edge.getAttribute("source"), 'target': edge.getAttribute('target')}, edges))


if __name__ == "__main__":
  edges = parse("graph.graphml")
  print(edges)