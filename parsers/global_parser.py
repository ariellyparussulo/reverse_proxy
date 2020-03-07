"""Global Parser that builds every individual parsers that knows how to handle a specific node"""
from . import main_parser, root_parser, properties_parser

class GlobalParser:
    """Global Parser Class"""
    def __init__(self):
        self.final_map = {}

    def get_final_map(self):
        """Return the final_map"""
        return self.final_map

    @classmethod
    def parse(cls, node, content):
        """Parses the config with their own handlers"""
        if node == 'main':
            main_parser.MainParser.parse(node, content)
        elif node == 'root':
            root_parser.RootParser.parse(node, content)
        else:
            properties_parser.PropertiesParser.parse(node, content)
