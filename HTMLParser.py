from bs4 import BeautifulSoup
import csv
import datetime

import re

columns = ['id', 'price', 'date', 'time']
with open('shoes_old.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(columns)

def HTMLParser(parser):
    start = datetime.datetime.now()

    with open(parser, encoding='utf-8') as file:
        readFile = file.read()

    BS = BeautifulSoup(readFile, 'lxml')

    Finding = BS.find(class_="table-responsive")

    tr = Finding.find_all('tr')

    for i in range(1, len(tr)):
        id = str(tr[i]).split('"')
        id = id[19]

        td = tr[i].find_all('td')
        br = str(td[2]).split('GMT')
        br1 = str(br[0]).split('  ')
        price = br1[-1] + 'GMT'

        a = str(td[-1]).split(' ')
        date = a[20]

        b = str(a[21])
        time = b[:5]

        columns = [id, price, date, time]
        with open('shoes_old.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(columns)

    stop = datetime.datetime.now()
    print(stop - start)

def searchForLastPage(parser):
    '''
    returns the last page number
    :param readFile: parsing page
    :return: the last page number is returned
    '''
    with open(parser, encoding='utf-8') as file:
        readFile = file.read()

    BS = BeautifulSoup(readFile, 'lxml')
    Finding = BS.find(class_="pagination flex flex-j-between flex-a-ctr")

    RF = Finding.find_all('li')
    match = re.findall(r'\d{2,3}', str(RF[-2]))
    return int(match[0])


# x = searchForLastPage('result.html')
# print(x)


# tr = Finding.find_all(class_="page-link")


#with open('table.html', 'w', encoding='utf-8') as file:
    #file.write(str(Finding))

#Finding = BS.find(class_="table-responsive")