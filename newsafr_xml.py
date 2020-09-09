import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding = 'UTF-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

news_list = root.findall('channel/item')

all_news = ''
for i,news in enumerate(news_list):
  discript = news.find("description").text
  all_news += discript
list_all_word = all_news.split(' ')
new_list = []
for element in list_all_word:
  if len(element) > 6:
    new_list.append(element)
  else:
    continue
common_words = sorted(set(new_list), key = new_list.count, reverse = True)

print(common_words[:10])