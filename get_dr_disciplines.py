import requests
from lxml import etree


def get_page(page):
    base_URL = "https://lib.dr.iastate.edu"
    r = requests.get("".join([base_URL, page]))
    tree = etree.HTML(r.text)

    return tree


def get_disciplines(tree):
    base_xpath = "//dl[@class='new-discipline']"
    discipline_xpath = "dt/text()"
    sub_disciplines_xpath = "dd[@class='sub-discipline']/a/@href"
    disciplines = tree.xpath(base_xpath)
    collected_disciplines = {}

    for d in disciplines:
        discipline = d.xpath(discipline_xpath)[0]
        sub_disciplines_page = d.xpath(sub_disciplines_xpath)

        if sub_disciplines_page:
            collected_disciplines[discipline] = get_disciplines(get_page(sub_disciplines_page[0]))
        else:
            collected_disciplines[discipline] = {}

    return collected_disciplines


def save_disciplines(disciplines, file_handle, level=0):
    delimiter = "\t"

    for key in disciplines.keys():
        file_handle.write(f"{delimiter * level}{key}\n")
        if disciplines[key]:
            save_disciplines(disciplines[key], file_handle, level=level+1)
   


if __name__ == "__main__":
    base_disciplines_page = "/do/discipline_browser/disciplines"
    out_file = "disciplines.txt"
    disciplines = get_disciplines(get_page(base_disciplines_page))
    with open(out_file, "w", encoding="utf-8") as fh:
        save_disciplines(disciplines, fh)