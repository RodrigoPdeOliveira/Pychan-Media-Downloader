import argparse
import helpers

parser = argparse.ArgumentParser()

parser.add_argument("url", help="4Chan thread URL")
parser.add_argument(
    "-o", "--output", help="Output path", default="./downloads"
)
# TODO: Download image only or video only mode
# TODO: Download from url in txt file
# TODO: Download each thread in separate dirs

args = parser.parse_args()

url = args.url
download_dir = args.output

helpers.check_dir(download_dir)

for url, name, ext in helpers.get_media(url):
    print(f"Downloading {name}.{ext}")
    helpers.download(url, name, ext, download_dir)

print("All media downloaded.")
