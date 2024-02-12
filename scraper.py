import requests
from pyquery import PyQuery

## returns html source of page or None if response is not not 200 OK
def get_source(url: str) -> str | None:
    try:
        page = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        print("Timed Out")
    if page.ok:
        return page.text
    else:
        return None

## returns text inside HTML element selected by selector: '.article__content' would select an element with the 
## class 'article__content' and '#title' would select the element with the id 'title'. For more examples, research jQuery selectors
def get_inner_html(page_src: str, jQuery_selector: str) -> str:
    doc = PyQuery(page_src)
    res = doc(jQuery_selector)
    return res.text()

## returns article contents from cnn page source
def get_cnn_article(page_src: str) -> str:
    return get_inner_html(page_src, ".article__content")

## returns article title from cnn page source
def get_cnn_title(page_src: str) -> str:
    return get_inner_html(page_src, ".headline__text")


def main():
    url = "https://www.cnn.com/2024/02/12/europe/trump-comments-reaction-nato-stoltenberg-intl-hnk/index.html"
    page_source = get_source(url)

    print(get_cnn_title(page_source))
    print(get_cnn_article(page_source))

if __name__=="__main__":
    main()