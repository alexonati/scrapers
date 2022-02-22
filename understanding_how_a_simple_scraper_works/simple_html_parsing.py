from bs4 import BeautifulSoup

SIMPLE_HTML: str = '''<html>
<head></head>
<body>
<h1>Acesta este un titlu / element header in htlm.</h1>
<p class="subtitle">Ala bala portocala. Dani are mere.</p>
<p>Un paragraf html fara clasa.]</p>
<ul>
    <li>Alex</li>
    <li>Alina</li>
    <li>Raul</li>
    <li>Victor</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    print(simple_soup.find('h1').string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_content = [s.string for s in list_items]
    print(list_content)


def find_paragraph_with_class():
    print(simple_soup.find('p', {'class': 'subtitle'}).string)


def find_paragraph_without_class():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)


find_title()
find_list_items()
find_paragraph_with_class()
find_paragraph_without_class()
