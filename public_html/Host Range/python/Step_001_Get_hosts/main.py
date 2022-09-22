import requests
from bs4 import BeautifulSoup

def get_page(url):
    page = requests.get(url)
    return page

def get_first_page():
    url = 'https://www.wur.nl/en/research-results/chair-groups/plant-sciences/laboratory-of-nematology/nematode-in-the-picture/nematode-pictures.htm'
    page = get_page(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    liList = soup.find_all('li', class_='stone')
    lst = list()
    for li  in liList:
        href = ''
        caption = ''
        a = li.find_all('a', class_='navigation')
        for kkk in a :
            href = str(kkk['href']).strip()
            href = 'https://www.wur.nl' + href
        for jj in a:
            h2 = jj.find_all('h2')
            for kk in h2:
                caption = str(kk.get_text()).strip()
        item = (href, caption)
        lst.append(item)
    return lst

def get_all_images():
    page = get_first_page()
    lst = list()
    for i in page:
        author = ''
        (url, genus) = i
        page = get_page(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        collection = soup.find_all( class_='WUREditableContent')
        for iii in collection:
            p = iii.find_all('p')
            for aa in p :
                txt = str(aa.get_text()).strip()
                if 'Picture:' in txt:
                    lll = txt.split(':')
                    aaa = len(lll)
                    if len(author) < 1:
                        author = str(lll[aaa-1]).strip()

        figure = soup.find_all('figure')
        for f in figure:
            href = ''
            title = ''
            caption = ''
            a = f.find_all('a')
            for kk in a:
                href = kk['href']
                href = 'https://www.wur.nl' + href
                title = kk['title']
            figcaption = f.find_all('figcaption')
            for cap in figcaption:
                caption = str(cap.get_text()).strip()
            tup =  (genus, href,title,caption,author)
            lst.append(tup)
    return lst

def main():
    images = get_all_images()
    f = open("./ImagesOnWUR.csv", "w")
    header = ''
    header = header + 'genus,'
    header = header + 'href,'
    header = header + 'title,'
    header = header + 'caption,'
    header = header + 'author,'
    f.write(header + '\n')
    for i in images:
        (genus, href, title, caption,author) = i
        print (genus)
        print(href)
        print (title)
        print (caption)
        print (author)
        f.write('"' + str(genus) + '"' + ',')
        f.write('"' + str(href) + '"' + ',')
        f.write('"' + str(title) + '"' + ',')
        f.write('"' + str(caption) + '"' + ',')
        f.write('"' + str(author) + '"' )
        f.write('\n')
    f.close()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
