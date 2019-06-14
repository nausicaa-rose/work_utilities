from crossref.restful import Prefixes

prefixes = Prefixes()

wall = prefixes.works("10.31274").all()

with open("out.txt", "w", encoding="utf-8") as fh:
    fh.write("doi_md = [\n")
    for w in wall:
        fh.write(f"    {w},\n")
    fh.write("\n]")
