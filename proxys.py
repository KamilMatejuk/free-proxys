import sys
import requests
from bs4 import BeautifulSoup


def extract(file):
    url = 'https://free-proxy-list.net/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.select('[id=proxylisttable] tr')
    ips = []
    for row in table:
        ip = ':'.join(t.text for t in row.select('td')[:2])
        ips.append(ip + '\n')
    print(f'Extracted {len(ips)} proxys from {url}')
    with open(file, 'w+') as f:
        f.writelines(ips)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Specify output file as a second argument')
        exit(1)
    extract(sys.argv[1])
