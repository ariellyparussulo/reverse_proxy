""" parse root node from config file """
from utils import utils

class RootParser:
    """
    methods used to validate root node properties
    """
    @staticmethod
    def parse(node, content):
        """
        calls check_property method to validate root nodes types and
        whether they are mandatory.
        """
        return (utils.Utils.check_property(node, content, 'redirect', bool, False)
                and utils.Utils.check_property(node, content, 'to', str, True))
