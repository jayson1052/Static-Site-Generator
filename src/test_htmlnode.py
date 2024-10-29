import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html1 = HTMLNode()
        html1.tag = "h1"
        html1.props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }

        html2 = HTMLNode(tag= "p", value= "Test", children= None)
        html2.props = {
            "href": "https://www.facebook.com", 
            "target": "_blank",
        }

        html3 = HTMLNode(tag= "p", value= "Test", children= None, props = None)
        
        self.assertEqual(html1.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(html2.props_to_html(), ' href="https://www.facebook.com" target="_blank"')
        self.assertEqual(html3.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leafnode1 = LeafNode(tag="p", value="This is a paragraph of text.")
        leafnode2 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        
        self.assertEqual(leafnode1.to_html(), '<p>This is a paragraph of text.</p>')
        self.assertEqual(leafnode2.to_html(), '<a href="https://www.google.com">Click me!</a>')


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

        node1 = ParentNode(
    "div",
    [
        LeafNode(None, "Some text without a tag"),
        LeafNode("em", "Emphasized text"),
    ],
)
        self.assertEqual(node1.to_html(), '<div>Some text without a tag<em>Emphasized text</em></div>')

        node2 = ParentNode(
    "span",
    []
)
        with self.assertRaises(ValueError):
            node2.to_html()
            
        node3 = ParentNode(
    "section",
    [
        LeafNode("h1", "Title"),
        LeafNode("p", None),  # No text provided here
        LeafNode("strong", "Important text"),
    ],
)   
        with self.assertRaises(ValueError):
            node3.to_html()
if __name__ == "__main__":
    unittest.main()