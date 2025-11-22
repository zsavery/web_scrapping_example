from bs4 import BeautifulSoup

def find_tag(path, tag):
    with open(path, 'r', encoding='utf-8') as file:
        html_source = file.read()

        soup = BeautifulSoup(html_source, 'html.parser')

        selected_tag = soup.find(tag)
        print(selected_tag)


def find_all_tag(path, tag):
    with open(path, 'r', encoding='utf-8') as file:
        html_source = file.read()

        soup = BeautifulSoup(html_source, 'html.parser')

        selected_tag_all = soup.find_all(tag)
        print(selected_tag_all)


site_path = "sites/welcome.html"

find_tag(site_path, 'h1')
find_all_tag(site_path, 'h2')