import requests
import urllib.parse
from html.parser import HTMLParser

class NutrimaticParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.record = False
        self.res = []
        self.font_size = None

    def handle_starttag(self, tag, attrs):
        if tag != 'span':
            return
        self.record = True
        for key, value in attrs:
            if key == 'style':
                # Okay for now but should find a more robust extraction for font-size
                self.font_size = value[11:-2]
                return 
            
    def handle_endtag(self, tag):
        if tag == 'span':
            self.record = False

    def handle_data(self, data):
        if self.record:
            self.res.append((data, self.font_size))
         

def query(q, 
        normalize_freq=False, 
        try_harder=False, 
        addtl_comp=2000000):
    """
    Query nutrimatic with q

    Setting try_harder to True will increase the computation time requested. Can increase addtl_comp to get more compute time. PROBABLY NOT A GOOD IDEA TO ABUSE THIS.

    Returns a list of tuples. Each tuple contains a string with the result and a relative measure of frequency as determined by the font size Nutrimatic assigns.
    """
    query = urllib.parse.quote_plus(q)
    req = 'https://nutrimatic.org/?q={}'.format(query)
    if try_harder:
        req += '&comp={}'.format(addtl_comp)
    res = requests.get(req)
    
    parser = NutrimaticParser()
    parser.feed(res.text)
    result = [(i[0], float(i[1])) for i in parser.res]
    if normalize_freq:
        min_freq = min(result, key = lambda x: x[1])[1]
        result = [(i[0], i[1] / min_freq) for i in result]
    return result

if __name__ == "__main__":
    print(query('test', normalize_freq=False))
    print(query('test', normalize_freq=True))
    print(query("_ ___ ___ _*burger", try_harder=True))