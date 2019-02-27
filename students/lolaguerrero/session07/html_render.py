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

    def __init__(self, content='', **kwargs):
        self.content = [content]
        self.attributes = ''.join([' %s = "%s"' %(key, value) for key, value in kwargs.items()])

    def append(self, new_content):
        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))

    def render(self, out_file):
        out_file.write("<{}{}>\n".format(self.tag, self.attributes))
        for c in self.content:
            try:
                c.render(out_file)
            except AttributeError:
                out_file.write(c)
        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = "html"

    def render(self, out_file):
        out_file.write("<!DOCTYPE html>\n")
        super(Html, self).render(out_file)  # calls 'Element.render()'


class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}{}>".format(self.tag, self.attributes)+self.content[0]+"</{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def render(self, out_file):
        out_file.write("<{} {} />\n".format(self.tag, self.attributes))

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(Element):
    tag = 'a'

    def __init__(self, link, content):
        self.link = link
        self.content = content

    def render(self, out_file):
        anchor_dict = {'tag':self.tag, 'link':self.link, 'content': self.content}
        out_file.write('<{tag} href="{link}">{content}</{tag}>\n'.format(**anchor_dict))

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):

    tag = 'h'

    def __init__(self, size, content, **kwargs):
        self.size = size
        self.tag = '{}{}'.format(self.tag, self.size)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'