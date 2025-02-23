import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_novalueerror(self):
        node = LeafNode(None, None, None)
        self.assertRaises(ValueError, node.to_html)
        
    def test_to_html_notag(self):
        value = "Leaf without tag"
        node = LeafNode(value, None, None)
        to_html_value = node.to_html()
        self.assertEqual(value, to_html_value, f"Value: {value} | to_html(): {to_html_value}")
        
    def test_to_html_withtag(self):
        value = "Leaf with p tag"
        tag = "p"
        expected = f"<{tag}>{value}</{tag}>"
        node = LeafNode(value, tag, None)
        to_html_value = node.to_html()
        self.assertEqual(expected, to_html_value)
    
if __name__ == "__main__":
    unittest.main()