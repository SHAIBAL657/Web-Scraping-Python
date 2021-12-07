import re
import urllib.request
from html.parser import HTMLParser
import mysql.connector
from mysql.connector import Error

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Import HTML from a URL
url = urllib.request.urlopen(
    "https://www.vrbo.com/vacation-rentals/usa/alabama/orange-beach")
html = url.read().decode()
url.close()


class WebParser(HTMLParser):
    # search query
    query = []

    # search result match
    match = {}

    # results list
    results = []

    # handle opening tag

    def handle_starttag(self, tag, attr):
        self.match['name'] = tag
        self.match['attr'] = attr

    # handle data within a tag
    def handle_data(self, data):
        # init query tag
        tag = self.query[0]

        # init attr query
        attr = self.query[1]

        # init query output
        text = self.query[-1]

        try:
            # found tag name
            if self.match['name'] == tag:
                # attributes are not specified in query
                if not len(attr):
                    # on tag text node query
                    if text == 'text':
                        self.results.append(data)

                    # on tag attrbute data query
                    else:
                        # loop over attributes list
                        for item in self.match['attr']:
                            # init attr key and value
                            key = item[0]
                            val = item[1]

                            # query output is within attr's key
                            if text == key:
                                self.results.append(val)

                # attributes are specified in query
                else:
                    # loop over attributes list
                    for item in self.match['attr']:
                        # init available attr key and value
                        key = item[0]
                        val = item[1]

                        # init query attr key and value
                        q_key = attr[0]
                        q_val = attr[1]

                        # match key and value pairs
                        if q_key == key and q_val == val:
                            # on tag text node query
                            if text == 'text':
                                self.results.append(data)

                            # on tag attrbute data query
                            else:
                                # loop over attributes list
                                for item in self.match['attr']:
                                    # init attr key and value
                                    key = item[0]
                                    val = item[1]

                                    # query output is within attr's key
                                    if text == key:
                                        self.results.append(val)

        except:
            pass

    # handle closing tag
    def handle_endtag(self, tag):
        # reset result match after matching closing tag
        self.match = {}

# parse content


def find(content, query):
    # create parser instance
    parser = WebParser()

    # init query
    parser.query = query

    # find matching results
    parser.feed(str(content))

    # close parser
    parser.close()

    # return results
    return parser.results


# data extraction logic
HotelName = find(content=html, query=[
    'div', ('class', 'CommonRatioCard__description'), 'text'])
WebParser.results = []
Facilites = find(content=html, query=[
    'div', ('class', 'CommonRatioCard__subcaption'), 'text'])
WebParser.results = []
Price = find(content=html, query=[
    'span', ('class', 'CommonRatioCard__price__amount'), 'text'])
WebParser.results = []
img = find(content=html, query=[
    'script', (), 'text'])
WebParser.results = []

# facilities extraction logic
facilities_ind = []
for index in range(0, len(Facilites)):
    # write line
    facilities_ind.append(Facilites[index].split(" · "))

for index in range(0, len(facilities_ind)):
    if(len(facilities_ind[index]) < 3):
        temp = facilities_ind[index]
        temp.append('None')
        facilities_ind[index] = temp

# image extraction logic
for index in range(0, len(img)):
    # take the specific one
    if(img[index].startswith('window.__PRELOADED_STATE__ ')):
        img = img[index]


list_match_img_url1 = re.findall(
    r'"tripleId":(.*?),"thumbnailUrl":(.*?),', img)
'''for i in list_match_img[-6:]:
    print(i, "\n")'''
list_match_img_url2 = re.findall(
    r'"tripleId":(.*?),"thumbnailUrl2":(.*?),', img)
list_match_img_url3 = re.findall(
    r'"tripleId":(.*?),"thumbnailUrl3":(.*?),', img)


matched_img1 = list_match_img_url1[-6:]
matched_img2 = list_match_img_url2[-6:]
matched_img3 = list_match_img_url3[-6:]

collapse_img = []
for i in range(len(matched_img1)):
    collapse_img.append([matched_img1[i][1],
                         matched_img2[i][1], matched_img3[i][1]])


# ra3g_Df7wy

final_info = []
print("\n\n\n")
for i in range(0, len(HotelName)):
    final_info.append([HotelName[i], facilities_ind[i],
                      Price[i], collapse_img[i]])

'''
for i in final_info:
    print(i, "\n")
'''


def insert_mysql(name, sleeps, bedroom, bathroom, img1, img2, img3, price):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='vrbo',
                                             user='root',
                                             password='ra3g_Df7wy')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Condo_House (Name, Sleeps, Bedroom, Bathroom, Image1, Image2, Image3, Price) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

        record = (name, sleeps, bedroom, bathroom, img1, img2, img3, price)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Villa")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# Database Insertion
for info in final_info:
    insert_mysql(info[0],
                 info[1][0],
                 info[1][1],
                 info[1][2],
                 info[3][0],
                 info[3][1],
                 info[3][2],
                 info[2])
