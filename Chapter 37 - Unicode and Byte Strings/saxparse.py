import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False

    def startElement(self, name, attrs):
        if name == 'title':
            self.inTitle = True

    def characters(self, content):
        if self.inTitle:
            print(content)

    def endElement(self, name):
        if name == 'title':
            self.inTitle = False

import xml.sax

parser = xml.sax.make_parser()

handler = BookHandler()

parser.setContentHandler(handler)

parser.parse('mybooks.xml')