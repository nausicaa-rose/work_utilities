import argparse
import xml.dom.minidom as xdm


parser = argparse.ArgumentParser()
parser.add_argument("input_xml")
parser.add_argument("output_xml")

args = parser.parse_args()

with open(args.input_xml, "r", encoding="utf-8") as ifh:
    with open(args.output_xml, "w", encoding="utf-8") as ofh:
        ofh.write(xdm.parseString(ifh.read()).toprettyxml())
