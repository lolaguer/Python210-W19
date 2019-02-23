#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None):
        self.content = content

    def append(self, new_content):
        self.content = self.content +'.\n' + new_content + '.\n'

    def render(self, out_file):
        tag_name = {'tn' : self.tag}
        out_file.write("<{}> \n".format(self.tag) + self.content + " </{}>".format(self.tag))



class Html(Element):

    tag = "html"

    def __init__(self, content=None):
        self.content = content


class Body(Element):

    tag = "body"

    def __init__(self, content=None):
        self.content = content


class Paragraph(Element):

    tag = "p"

    def __init__(self, content=None):
        self.content = content

