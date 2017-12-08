import re
import collections
import networkx as nx

def get_file_and_format():
    with open('day_7/input.txt') as f:
        return [strip_comma(s) for s in f.read().splitlines()]

def strip_comma(s):
    s = re.sub(',', '', s)
    for stri in s:
        if ',' in stri:
            return stri.pop(',')
    return s


class Network:
    rows = []
    graph = nx.DiGraph()

    def __init__(self):
        self.parse()

    def parse(self):
        arr = get_file_and_format()
        for line in arr:
            l = line.split(' ')
            i = l[0]
            weight = l[1]
            length = len(l)
            n = dict()
            n['self'] = i
            n['weight'] = weight.strip('()')

            if length > 2:
                children = l[3:length]
                n['children'] = children

            self.rows.append(n)

    def build_tree(self):
        for line in self.rows:
            name = line.get('self')
            weight = line.get('weight', None)
            if weight:
                weight = int(weight)
            self.graph.add_node(name, weight=weight)
            children = line.get('children', None)
            if children:
                for child in children:
                    self.graph.add_edge(name, child)

        ordered = list(nx.topological_sort(self.graph))

        print('PART 1:', ordered[0])

        weights = {}

        # Going backwards (starting from the leaves)
        for node in reversed(ordered):
            # Start with this nodes own weight
            total = self.graph.nodes[node]['weight']

            counts = collections.Counter(weights[child] for child in self.graph[node])
            unbalanced = None

            for child in self.graph[node]:
                # If this child's weight is different than others, we've found it
                if len(counts) > 1 and counts[weights[child]] == 1:
                    unbalanced = child
                    break

                # Otherwise add to the total weight
                val = weights[child]
                total += weights[child]

            if unbalanced:
                # Find the weight adjustment and the new weight of this node
                diff = weights[unbalanced] - val
                print('PART 2:', self.graph.nodes[unbalanced]['weight'] - diff)
                break

            # Store the total weight of the node
            weights[node] = total


# Build the graph of programs


# Topological sort to find the root of the tree


# Keep track of each node's total weight (itself + its children)
