from AlphabetTree import AlphabetTree
import unittest,ipdb

class Testing(unittest.TestCase):

    def test_0_test_height_1(self):
        tree = AlphabetTree('A')
        self.assertTrue(tree.height() == 1)

    def test_1_test_letter1(self):
        tree = None
        try:
            tree = AlphabetTree('@')
        except ValueError:
            pass
        self.assertIsNone(tree)

    def test_2_union1(self):
        tree1 = AlphabetTree('A')
        tree1.add_node(AlphabetTree('B'))
        tree1.add_node(AlphabetTree('C'))
        tree2 = AlphabetTree('X')
        tree2.add_node(AlphabetTree('Y'))
        tree2.add_node(AlphabetTree('Z'))
        ipdb.set_trace()

        self.assertTrue(len(tree1.compare(tree2)) == 6)


