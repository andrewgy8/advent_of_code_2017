import re
import networkx as nx


def get_file_and_format():
    with open('day_12/input.txt') as f:
        return f.read()


def strip_comma(s):
    s = re.sub(',', '', s)
    for stri in s:
        if ',' in stri:
            return stri.pop(',')
    return s


class TravelingSalesman:

    relationships = {}
    con_to_zero = 0
    connections = []
    parent_checking = []

    def __init__(self, i):
        self.lines = [strip_comma(s) for s in i.splitlines()]

    def parse(self):
        for line in self.lines:
            l = line.split(' ')
            person = int(l[0])

            if len(l) > 3:
                connections = [int(n) for n in l[2:-1]]
            else:
                connections = [int(l[2])]

            self.relationships[person] = connections

    def check_zero_connections(self, p):
        c = self.relationships[p]
        # print('checking ', p, c)

        if p == 0 or 0 in c:
            self.parent_checking.append(p)
            return [p]
        elif len(c) > 0:
            self.parent_checking.append(p)
            return self.go_through_conn(p)

    def cycle_through_relationships(self):
        for p, c in self.relationships.items():
            self.parent_checking.clear()

            connection_existent = self.check_zero_connections(p)
            self.connections += connection_existent
        return len(self.connections)

    def go_through_conn(self, person):
        conns = self.relationships[person]
        connections = []
        for c in conns:
            pre_checked = c in self.parent_checking
            if person != c and not pre_checked:
                connection_existent = self.check_zero_connections(c)

                if connection_existent:
                    print(c)
                    connections.append(c)
        return connections


class NetworkSalesman:
    # Create a graph of programs
    graph = nx.Graph()

    def create(self):
        i = get_file_and_format()
        inputs = [strip_comma(s) for s in i.splitlines()]
        for line in inputs:
            # Parse the line
            node, neighbors = line.split(' <-> ')
            print(node, neighbors)
            # Add edges defined by this line
            self.graph.add_edges_from((node, neighbor) for neighbor in neighbors.split(' '))


if __name__ == '__main__':
    network = NetworkSalesman()
    network.create()
    print('Part 1:', len(nx.node_connected_component(network.graph, '0')))
    print('Part 2:', nx.number_connected_components(network.graph))
    # i = get_file_and_format()
    # t = TravelingSalesman(i)
    # t.parse()
    #
    # try:
    #     res = t.cycle_through_relationships()
    #     print('connections to zero: ', res)
    # except Exception as e:
    #     print(e)

