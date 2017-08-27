class Tag(object):

  def __init__(self, jinja):
    self.jinja = jinja

  def to_html(self, *args, **kwargs):
    params = self.process(*args, **kwargs)
    template = self.jinja.from_string(self.template)
    return template.render(params)
