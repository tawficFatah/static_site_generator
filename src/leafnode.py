from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        
        props_str = self.props_to_html()
        html_str = f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
        return html_str
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"