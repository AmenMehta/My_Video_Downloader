from .includes import *


def start():
    init(autoreset=True)
    parser = argparse.ArgumentParser(description="This is the 'url_dump' module!")

    # Here is an example showing how to use arguments in your code
    parser.add_argument("-u", "--url", type=str, help="YouTube link (URL)")
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="File containing YouTube Video URLs (one URL per line)",
    )

    # Accept the URL or Filename from the user
    args = parser.parse_args()

    # If both (URL and Filename) are present, then print an error
    if args.url != None and args.file != None:
        print(Fore.RED + URL_FILE_BOTH_PRESENT)
        quit()
