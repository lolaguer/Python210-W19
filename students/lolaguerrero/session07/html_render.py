#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag_name = "html"

    def __init__(self, content=None):
        self.content = content

    def append(self, new_content):
        self.content = self.content +'.\n' + new_content + '.\n'

    def render(self, out_file):
        out_file.write("<html> \n" + self.content + " </html>")
