import requests, bs4, json

base_url = "https://www.codecademy.com"

def get_lang(lang):
    lang_sheets = []
    r = requests.get(base_url + "/resources/cheatsheets/language/" + lang)
    soup = bs4.BeautifulSoup(r.content, "html5lib")
    names = soup.select("div.text__kF2Qrng-d0Lmkb-C93zS5.gamut-1ftoruk-HeadingWrapper.ebumvst1.fontSize_md__xs__2cjvYJ-qGQpQ0N90v2Yrx2")
    conts = soup.select("div.gamut-4fg4xn-Column.e1y0e4q30")
    urls = [x.find("a").get("href") for x in conts]        
    for i in range(len(names)):
        lang_sheets.append({
            "name":names[i].text,
            "url":base_url + urls[i]
        })
    return lang_sheets


def compile_json():
    sheets = {}
    languages = ["html-css", "python", "javascript", "java", "sql", "bash", "ruby", "c-plus-plus", "r", "c-sharp", "php", "go", "swift", "kotlin"]
    for l in languages:
        lang_sheets = get_lang(l)
        sheets[l] = lang_sheets
    with open(r"C:\Users\Public\Desk\Automation\sheets.json", "w") as f:
        tmp = json.dumps(sheets)
        f.write(tmp)

def get_body(url):
    body = ""
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, "html5lib")
    cards = soup.find_all("div", {"class": "reviewCardGrid__3EzDHwkp6X8nlMT6Z_NEMw gamut-15b6f3e-LayoutGrid e10xj1580"})
    for card in cards:
        card_text = ""
        divs = card.find_all("div")
        for div in divs:
            kind = div.get("class")
            if kind == ["reviewCardTitleColumn__mgmCdQAzfZj0jxEM28lw1", "gamut-1bm9l11-Column", "e1y0e4q30"]:
                card_text += "[ " + div.find("h3").text.upper() + " ]\n\n"
            if "reviewCardTextColumn__n4kVVPftRbnZCNDkXYIUj" in kind:
                paragraphs = div.find_all("p")
                for p in paragraphs:
                    card_text += p.text + "\n"
                card_text += "\n"
            if kind == ["gamut-6x0oro-ColorizedContainer", "e1hgti5c0"]:
                card_text += "CODE\n" + div.text + "\nEND CODE\n\n"
        body += card_text + "-----\n"
    if body != "":
        return body, 1
    else:
        return body, 0

def get_sections(url):
    sections = {}
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, "html5lib")
    labels = soup.select("div.cheatSheetLink__1EVzcDyZ5-kJzLDzxJ9LRZ")
    tabs = soup.select("a.e14vpv2g1.gamut-1o2ez3y-ResetElement-Anchor-AnchorBase.e1bhhzie0")
    sections[labels[0].text] = url
    for i in range(len(labels) - 1):
        sections[labels[i + 1].text] = base_url + str(tabs[i].get("href"))
    return sections

def get_full_cheatsheet(url):
    bodies = ""
    sections = get_sections(url)
    for label in sections:
        body = get_body(sections[label])
        if body[1] == 1:
            bodies += body[0]
    return bodies

def main():
    with open(r"C:\Users\Public\Desk\Automation\sheets.json", "r") as f:
        sheets = dict(json.load(f))
        while True:
            try:
                command = input("# ").split()
                if command[0] == "show" or command[0] == "s":
                    if command[1] == "byid" or command[1] == "b":
                        if "." not in command[2]:
                            lang_sheets = sheets[list(sheets.keys())[int(command[2])]]
                            for i, l in enumerate(lang_sheets):
                                n = l["name"]
                                print(f"[{command[2]}.{i}] {n}")
                        else:
                            ids = command[2].split(".")
                            lang_sheet = sheets[list(sheets.keys())[int(ids[0])]][int(ids[1])]
                            name = lang_sheet["name"]
                            url = lang_sheet["url"]
                            spaces = " " * (len(ids[0]) + len(ids[1]) + 4)
                            print(f"[{ids[0]}.{ids[1]}] {name} \n{spaces}{url}")
                            
                    elif command[1] == "all" or command[1] == "a":
                        for i, k in enumerate(sheets):
                            print(f"[{i}] {k}")

                    elif command[1] == "secs" or command[1] == "s":
                        ids = command[2].split(".")
                        lang_sheet = sheets[list(sheets.keys())[int(ids[0])]][int(ids[1])]
                        url = lang_sheet["url"]
                        sections = get_sections(url)
                        for i, label in enumerate(sections):                    
                            print(f"[{ids[0]}.{ids[1]}.{i}] {label}")                    

                elif command[0] == "get" or command[0] == "g":
                    if command[1] == "sec" or command[1] == "s":
                        ids = command[2].split(".")
                        lang_sheet = sheets[list(sheets.keys())[int(ids[0])]][int(ids[1])]
                        url = lang_sheet["url"]
                        sections = get_sections(url)
                        url = sections[list(sections.keys())[int(ids[2])]]
                        body = get_body(url)
                        if body[1] == 1:
                            print(body[0][:-1])
                        else:
                            print("Section unavailable")
                    elif command[1] == "sheet" or command[1] == "a":
                        ids = command[2].split(".")
                        lang_sheet = sheets[list(sheets.keys())[int(ids[0])]][int(ids[1])]
                        url = lang_sheet["url"]
                        cs = get_full_cheatsheet(url)
                        print(cs[:-1])
                elif command[0] == "help":
                    print("show:\n  byid *(.*)\n  all\n  secs *.*\nget:\n  sec *.*\n  sheet *.*.*\nexit")
                elif command[0] == "exit" or command[0] == "e":
                    return
                else:
                    print("Invalid Input")
            except (ValueError, IndexError):
                print("Invalid Input")
main()