import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node1 = TextNode("testing", TextType.NORMAL, url= "https://www.google.com")
        node2 = TextNode("testing", TextType.NORMAL, url= "https://www.google.com")
        node3 = TextNode("testing", TextType.NORMAL, url= "https://www.google.com")
        node4 = TextNode("testing", TextType.NORMAL, url= "https://www.google.com")
        self.assertEqual(node1, node2)
        self.assertEqual(node2, node4)
        self.assertEqual(node1, node4)
        self.assertEqual(node3, node4)
if __name__ == "__main__":
    unittest.main()