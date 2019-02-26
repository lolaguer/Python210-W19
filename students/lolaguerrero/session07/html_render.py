#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out):
        file_out.write(self.text)


class Element(object):

    tag = "html"

    def __init__(self, content=''):
        self.content = [content]

    def append(self, new_content):
        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for c in self.content:
            try:
                c.render(out_file)
            except AttributeError:
                out_file.write(c)
        out_file.write("</{}>\n".format(self.tag))



class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag)+'PythonClass - Session 6 example'+"</{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = "title"
