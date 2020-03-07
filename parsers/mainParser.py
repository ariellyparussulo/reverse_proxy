from utils import utils
class MainParser:
    @staticmethod
    def parse(node, content):
        return utils.Utils.check_property(node, content, "port", int, True) and utils.Utils.check_property(node, content, "redirect-to-https", bool, True)

    
