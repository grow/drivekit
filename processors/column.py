class Column(object):

    def process(self, soup):
        tables = soup.find_all('table')
        for table in tables:
            pass
        print 'foo'
