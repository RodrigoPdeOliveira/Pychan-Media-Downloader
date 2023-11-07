import requests
import os
from bs4 import BeautifulSoup


def check_dir(dir_path: str):
    """Creates a directory if it doesn't exists yet

    Args:
        dir_path (str): Path to be checked
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def download_media(url: str, name: str, download_dir: str):
    """Download a file from a url

    Args:
        url (str): URL to download
        name (str): File name with extension (name.ext)
        download_dir (str): Download Path
    """
    download_path = os.path.join(download_dir, f"{name}")
    response = requests.get(url, allow_redirects=True)
    with open(download_path, "wb") as f:
        f.write(response.content)


def get_media(thread_url: str):
    """Find and yields every media in a 4chan thread

    Args:
        thread_url (str): Thread to check

    Yields:
        Generator[tuple[str, str]]: Yields a url and name
    """
    response = requests.get(thread_url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("div", attrs={"class": "fileText"}):
        element = link.find("a")
        url = "https://" + element.get("href")[2:]
        name = element.string
        yield url, name


def thread_name(thread_url: str) -> str:
    """Finds the name of the thread, if not available uses the id as name

    Args:
        thread_url (str): Thread to check

    Returns:
        str: Returns thread name or thread id
    """
    response = requests.get(thread_url)
    soup = BeautifulSoup(response.text, "html.parser")

    subject = soup.find("span", attrs={"class": "subject"})

    if subject.text:
        return subject.text
    else:
        return thread_url.split("/")[-1]
