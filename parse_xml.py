from bs4 import BeautifulSoup
import requests
import lxml


def parse_xml():
    url = "http://upload.itcollege.ee/~aleksei/test.xml"
    xml_content = requests.get(url).content
    soup = BeautifulSoup(xml_content, 'xml')

    result = soup.find_all("data")
    for res in result:
        (res.get_text())

    return res.get_text()
print(parse_xml())
