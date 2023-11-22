import argparse
import helpers


def main():
    parser = argparse.ArgumentParser()

    url_group = parser.add_mutually_exclusive_group()
    url_group.add_argument("-u", "--url", help="4Chan thread URL")
    url_group.add_argument("-f", "--file", help="File with multiple urls")

    parser.add_argument(
        "-o",
        "--output",
        help="Output path",
        default="./downloads"
    )

    parser.add_argument(
        "-e",
        "--extension",
        help="Download files with specified extensions",
        default=None,
        nargs="+"
    )

    args = parser.parse_args()

    if not args.url and not args.file:
        return print("Must select either --file or --url.")

    if args.file:
        with open(args.file, "r") as f:
            for url in f:
                download(url, args.output, args.extension)
    else:
        download(args.url, args.output, args.extension)


def download(url: str, download_dir: str, accepted_ext: list[str] | None):
    download_dir += f"/{helpers.thread_name(url)}"

    helpers.check_dir(download_dir)

    for url, name in helpers.get_media(url):
        extension = name.split(".")[1]
        if accepted_ext is None or extension in accepted_ext:
            print(f"Downloading {name}")
            helpers.download_media(url, name, download_dir)

    print("All media downloaded.")


if __name__ == "__main__":
    main()
