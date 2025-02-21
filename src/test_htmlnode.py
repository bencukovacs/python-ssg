import unittest
import htmlnode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = htmlnode.HTMLNode("div", "This is a div node")
        node2 = htmlnode.HTMLNode("div", "This is a div node")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = htmlnode.HTMLNode("div", "This is a div node")
        node2 = htmlnode.HTMLNode("span", "This is a span node")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = htmlnode.HTMLNode("div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), 'class="container" id="main"')

    def test_props_to_html_empty(self):
        node = htmlnode.HTMLNode("div")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = htmlnode.HTMLNode("div", "This is a div node", ["child1", "child2"], {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(div, This is a div node, ['child1', 'child2'], {'class': 'container'})")

if __name__ == '__main__':
    unittest.main()