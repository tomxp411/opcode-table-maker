#
# HtmlTypes
#
# Classes for HTML/XML objects
#

import os

# an html element can contain other html elements
# or text elements. All items must implement
#   def get_markup(self, indent:int = 0) -> str:
class html_element(list):
    def __init__(self):
        self.name = ""
        self.attributes = {} # name,str
    
    def set_class(self, class_text:str):
        self["class"] = class_text

    def get_attributes(self) -> str:
        s = ""
        if len(self.attributes) == 0:
            return ""
        
        for k,v in self.attributes.items():
            s += " " + k + "=" + "'" + str(v) + "'"
        return s 
    
    # gets an <opening_tag> for an HTML object
    # attributes can be a str or dict 
    def get_tag_open(self) -> str:
        s = "<" + self.name
        s += self.get_attributes()
        s += ">"
        return s

    def get_tag_close(self) -> str:
        s = "</" + self.name + ">"
        return s

    # gets an <opening_tag> for an HTML object
    # attributes can be a str or dict 
    def get_tag_empty(self) -> str:
        s = "<" + self.name
        s += self.get_attributes()
        s += "/>"
        return s

    # returns the HTML markup of the entire object and its children
    # indent is the number of spaces to indent this object
    def get_markup(self, indent:int = 0) -> str:
        s = ""
        if indent > 0:
            s += " " * indent

        if len(self) == 0:
            s += self.get_tag_empty() + "\n"
        elif len(self) == 1 and isinstance(self[0], text_element):
            s += self.get_tag_open() \
                + self[0].text \
                + self.get_tag_close() \
                + "\n"
        else:
            s += self.get_tag_open() + "\n"
            for e in self:
                s += e.get_markup(indent + 2)
            if indent > 0:
                s += " " * indent
            s += self.get_tag_close() + "\n"

        return s

    def get_text(self) -> str:
        s = ""
        indent = 0
        if len(self) == 0:
            pass
        elif len(self) == 1 and isinstance(self[0], text_element):
            s += self[0].text
        else:
            for e in self:
                s += e.get_markup(indent + 2)
        return s

    @property
    def text(self):
        if len(self) == 0:
            return ""
        else:
            return self[0].get_text()
    
    @text.setter
    def text(self, value:str):
        self.clear()
        self.add_text(value)

    def attr(self, key:str, value:str=None):
        if value:
            self.attributes[key] = value
        if key in self.attributes:
            return self.attributes[key]

    def class_name(self, value=None):
        return self.attr("class",value)

    # add an html element
    def add(self, 
            name_or_element : str, 
            text:str=None, 
            css_class:str = None, 
            attributes:dict=None, 
            items:list=None):
        
        if isinstance(name_or_element, html_element):
            self.append(name_or_element)
            return name_or_element
        
        if name_or_element == None or len(name_or_element) == 0:
            raise Exception("add() HTML element: name is required")
        
        item = html_element()
        item.name = name_or_element
        self.append(item)
        
        if attributes:
            item.attributes = attributes
        if text:
            item.append(text_element(text))
        if items:
            item.extend(items)

        if css_class:
            item.attributes["class"] = css_class
        
        return item

    # add a text element
    def add_text(self, text:str):
        self.append(text_element(text))

    # add a text element
    def add_br(self, text:str = ""):
        self.add_text(text + "<br/>")

class text_element():
    def __init__(self, text:str = ""):
        self.text = text

    def get_markup(self, indent:int = 0):
        s = ""
        if indent > 0:
            s += " " * indent
        s += self.text
        s += "\n"
        return s

    def get_contents(self, indent:int = 0):
        return self.text

# an HTML document that can contain html_element objects.
# text must be contained inside of html_element objects.
class html_document(html_element):
    def __init__(self):
        super().__init__()
        self.name = "html"
        self.header = self.add("header")
        self.title = self.header.add("title")
        self.body = self.add("body")

    def set_title(self, text:str):
        self.title.clear()
        self.title.add_text(text)

class html_anchor(html_element):
    def __init__(self, href:str = "", text:str = ""):
        super().__init__()
        self.name = "a"
        self.href = href
        self.text = text

    @property
    def href(self):
        self.attr("href")
    
    @href.setter
    def href(self, value:str):
        self.attr("href", value)

    # def href(self, value=None):
    #     self.attr("href",value)

class html_style(html_element):
    def __init__(self):
        super().__init__()
        self.name = "style"
        self.styles = {}

    # add a style property to a style, creating the style if necesssary
    def add_style(self, name:str, attr_name:str, attr_val:str):
        if name in self.styles:
            slist = self.styles[name]
        else:
            slist = []
            self.styles[name] = slist
        s = attr_name + " : " + attr_val + ";"
        slist.append(s)
    
    def generate_markup(self):
        self.clear()
        for k,slist in self.styles.items():
            self.add_text(k + " {")
            for s in slist:
                self.add_text("  " + s)
            self.add_text("}")

    def get_markup(self, indent: int = 0) -> str:
        self.generate_markup()
        return super().get_markup(indent)
