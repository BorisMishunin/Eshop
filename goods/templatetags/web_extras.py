from django import template

register = template.Library()

class Hello(template.Node):
    def __init__(self, n):
        self.name = n;
    def render(self, context):
        return "Hello, I am %s" % self.name


def get_my_string(parser, token):
    tag_name, name = token.split_contents()
    return Hello(name)


@register.filter(name='lowerup')
def lowerup(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.upper()

register.tag('get_my_string', get_my_string)
