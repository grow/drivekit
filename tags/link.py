import base


class Link(base.Tag):
    """Renders a text link to another page from Google Docs.

    Usage:

    ```
    <link Page>
    <link Page | Link Title>
    ```
    """
    ident = 'link'
    template = """<a href="{{url}}">{{title}}</a>"""

    def process(self, doc_title, link_title=None):
        url = doc_title
        title = link_title
        return {
            'title': title,
            'url': url,
        }


class LinkNewTab(Link):
    ident = 'link-new-tab'
    template = """<a href="{{url}}" target="_blank">{{title}}</a>"""
