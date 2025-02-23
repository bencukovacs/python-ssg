from textnode import TextNode, TextType


def main():
    text_node = TextNode("Hello, World!", TextType.NORMAL, None)
    print(f"Created TextNode: {text_node}")

main()