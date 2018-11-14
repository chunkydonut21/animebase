from bs4 import BeautifulSoup
import cfscrape
import re

scraper = cfscrape.create_scraper()


def getAnimeList(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    lst = []

    for anime in soup.find_all('tr')[2:]:
        # title = anime.td.a.text.strip()
        url = f"http://kissanime.ru{anime.td.a['href'].strip()}"
        imgUrl = anime.td['title'].strip().replace(u'\r\n', u'')
        image = re.findall('http\S+jpg', str(imgUrl))[0]
        # status = anime.find_all('td')[-1].text.strip()
        slug = url.split('/')[-1]

        # moreInfo = getAnimeInformantion(url)
        # episodeList = getAnimeEpisodesDetails(url)

        lst.append({
            # 'title': title,
            'url': url,
            # 'status': status,
            'image': image,
            'slug': slug
            # 'moreInfo': moreInfo,
            # 'episodes': episodeList
        })
    #
    # file = open("result.json", "w")
    # simplejson.dump(lst, file, indent=4)
    # file.close()

    return lst


def getAnimeInformantion(link):
    global aired, status, views

    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    container = soup.find('div', id='container')

    name = container.find('a', class_='bigChar').text.strip()

    genreList = [genre.text.strip() for genre in container.find_all('a', class_='dotUnder')]

    p = container.find_all('p')
    img_container = container.find('div', id='rightside')
    image = img_container.img['src']

    description = p[-1].text.strip().replace(u'\xa0', u' ')
    slug = link.split('/')[-1]

    if len(p) is 4:
        aired = 'Unknown'
        detail = p[1].text.split("\n")
        detail = [x.strip().replace(u'\xa0', u' ') for x in detail if x is not None]
        status = detail[1].split(":")[1]
        views = detail[2].split(":")[1]

    elif len(p) is 5:
        aired = 'Unknown'
        detail = p[2].text.split("\n")
        detail = [x.strip().replace(u'\xa0', u' ') for x in detail if x is not None]
        status = detail[1].split(":")[1]
        views = detail[2].split(":")[1]

    elif len(p) is 6:
        aired = p[2].text.strip().replace(u'\xa0', u' ')
        detail = p[3].text.split("\n")
        detail = [x.strip().replace(u'\xa0', u' ') for x in detail if x is not None]
        status = detail[1].split(":")[1]
        views = detail[2].split(":")[1]

    else:
        aired = 'Unknown'
        status = 'Unknown'
        views = 'Unknown'

    episodeList = getAnimeEpisodesDetails(link)

    animeDescription = {
        "name": name,
        "aired": aired,
        "status": status,
        "slug": slug,
        "views": views,
        "image": image,
        "genre": genreList,
        "description": description,
        "episodeList": episodeList
    }

    file = open("info.txt", "w")
    file.write(str(animeDescription))
    file.close()


def getEpisodeVideoUrl(link):
    global episodeUrl
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')
    for line in soup:
        stuff = re.findall('https://www.rapidvideo.com\S+', str(line))
        if len(stuff) > 0:
            episodeUrl = stuff

    return episodeUrl[0].replace(u'\"', u'')


def getAnimeEpisodesDetails(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    container = soup.find('table')

    lst = []
    for items in container.find_all('a'):
        name = items.text.strip()
        url = getEpisodeVideoUrl(f"http://kissanime.ru/{items['href']}&s=rapidvideo")
        title = items['title']
        lst.append({"name": name, "url": url, "title": title, 'slug': name.replace(u' ', '-')})

    return lst


def getCustomAnimeList(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    lst = []

    for anime in soup.find_all('tr')[2:]:
        title = anime.td.a.text.strip()
        url = anime.td.a['href'].strip()
        status = anime.find_all('td')[-1].text.strip()

        lst.append({
            'title': title,
            'url': url,
            'status': status
        })

    return lst

