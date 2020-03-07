class Utils:
    @staticmethod
    def check_property(node, content, key, _type, mandatory):
        if mandatory is True and key not in content:
            print("[%s]: You need to declare the '%s' property." % (node, key))
            return False
        elif key in content and type(content[key]) is not _type:
            print("[%s]: '%s' property must be a '%s'." % (node, key, _type.__name__))
            return False
        return True