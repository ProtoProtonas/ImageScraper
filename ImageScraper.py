# credits go somewhere

import urllib.request
import requests
from PIL import Image

def if_full_link(link):
    if 'http' in link:
        return True
    else:
        return False


def download_image(link):    # downloads image from a given url (single url pointing to a single image)
    name = link.split('/')[-1]
    with open(name, 'wb') as handle:
        response = requests.get(link, stream = True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)



def get_links(url):       # gets links from the <img src="the_link_you_want"> tags

    links = []
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    html = html.decode('ascii')

    formats = ['png', 'jpg']
    
    img_pos = 0
    while(img_pos != -1):
        img_pos = html.find('<img')

        if img_pos != -1:
            new_html = html[img_pos:]
            img_tag = new_html[:new_html.find('>') + 2]\
            
            img_link = img_tag[img_tag.find('src'):]
            img_link = img_link[img_link.find('"') + 1:]
            img_link = img_link[:img_link.find('"')]

            if not if_full_link(img_link):
                img_link = url + img_link

            format = img_link.split('.')[-1]
            if format in formats:
                links.append(img_link)


        html = html[img_pos + 4:]
    return links

def if_meme(image):
    #check size


def main():
    links = get_links('https://projecteuler.net/')
    for link in links:
        download_image(link)



main()