from . import mainParser, rootParser, propertiesParser

class GlobalParser:
    def __init__(self):
        self.finalMap = {}

    def getFinalMap(self):
        return self.finalMap

    def parse(self, node, content):
        if (node == 'main'):
            mainParser.MainParser.parse(content)
        elif (node == 'root'):
            rootParser.RootParser.parse(content)
        else:
            propertiesParser.PropertiesParser.parse(content)