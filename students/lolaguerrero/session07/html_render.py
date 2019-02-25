#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=''):
        self.content = [content]

    def append(self, new_content):
        print('content', self.content)
        print('new content this is the class',  new_content)
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for c in self.content:
            if type(c) == str:
                out_file.write(c + '\n')
            else:
                out_file.write("<{}>\n".format(c.tag))
                out_file.write(' '.join(c.content) + '\n')
                out_file.write("</{}>\n".format(c.tag))

        out_file.write("</{}>\n".format(self.tag))



class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"


