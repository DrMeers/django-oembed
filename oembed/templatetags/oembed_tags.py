from django import template
from django.template.defaultfilters import stringfilter
from django.utils import http
from oembed.core import replace
from oembed.models import StoredOEmbed

register = template.Library()


@register.filter
def urlunquote(value):
    return http.urlunquote(value)


@register.filter
def urlunquote_plus(value):
    return http.urlunquote_plus(value)


def oembed(input, args=None):
    if args:
        try:
            width, height = map(int, args.lower().split('x'))
        except ValueError:
            raise template.TemplateSyntaxError("Oembed's optional " \
                "WIDTHxHEIGHT argument requires WIDTH and HEIGHT to be " \
                "positive integers.")
    else:
        width, height = None, None
    return replace(input, max_width=width, max_height=height)
oembed.is_safe = True
oembed = stringfilter(oembed)

register.filter('oembed', oembed)

def do_oembed(parser, token):
    """
    A node which parses everything between its two nodes, and replaces any
    links with OEmbed-provided objects, if possible.

    Supports one optional argument, which is the maximum width and height,
    specified like so:

        {% oembed 640x480 %}http://www.viddler.com/explore/SYSTM/videos/49/{% endoembed %}
    """
    args = token.contents.split()
    if len(args) > 2:
        raise template.TemplateSyntaxError("Oembed tag takes only one (option" \
            "al) argument: WIDTHxHEIGHT, where WIDTH and HEIGHT are positive " \
            "integers.")
    if len(args) == 2:
        try:
            width, height = map(int, args[1].lower().split('x'))
        except ValueError:
            raise template.TemplateSyntaxError("Oembed's optional " \
                "WIDTHxHEIGHT argument requires WIDTH and HEIGHT to be " \
                "positive integers.")
    else:
        width, height = None, None
    nodelist = parser.parse(('endoembed',))
    parser.delete_first_token()
    return OEmbedNode(nodelist, width, height)

register.tag('oembed', do_oembed)

class OEmbedNode(template.Node):
    def __init__(self, nodelist, width, height):
        self.nodelist = nodelist
        self.width = width
        self.height = height

    def render(self, context):
        kwargs = {}
        if self.width and self.height:
            kwargs['max_width'] = self.width
            kwargs['max_height'] = self.height
        return replace(self.nodelist.render(context), **kwargs)

# This comes in handy, so you don't hit the database so many times
# if you want to access different fields for a same object
_oembed_objects = {}

@register.filter
def get_oembed_property(oembed_url, json_property):
    """ Use it like this:
        {% url_string|get_oembed_property:'thumbnail_url' %}    
    """
    if not oembed_url in _oembed_objects:
        matches = StoredOEmbed.objects.filter(match=oembed_url)
        if matches:
            # Found it, happy path
            oembed = matches[0]
        else:
            # If not found, we will try to fetch it
            _ = replace(oembed_url)
            matches = StoredOEmbed.objects.filter(match=oembed_url)
            if matches:
                # Haven't been parsed before, but now is available
                oembed = matches[0]
            else:
                # Nothing to do, is not an oembed
                oembed = None
        _oembed_objects[oembed_url] = oembed
        
    if _oembed_objects[oembed_url]:
        return _oembed_objects[oembed_url].get_json(json_property)
    else:
        return '' 
