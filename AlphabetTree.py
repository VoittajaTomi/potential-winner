import ipdb


class AlphabetTree:
    def __init__(self, letter):
        if not letter or not ('A' <= letter <= 'Z'):
            raise ValueError
        self.letter = letter
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def height(self):
        if not self.nodes:
            return 1
        else:
            return 1 + max(node.height() for node in self.nodes)

    def traverse(self, nodes_list):
        the_list = []
        for item in list(nodes_list):
            if isinstance(item, list):
                for x in self.traverse(item):
                    the_list.append(x.get_char())
            else:
                the_list.append(item.get_char())
        return the_list
    def to_list(self):
        return list(self.traverse(self.nodes))

    def compare(self, another_tree):
        list_chars = []
        another_list = []
        #ipdb.set_trace()
        another_list.append(another_tree)
        list_chars.append(self.to_list(self.nodes))
        list_chars.append(self.to_list(another_list))

        return make_unique_set(list_chars)







    def get_set(self):
        return set(self.nodes)

    def get_char(self):
        return self.letter

    def __repr__(self):
        return f"AlphabetTree({self.letter}): {self.nodes}"
