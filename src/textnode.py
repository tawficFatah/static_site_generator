from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT        = 'text'
    BOLD        = 'bold'
    ITALIC      = 'italic'
    CODE        = 'code'
    LINK        = 'link'
    IMAGE       = 'image'
    
class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return  self.text == other.text and \
                self.text_type.value == other.text_type.value and \
                self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError(f"{text_node.text_type} is invalid TextType")
    
    leafnode = None
    text_type = text_node.text_type
    
    if text_type == TextType.TEXT:
        leafnode = LeafNode(None, text_node.text)
    elif text_type == TextType.BOLD:
        leafnode = LeafNode("b", text_node.text)
    elif text_type == TextType.ITALIC:
        leafnode = LeafNode("i", text_node.text)
    elif text_type == TextType.CODE:
        leafnode = LeafNode("code", text_node.text)
    elif text_type == TextType.LINK:
        leafnode = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_type == TextType.IMAGE:
        leafnode = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    return leafnode