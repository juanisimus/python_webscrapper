import requests 
import urllib.request

from bs4 import BeautifulSoup as bs

def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}/'.format(i))
        soup = bs(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('Descargando imagen {}'.format(image_name))

        #funcion para completar la direccion de la img con el https:
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)

if __name__ == "__main__":
    run()