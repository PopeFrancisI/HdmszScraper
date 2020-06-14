import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve


def get_gallery_urls(showcase_url: str):
    try:
        response = requests.get(showcase_url)
        response.raise_for_status()
        print(response.status_code)

        soup = BeautifulSoup(response.text, 'html5lib')

        galleries = soup.select('.works a')

        gallery_urls = []
        for gallery in galleries:
            gallery_urls.append(urljoin(showcase_url, gallery.attrs['href']))

        return gallery_urls

    except requests.HTTPError:
        return None


def scrape_gallery(gallery_url):
    pass


def scrape_showcase(showcase_url: str):

    page_counter = 1

    while True:

        full_showcase_url = f'{showcase_url}/page{page_counter}.html'
        gallery_urls = get_gallery_urls(full_showcase_url)

        for gallery_url in gallery_urls:
            scrape_gallery(gallery_url)

        page_counter += 1


def main():

    appeal_url = "http://www.hdmsz.com/showcase/appeal"
    fairlady_url = "http://www.hdmsz.com/showcase/fairlady"

    scrape_showcase(appeal_url)
    scrape_showcase(fairlady_url)


if __name__ == "__main__":
    main()


