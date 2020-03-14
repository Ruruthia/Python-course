import bs4
import requests
import re
import time
import queue
import threading

lock = threading.Lock()


class Crawler(threading.Thread):
    global lock

    def __init__(self, start_page, distance, action):

        self.distance = distance
        self.action = action
        self.hrefs_queue = queue.Queue()
        self.hrefs_queue.put(start_page)
        self.visited = {start_page: distance}
        threads = []
        for i in range(8):
            t = threading.Thread(target=self.search_page)
            t.start()
            threads.append(t)
        self.hrefs_queue.join()
        for t in threads:
            t.join()

    def search_page(self):

        while True:
            item = self.hrefs_queue.get()
            if self.visited[item] == 0:
                break
            else:
                self.find_hrefs(item, self.visited[item])
                self.hrefs_queue.task_done()

    def find_hrefs(self, given_href, distance):
        time.sleep(0.04)
        page = requests.get(given_href)
        soup = bs4.BeautifulSoup(page.text, "html.parser")
        all_hrefs = soup.find_all("a")
        for link in all_hrefs:
            href = link.get("href")
            if href and (href[0:7] == "http://" or href[0:8] == "https://"):
                complete_href = href
                if complete_href not in self.visited.keys():
                    lock.acquire()
                    self.visited[complete_href] = distance - 1
                    self.hrefs_queue.put(complete_href)
                    lock.release()

    def __iter__(self):
        self.licznik = 0
        return self

    def __next__(self):
        index = self.licznik
        hrefs = list(self.visited.keys())
        if index == len(hrefs):
            return None
        current_tuple = (hrefs[index], self.action(hrefs[index]))
        self.licznik += 1
        return current_tuple


def crawl(start_page, distance, action):
    crawler = Crawler(start_page, distance, action)
    result = next(iter(crawler), None)
    while result:
        print(result)
        result = next(crawler, None)


def search_for_python(page):
    time.sleep(0.04)
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


crawl("http://www.ii.uni.wroc.pl/~marcinm/dyd/python/", 2, search_for_python)
