class Validator(object):
    """The base class for validators"""
    def validate(self, data):
        """Override this method to validate the data."""
        raise NotImplementedError("{} does not implement validate.".format(type(self).__name__))
