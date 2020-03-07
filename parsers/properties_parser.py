""" parse properties (e.g.: path1) node from config file """
from utils import utils

class PropertiesParser:
    """
    methods used to validate property node properties
    """
    @staticmethod
    def parse(node, content):
        """
        calls check_property method to validate properties nodes types and
        whether they are mandatory.
        """
        return utils.Utils.check_property(node, content, 'to', str, True)
