import base
import cssutils


class Column(base.Processor):

    def process(self, soup):
        sheet = self.stylesheet
        # Map drive classes to style rules.
        drive_classes_to_rules = {}
        style_rules = sheet.cssRules.rulesOfType(cssutils.css.CSSRule.STYLE_RULE)
        for rule in style_rules:
            if rule.selectorText.startswith('.c'):
                drive_classes_to_rules[rule.selectorText] = rule

        tables = soup.find_all('table')
        columns = first_row.find_all('td', recursive=False)
        widths = []
        column_content = []
        for table in tables:
	    columns = first_row.find_all('td', recursive=False)
	    widths = []
	    for cell in columns:
	      class_names = cell.get('class') or []
	      for class_name in class_names:
		class_name = '.{}'.format(class_name)
		if class_name in drive_classes_to_rules:
		  rule = drive_classes_to_rules[class_name]
		  width = rule.style.width
		  widths.append(width)
