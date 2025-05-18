import argparse
import gc
import re
import sys
import time

from bs4 import BeautifulSoup
from func import append_dict_to_csv, get_schema_and_domain, wait_for_string
from seleniumbase import SB


def google_search(query: str):
    with SB(uc=True, test=True, locale="en") as sb:
        sb.open("https://google.com/ncr")
        sb.type('[title="Search"]', f"{query}\n")
        sb.sleep(2)
        response = "starting"
        while response is not None:
            source = sb.get_page_source()
            try:
                output = wait_for_string(source)
                # center_col
                soup = BeautifulSoup(output, "html.parser")
                is_next = soup.find("a", attrs={"id": "pnnext"})
                if is_next is None:
                    response = None
                    continue
                search_results = soup.find_all(
                    "a", class_="zReHs"
                )  # Use the correct class name for Google search results

                domains = []
                for result in search_results:
                    link = result.get("href")
                    title = result.find("h3").text.strip()
                    title = re.sub(r"[^a-zA-Z0-9\s]", "", title)
                    if link:  # Check if link is not None
                        domain = get_schema_and_domain(result.get("href"))
                        domains.append(dict(urls=domain, title=title))
                append_dict_to_csv("output/google.csv", ["urls", "title"], domains)
                sb.click("a#pnnext", timeout=30)
                time.sleep(1)
            except TimeoutError as e:
                print(e)
        gc.collect()
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        nargs="+",
        dest="files",
        help="Dorking or any keywords lists to search",
    )

    args = parser.parse_args()
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        try:
            parser.print_help()
        except ValueError:
            print("No arguments provided.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    if args.files:
        for filename in args.files:
            try:
                with open(filename) as file:
                    for line in file:
                        print(f"Dorking : {line.strip()}")
                        google_search(line.strip())
                        time.sleep(2)
            except FileNotFoundError:
                print(f"Error: File not found: {filename}")


if __name__ == "__main__":
    main()
