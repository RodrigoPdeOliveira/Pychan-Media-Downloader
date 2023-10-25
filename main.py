import argparse
import helpers


def main():
    parser = argparse.ArgumentParser()

    url_group = parser.add_mutually_exclusive_group()
    url_group.add_argument(
        "-u", "--url", help="4Chan thread URL"
    )
    url_group.add_argument(
        "-f", "--file", help="File with multiple urls"
    )

    parser.add_argument(
        "-o", "--output", help="Output path", default="./downloads"
    )
    # TODO: Download image only or video only mode

    args = parser.parse_args()

    if not args.url and not args.file:
        return print("Must select either --file or --url.")

    if args.file:
        with open(args.file, "r") as f:
            for url in f:
                download(url, args.output)
    else:
        download(args.url, args.output)


def download(url: str, download_dir: str):
    download_dir += f"/{helpers.thread_name(url)}"

    helpers.check_dir(download_dir)

    for url, name, ext in helpers.get_media(url):
        print(f"Downloading {name}.{ext}")
        helpers.download_media(url, name, ext, download_dir)

    print("All media downloaded.")


if __name__ == "__main__":
    main()
