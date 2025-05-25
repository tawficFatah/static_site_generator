import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_result = "<p>This is a paragraph of text.</p>"

        #Debugging
        #print(node)
        
        self.assertEqual(node.to_html(), expected_result)
        
    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_result = "<a href=\"https://www.google.com\">Click me!</a>"

        #Debugging
        #print(node)

        self.assertEqual(node.to_html(), expected_result)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected_result = "<p>Hello, world!</p>"

        #Debugging
        #print(node)
        self.assertEqual(node.to_html(), expected_result)
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")

        #Debugging
        #print(node)
        self.assertEqual(node.to_html(), "Hello, world!")    
        
if __name__ == "__main__":
    unittest.main()