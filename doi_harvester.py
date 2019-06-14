from crossref.restful import Prefixes

prefixes = Prefixes()

wall = prefixes.works("10.31274").all()

with open("out.json", "w", encoding="utf-8") as fh:
    fh.write("[")
    for w in wall:
        fh.write(f"{w},")
    fh.write("]")
