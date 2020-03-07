from utils import utils

class RootParser:
    @staticmethod
    def parse(node, content):
        return utils.Utils.check_property(node, content, 'redirect', bool, False) and utils.Utils.check_property(node, content, 'to', str, True)