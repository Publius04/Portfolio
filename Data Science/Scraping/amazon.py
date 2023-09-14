from requests_html import HTMLSession

base_url = "https://j2store.net"

s = HTMLSession()

page = f"{base_url}/demo/index.php/shop?start=0"
r = s.get(page)
products = r.html.find("div.j2store-single-product")
for p in products:
    link = base_url + p.find("h2 a")[0].attrs["href"]
    item = s.get(link).html.find("div.simple-product")
    print(item)
