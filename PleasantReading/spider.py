# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4
import re
from PIL import Image
from random import randint
import json
import unicodedata

INIT = 1
idcnt = 0
categoryTree = {}

def remove_emoji(text):
    text_without_emoji = ''
    for char in text:
        if unicodedata.category(char) != 'So':
            text_without_emoji += char
    return text_without_emoji

def getHTMLText(url):
    try:
        requests.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        r = requests.get(url, timeout = 10, headers = {'user-agent': 'Mozilla/5.0', 'Connection': 'close'})
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'ERROR'

def login():
    url = 'http://154.8.183.51/manager/login'
    data = {'id': 'abyss7893', 'pwd': 'abyss7893'}
    for i in range(50):
        try:
            requests.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            response = requests.post(url, timeout = 10, json = data)
            assert(response.status_code == 200)
            break
        except Exception as e:
            print(e)
            continue
    return "Bearer " + response.json()['access']

# 换算：25W words = 10M
# 10G = 25000W words
# 5个字数档次 * x个分类 * 1200 *  = 25000

def getBooks():
    cates = ['chanId2', 'chanId4', 'chanId5', 'chanId6', 'chanId9', 'chanId10', 'chanId12', 'chanId15']
    num2size = [8, 8, 8, 8, 1]
    books = []
    cnt = 0
    for cate in cates:
        print('Crawling', cate)
        for size in range(5):
            url = 'https://www.qidian.com/free/all/' + cate + '-' + 'size' + str(size+1)
            text = getHTMLText(url)
            ren = r'<h2><a href="//book.qidian.com/info/(.*?)"'
            ren_url = re.compile(ren)
            book_url = ren_url.findall(text)
            if len(book_url) > num2size[size]:
                books += book_url[:num2size[size]]
                cnt += num2size[size]
            else:
                books += book_url
                cnt += len(book_url)
        print('Finished', cate, 'and cumulative number is', cnt)
    print('Finished crawling urls')
    return books

def submitBasicInfo(id, title, au, cate, intro, cover):
    title = remove_emoji(title)
    au = remove_emoji(au)
    cate = remove_emoji(cate)
    intro = remove_emoji(intro)

    url = 'http://154.8.183.51/manager/newbook2'
    data = {'title': title, 'category': cate, 'brief': intro, 'status': '连载' if randint(0, 1) == 0 else '完结', 'author': au, 'vip': True if randint(0, 3) == 0 else False, 'onShelf': True}
    headers = {'Content-type': 'application/json', 'Authorization': login(), 'Connection': 'close'}

    for i in range(50):
        try:
            requests.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            response = requests.post(url, timeout = 10, data=json.dumps(data), headers=headers)
            assert(response.status_code == 200)
            break
        except Exception as e:
            print(e)
            continue

    print('Basic text submitted successfully!')

    for i in range(50):
        try:
            requests.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            response = requests.get(cover, timeout = 10, headers = {'user-agent': 'Mozilla/5.0', 'Connection': 'close'})
            assert(response.status_code == 200)
            break
        except Exception as e:
            print(e)
            continue

    filename = 'tmp.webp'
    with open(filename, 'wb') as f:
        f.write(response.content)
    print('Got the cover successfully')

    im = Image.open(filename)
    if im.mode == "RGBA":
        im.load()
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])
    save_name = filename.replace('webp', 'jpg')
    im.save('{}'.format(save_name), 'JPEG')
    print('Convert the image to jpeg successfully')

    url = 'http://154.8.183.51/manager/setcover'
    headers = {'Authorization': login(), 'Connection': 'close'}
    with open('tmp.jpg', 'rb') as f:
        img = f.read()
    data = {'bookid': id}
    files = {'img': ('tmp.jpg', img)}
    for i in range(50):
        try:
            requests.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            response = requests.post(url, timeout=10, data=data, files=files, headers = headers)
            assert(response.status_code == 200)
            break
        except Exception as e:
            print(e)
            continue
    print('Image submitted successfully!')

