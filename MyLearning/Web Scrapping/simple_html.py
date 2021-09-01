from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Here is one paragraph.</p>
<p>Here is another paragraph without class</p>
<ul>
    <li>Rolf</li>
    <li>Jose</li>
    <li>Jen</li>
</ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')
def find_title():
    h1_tag = simple_soup.find('h1')     #to get the details of the entire tag, However find only gives only one of the many instances of tag present

    print(h1_tag.string)    #to get the exact string present in the tag

def find_list_items():
    list_items = simple_soup.find_all('li')     #findall finds all the instances of the tag present and return it as a list of all the items found
    new_list = [x.string for x in list_items]
    print(new_list)

def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)

def find_other_paragraphs():
    paragraph = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraph if 'subtitle' not in p.attrs.get('class', [])]  #get method has a benefit as it won't raise any error if it can't find a key, after class specifying a empty list to return if it doesn't find it
    print(other_paragraph[0].string)

find_title()
find_list_items()
find_subtitle()
find_other_paragraphs()
