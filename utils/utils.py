"""
This is a utility module.
"""

# pytlint: disable=too-few-public-methods
class Utils:
    """
This class implements utils methods to be used in our code.
    """
    @staticmethod
    def check_property(node, content, key, _type, mandatory):
        """
This method validates a property. It gets a node and checks if it was declared in
the right type and also if it is mandatory of not.
        """
        if mandatory is True and key not in content:
            print("[%s]: You need to declare the '%s' property." % (node, key))
            return False

        if key in content and isinstance(content[key]) is not _type:
            print("[%s]: '%s' property must be a '%s'." % (node, key, _type.__name__))
            return False

        return True
