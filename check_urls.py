import argparse

import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url_file")
    parser.add_argument("out_file")
    args = parser.parse_args()

    with open(args.url_file, "r", encoding="utf8") as fh:
        urls = [u.strip() for u in fh]

    checked = []
    for u in urls:
        checked.append((requests.get(u).status_code, u))

    with open(args.out_file, "w", encoding="utf8") as fh:
        for c, u in checked:
            fh.write(f"{c}\t{u}\n")