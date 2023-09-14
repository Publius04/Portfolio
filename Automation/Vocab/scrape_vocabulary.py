import requests, json, csv, bs4

url = "https://api.pictadicta.com/campaign-games/VP/CU011/CG789/search-cards"

def get_words():
    j = json.loads(requests.get(url).text)
    with open("words.csv", "w", encoding = "utf-8") as f:
        w = csv.writer(f, delimiter = ";")
        for i in range(1557):
            info = j[i]["right_column_info"].lower().replace("\u012b", "I").replace("\u014d", "O").replace("\u0101", "A").replace("\u0113", "E").replace("\u016b", "U").replace("\u0081", "").replace("\u008d", "").replace("\u0233", "Y")
            eng = bs4.BeautifulSoup(info, "html").get_text(" ").replace("I", "ī").replace("O", "о̄").replace("A", "ā").replace("E", "ē").replace("U", "ū").replace("Y", "ӯ").replace("\"", "")
            w.writerow([j[i]["left_column_field"], eng])

def main():
    get_words()

if __name__ == "__main__":
    main()