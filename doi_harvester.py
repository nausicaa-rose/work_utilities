"""Download all Iowa State-generated DOIs from Crossref."""

from time import sleep

import requests

# total_records: 38204

cursor = "*"

out_file = "crossref_metadata_json.json"

with open(out_file, "w", encoding="utf-8") as fh:
    fh.write("[")

while True:
    print(cursor)
    url = f"https://api.crossref.org/prefixes/10.31274/works?cursor={cursor}"
    r = requests.get(url)

    if r.ok:
        with open(out_file, "a", encoding="utf-8") as fh:
            fh.write(f"{r.text},")

        cursor = r.json()["message"]["next-cursor"]

        if len(r.json()["message"]["items"]) < 20:
            print("Done!")
            break

    else:
        print(r.status_code)
        print(r.text)
        break
    
    sleep(2)

with open(out_file, "a", encoding="utf-8") as fh:
    fh.write("]")
