""" parse main node from config file """
from utils import utils
class MainParser:
    """
    methods used to validate main node properties
    """
    @staticmethod
    def parse(node, content):
        """
        calls check_property method to validate main nodes types and whether they are mandatory
        """
        return (utils.Utils.check_property(node, content, "port", int, True) and
                utils.Utils.check_property(node, content, "hostname", str, True) and
                utils.Utils.check_property(node, content, "redirect-to-https", bool, True))
