class HTMLNode():
    def __init__(self, tag= None, value= None, children= None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode(tag= {self.tag}, value= {self.value}, children= {self.children}, props= {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def props_to_html(self):
        return super().props_to_html()
    
    def to_html(self):
        if not self.value:
            raise ValueError("Missing value")
        elif not self.tag:
            return f"{self.value}"
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):

    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def props_to_html(self):
        return super().props_to_html()

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        elif not self.children:
            raise ValueError("Missing children")
        else:
            all_children_html = ''
            for node in self.children:
                all_children_html += node.to_html()
            return f'<{self.tag}{self.props_to_html()}>{all_children_html}</{self.tag}>'
        
 