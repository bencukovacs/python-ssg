import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        node = ParentNode(None, [], None)
        self.assertRaisesRegex(ValueError, ".*a tag", node.to_html)
        
    def test_no_children(self):
        node = ParentNode("div", [], None)
        self.assertRaisesRegex(ValueError, ".* children", node.to_html)
        
    def test_to_html_oneleaf(self):
        leafnode = LeafNode("LeafNode", None, None)
        node = ParentNode("div", [leafnode], None)
        text = node.to_html()
        self.assertEqual(text, "<div>LeafNode</div>")
    
    def test_to_html_nestedparent(self):
        leafnode = LeafNode("LeafNode", None, None)
        node = ParentNode("div", [leafnode], None)
        node2 = ParentNode("div", [node], None)
        text = node2.to_html()
        self.assertEqual(text, "<div><div>LeafNode</div></div>")

    def test_to_html_complex(self):
        leafnode = LeafNode("LeafNode", "p", None)
        leafnode2 = LeafNode("LeafNode2", "p", None)
        node = ParentNode("div", [leafnode], None)
        node2 = ParentNode("html", [node, leafnode2], None)
        text = node2.to_html()
        self.assertEqual(text, "<html><div><p>LeafNode</p></div><p>LeafNode2</p></html>")
    
    def test_to_html_multiple_children(self):
        leafnode1 = LeafNode("LeafNode1", None, None)
        leafnode2 = LeafNode("LeafNode2", None, None)
        node = ParentNode("div", [leafnode1, leafnode2], None)
        text = node.to_html()
        self.assertEqual(text, "<div>LeafNode1LeafNode2</div>")

    def test_to_html_with_attributes(self):
        leafnode = LeafNode("LeafNode", None, None)
        node = ParentNode("div", [leafnode], {"class": "container"})
        text = node.to_html()
        self.assertEqual(text, '<div class="container">LeafNode</div>')

    def test_to_html_nested_with_attributes(self):
        leafnode = LeafNode("LeafNode", None, None)
        node = ParentNode("div", [leafnode], {"class": "inner"})
        node2 = ParentNode("div", [node], {"class": "outer"})
        text = node2.to_html()
        self.assertEqual(text, '<div class="outer"><div class="inner">LeafNode</div></div>')

    def test_to_html_empty_parent(self):
        node = ParentNode("div", [], None)
        self.assertRaisesRegex(ValueError, ".* children", node.to_html)
          
if __name__ == "__main__":
    unittest.main()