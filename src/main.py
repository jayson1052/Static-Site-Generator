from textnode import TextNode, TextType
def main():
    test = TextNode("Text test", TextType.ITALIC)
    print(test.__repr__())
main()