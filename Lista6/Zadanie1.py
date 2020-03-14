import bs4
import requests
import re
import time


class Crawler:
    """Iterator that is used in crawl function."""

    def __init__(self, start_page, distance, action):
        self.licznik = 0
        self.hrefs = [start_page]
        self.action_on_hrefs = [action(start_page)]
        start = 0
        while distance:
            for i in range(start, len(self.hrefs)):
                new_start = len(self.hrefs)
                time.sleep(0.01)
                page = requests.get(self.hrefs[start])
                soup = bs4.BeautifulSoup(page.text, "html.parser")
                all_hrefs = soup.find_all("a")
                for link in all_hrefs:
                    href = link.get("href")
                    if href[0:7] == "http://" or href[0:8] == "https://":
                        complete_href = href
                        if complete_href not in self.hrefs:
                            self.hrefs.append(complete_href)
                            self.action_on_hrefs.append(action(complete_href))
            distance -= 1
            start = new_start

    def __iter__(self):
        return self

    def __next__(self):
        index = self.licznik
        if index == len(self.hrefs):
            return None
        current_tuple = (self.hrefs[index], self.action_on_hrefs[index])
        self.licznik += 1
        return current_tuple


def crawl(start_page, distance, action):
    crawler = Crawler(start_page, distance, action)
    result = next(crawler, None)
    while result:
        print(result)
        print("")
        print(result[1])
        print("")
        result = next(crawler, None)


def search_for_python(page):
    time.sleep(0.01)
    content = requests.get(page).content
    soup = bs4.BeautifulSoup(content, "html.parser")
    for script in soup(["script", "style"]):
        script.decompose()
    text_clean = soup.get_text()
    text_clean = text_clean.replace('\n', ' ')
    text_clean = text_clean.replace('\r', ' ')
    result = text_clean
    result = re.findall(r"([^.!?]*?Python[^.]*\. )", result)
    return "\n \n ".join(result)


crawl("http://www.ii.uni.wroc.pl/~marcinm/dyd/python/", 1, search_for_python)
