import requests


def do_quote():
    print("Input the URL of the quote:")
    url = input()
    r = get_quote(url)
    if quote_is_valid(r):
        print(r.json()["content"])
    else:
        print("Invalid quote resource!")


def get_quote(url):
    return requests.get(url)


def quote_is_valid(r):
    # check if request is valid
    if r:
        # check if body is a quote
        if "content" in r.json():
            # quote is valid
            return 1
        else:
            # quote is not valid
            return 0
    else:
        return 0


do_quote()
