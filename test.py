html = """
<!DOCTYPE html>
&lt;link Hello World | foo&gt;
&lt;link-new-tab Hello World | foo&gt;
"""

import bs4
import jinja2
import re
import tags
import processors


def collect_processors():
    return [
        processors.column.Column,
    ]


def collect_tags():
    return [
        tags.link.Link,
        tags.link.LinkNewTab,
    ]


def _handle_match(idents_to_classes, match):
    raw_content = match.group(0)
    tag_command = match.groupdict()['command']
    ident, args = tag_command.split(' ', 1)
    args = [arg.strip() for arg in args.split('|')]
    tag_class = idents_to_classes.get(ident)
    if not tag_class:
        return raw_content
    jinja_env = jinja2.Environment()
    tag_instance = tag_class(jinja_env)
    return tag_instance.to_html(*args)


def parse_google_html(html):
    all_tags = collect_tags()
    tag_idents = '|'.join([tag_class.ident for tag_class in all_tags])
    tag_regex_str = r'&lt;(?P<command>({})(\s.*?)?)&gt;'.format(tag_idents)
    idents_to_classes = dict([(tag_class.ident, tag_class)
                              for tag_class in all_tags])
    regex = re.compile(tag_regex_str, re.I)
    func = lambda match: _handle_match(idents_to_classes, match)
    return regex.sub(func, html)


def test(html):
    parsed_html = parse_google_html(html)
    soup = bs4.BeautifulSoup(parsed_html, 'html5lib')
    for processor_class in collect_processors():
        processor_instance = processor_class()
        processor_instance.process(soup)
    return soup


print unicode(test(html))
