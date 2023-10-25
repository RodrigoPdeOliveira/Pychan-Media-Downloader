import requests
import os
from bs4 import BeautifulSoup


def check_dir(dir_path: str):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def download_media(url: str, name: str, ext: str, download_dir: str):
    download_path = os.path.join(download_dir, f"{name}.{ext}")
    response = requests.get(url, allow_redirects=True)
    with open(download_path, "wb") as f:
        f.write(response.content)


def get_media(thread_url: str):
    response = requests.get(thread_url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("div", attrs={"class": "fileText"}):
        element = link.find("a")
        url = "https://" + element.get("href")[2:]
        name = element.string.split(".")
        ext = name[-1]
        name = name[0]
        yield url, name, ext


def thread_name(thread_url: str) -> str:
    response = requests.get(thread_url)
    soup = BeautifulSoup(response.text, "html.parser")

    subject = soup.find("span", attrs={"class": "subject"})

    if subject.text:
        return subject.text
    else:
        return thread_url.split("/")[-1]