def submitContent(id, cnum, ctitle, text, token):
    ctitle = remove_emoji(ctitle)
    text = remove_emoji(text)
    url = 'http://154.8.183.51/manager/uploadchapter'
    data = {'bookid': id, 'chapter': cnum, 'context': text, 'title': ctitle}
    headers = {'Content-type': 'application/json', 'Authorization': token, 'Connection': 'close'}
    for i in range(50):
        try:
            requests.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            response = requests.post(url, timeout = 10, data=json.dumps(data), headers=headers)
            assert(response.status_code == 200)
            break
        except Exception as e:
            print(e)
            continue
    print('Context submitted successfully!')

def getBookDetails(url, id):
    global idcnt
    print('Getting Basic Info of Book', id, '......')

    text = getHTMLText(url)

    ren = r' <h1>.*?<em>(.*?)</em>'
    for i in range(20):
        if len(re.compile(ren).findall(text))>0:
            break
        text = getHTMLText(url)
    if len(re.compile(ren).findall(text)) == 0:
        idcnt -= 1
        return
    title = re.compile(ren).findall(text)[0]

    ren = r'writer.*?>(.*?)</a>'
    author = re.compile(ren).findall(text)[0]

    ren = r'qd_G10\".*?>(.*?)</a>'
    category1 = re.compile(ren).findall(text)[0]
    ren = r'qd_G11\".*?>(.*?)</a>'
    category2 = re.compile(ren).findall(text)[0]

    if category1 in categoryTree:
        if category2 not in categoryTree[category1]:
            categoryTree[category1].append(category2)
    else:
        categoryTree[category1] = [category2]

    ren = r'book-intro\"><p>(.*?)</p>'
    intro = re.compile(ren).findall(text)[0]
    intro = "".join(intro.split())
    intro = intro.replace('<br>', '\n')

    ren = r'\"og:image\" content=\"(.*?)\"/>'
    cover = 'https:' + re.compile(ren).findall(text)[0] + '.webp'

    print('编号：', id)
    print('书名：', title)
    print('作者：', author)
    print('分类：', category1, category2)
    print('简介：', intro[:20])
    print('封面：', cover)

    print('Posting Basic Info...')
    submitBasicInfo(id, title, author, category1 + '-' + category2, intro, cover)

    url = url + '#Catalog'
    print('Crawling outline:', url)
    for i in range(50):
        try:
            text = getHTMLText(url)
            soup = BeautifulSoup(text, 'html5lib')
            assert(len(soup.find_all('div', {'class': 'volume'})) > 0)
            break
        except Exception as e:
            print(e)
            continue
    cnum=0
    token = login()
    for vols in soup.find_all('div', {'class': 'volume'}):
        ul = vols.find('ul', {'class': 'cf'})
        for li in ul.find_all('li'):
            cnum += 1
            a = li.find('h2').find('a')
            ctitle = a.text
            curl = 'https:' + a.attrs['href']

            for i in range(50):
                try:
                    content = getHTMLText(curl)
                    soup = BeautifulSoup(content, 'html5lib')
                    assert(len(soup.find_all('p')) > 0)
                    break
                except Exception as e:
                    print(e)
                    continue

            # print(soup.prettify())
            pars = soup.find_all('p')
            text, cnt = "", 0
            for par in pars:
                if par.text.startswith('　'):
                    text = text + par.text[2:] + '\n'
                    cnt += 1
            print('Got chapter {} of book {}, the number of paragraphs is {}'.format(cnum, id, cnt))
            submitContent(id, cnum, ctitle, text, token)

if __name__ == '__main__':
    books = getBooks()
    for i in range(len(books)):
        getBookDetails('https://book.qidian.com/info/' + books[i], idcnt+INIT)
        idcnt += 1
    print(categoryTree)
