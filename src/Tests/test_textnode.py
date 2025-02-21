import unittest

from Models.textnode import TextNode, TextType
        
class TestTextNode(unittest.TestCase):
        def test_eq(self):
            node = TextNode("This is a text node", TextType.BOLD)
            node2 = TextNode("This is a text node", TextType.BOLD)
            self.assertEqual(node, node2)
            
        def test_urlisnone(self):
            node = TextNode("URL is None", TextType.NORMAL)
            self.assertIsNone(node.url)
            
        def test_noteq(self):
            node = TextNode("This is a text node", TextType.BOLD)
            node2 = TextNode("This is a text node", TextType.NORMAL)
            self.assertNotEqual(node, node2)
            
        def test_repr(self):
            node = TextNode("This is a text node", TextType.ITALIC, "http://example.com")
            self.assertEqual(repr(node), "TextNode(This is a text node, italic, http://example.com)")
            
        def test_text_type(self):
            node = TextNode("This is a text node", TextType.CODE)
            self.assertEqual(node.text_type, TextType.CODE)
            
        def test_text(self):
            node = TextNode("This is a text node", TextType.LINK, "http://example.com")
            self.assertEqual(node.text, "This is a text node")
            
        def test_url(self):
            node = TextNode("This is a text node", TextType.IMAGE, "http://example.com/image.png")
            self.assertEqual(node.url, "http://example.com/image.png")
        
if __name__ == "__main__":
    unittest.main()