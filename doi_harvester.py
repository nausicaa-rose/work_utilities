"""Download all Iowa State-generated DOIs from Crossref."""

from time import sleep

import requests

offset = 0
total_records = 38204

out_file = "crossref_metadata_json.txt"

while offset < total_records:
    print(offset)
    url = f"https://api.crossref.org/prefixes/10.31274/works?offset={offset}"
    r = requests.get(url)

    if r.ok:
        with open(out_file, "a", encoding="utf-8") as fh:
            fh.write(r.text)
        offset +=20
    else:
        print(r.status_code)
    # We've got a lot records, so let's play nice and not blast the API
    # with 1,910 requests over just a minute or two.
    sleep(5)
