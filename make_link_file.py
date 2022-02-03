import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("path")
    args = parser.parse_args()

    contents = f'<!DOCTYPE HTML><html><head><script>window.location.href = "{args.url}"</script></head><body></body></html>'

    with open(args.path, "w", encoding="utf8") as fh:
        fh.write(contents)

main()