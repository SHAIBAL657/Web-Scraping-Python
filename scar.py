from html.parser import HTMLParser
import urllib.request

# Import HTML from a URL
url = urllib.request.urlopen(
    "https://www.vrbo.com/vacation-rentals/usa/alabama/orange-beach")
html = url.read().decode()
url.close()


class Parse(HTMLParser):
    def __init__(self):
        # Since Python 3, we need to call the __init__() function of the parent class
        super().__init__()
        self.reset()
    # Defining what the method should output when called by HTMLParser.

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "div":
            for name, atr in attrs:
                print("hi")
                if name == "class" and atr == "CommonRatioCard__description":  # .startswith
                    print("CommonRatioCard__description", atr)
                if name == "class" and atr == "CommonRatioCard__price_amount":  # .startswith
                    print("CommonRatioCard__price_amount", atr)
                if name == "class" and atr == "CommonRatioCard__subcaption":  # .startswith
                    print("CommonRatioCard__subcaption", atr)
        print("hello")

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        print("Encountered some data  :", data, "\n")


p = Parse()
p.feed(str(html))
