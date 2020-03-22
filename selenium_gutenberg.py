import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_info(title):
    base_url = 'http://www.gutenberg.org/wiki/Main_Page'
    browser = webdriver.Chrome()
    browser.get(base_url)
    browser.implicitly_wait(3)

    # search_field = browser.find_element_by_tag_name('input')
    search_field = browser.find_element_by_name('query')
    search_field.send_keys(title)
    search_field.submit()
    
    sleep(3)
    # browser.implicitly_wait(3)

    page_source = browser.page_source
    
    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    event_cells = soup.find_all('li', {'class': 'booklink'})
    print(event_cells)
    entries_str = []
    for e in event_cells:
        # print('cell: ',e)
        #title = e.select('a span span')[0].text
        #print(title)
        #subtitle = e.select('span:nth-child(1)')[0].text
        extra = e.select('span:nth-child(2)')[0].text
        #phone = e.select('span:nth-child(3)')[0].text
        #samlet = '{}\n'.format(extra)
        #print(samlet)
        # print(element.text)
        entries_str.append(extra)
    return entries_str

def save_to_file(content, out_path='./test.txt'):
    with open(out_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    entries = get_info('Møller')
    save_to_file('\n\n'.join(entries))
