"""Search in navbar"""
from django import template

from search.forms import SearchForm

register = template.Library()


class NavbarSearchNode(template.Node):
    """Node for navbar search"""

    def __init__(self):
        self.form = SearchForm()

    def render(self, context):  # pylint: disable=unused-argument
        """Render a given form"""
        self.rmedia()
        return self.form

    def rmedia(self):
        """Get a form's media"""
        return self.form.media


@register.tag(name="navbar_search")
def navbar_search(parser, token):  # pylint: disable=unused-argument
    """Tag for navbar_search"""
    return NavbarSearchNode()
