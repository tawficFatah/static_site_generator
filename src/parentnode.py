from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        
        html_str_start = f"<{self.tag}{self.props_to_html()}>"
        
        html_str_middle = ""
        for child in self.children:
            html_str_middle += child.to_html()
            
        html_str_end = f"</{self.tag}>"
        return f"{html_str_start}{html_str_middle}{html_str_end}"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"