from utils import utils

class PropertiesParser:
    @staticmethod
    def parse(node, content):
        return utils.Utils.check_property(node, content, 'to', str, True)