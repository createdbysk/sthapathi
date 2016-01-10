import pystache

other_than_name = {"exclamation": "!"}


class Context(object):
    """
    Provides the context variables
    """
    def name(self):
        return "World"

    def __getattr__(self, item):
        return other_than_name[item]

template = "Hello {{name}}{{exclamation}}"
context = Context()
print pystache.render(template, context)
