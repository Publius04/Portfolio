import os
import json
import subprocess

u = "http://127.0.0.1:1969/web"

class client:
    def __init__(self, inits):
        self.inits = inits

    def is_running(self):
        cmd = "docker ps"
        pipe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        line = pipe.stdout.readline()
        lines = ""

        while True:
            line = pipe.stdout.readline().decode("utf-8")
            if line:
                lines += line
            if not line:
                break

        if lines.find("zotero/translation-server") != -1:
            return True
        return False

    def start_server(self):
        os.system("docker pull zotero/translation-server")
        os.system("docker run -d -p 1969:1969 --rm --name translation-server zotero/translation-server")

    def get_citation(self, url):
        try:
            cmd = f'curl -d "{url}" -H "Content-Type: text/plain" http://127.0.0.1:1969/web'
            pipe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            line = pipe.stdout.readline()
            if line:
                return json.loads(line.decode('utf-8')[1:-1])
        except json.decoder.JSONDecodeError:
            print("The remote document is not in a supported format.")

    def parse_package(self, package):
        check = False
        site = package["url"]

        try:
            if "lastName" in package["creators"][0] and "firstName" in package["creators"][0]:
                authors = ""
                for author in package["creators"]:
                    last = author["lastName"]
                    first = author["firstName"]
                    authors += f"{last}, {first}. "
                name = authors
            elif "name" in package["creators"][0]:
                name = package["creators"][0]["name"] + ". "
        except:
            name = "No name. "
            check = True

        title = package["title"]
        type = package["itemType"]

        if type == "newspaperArticle":
            src = package["publicationTitle"]
        elif type == "blogPost":
            src = package["blogTitle"]
        else:
            src = site[8:site.find("/", 8)]
            check = True

        try:
            t1 = package["date"]
            date = t1[6:7] + "/" + t1[9:10] + "/" + t1[:4]
        except KeyError:
            date = "No date"
            check = True

        t2 = package["accessDate"][:10]
        access_date = t2[6:7] + "/" + t2[9:10] + "/" + t2[:4]

        citation = f"{name}\"{title}\" {src}, {date}. Accessed {access_date} from {site}. [{self.inits}]"

        if check:
            citation += " (Citation incomplete, check site for more info)"

        return citation

    def cite(self):
        while True:
            url = input("Enter url: ")

            if "?" in url:
                url = url[:url.find("?") - 1]

            try:
                package = self.get_citation(url)
                citation = self.parse_package(package)
                print(citation)
            except:
                print("Error") #10 mil iq debugging

            command = input("Continue? [Y/n]: ")

            if command.lower() != 'y':
                self.kill_server()
                break

    def kill_server(self):
        os.system("docker kill translation-server")

def prettify(d):
    parsed = json.loads(d)
    dict = json.dumps(parsed, indent = 4)
    print(dict)

def main():
    inits = input("Enter initials: ")
    c = client(inits)

    command = input("Get citation? [Y/n]: ")

    if command.lower() == 'y':
        if not c.is_running():
            c.start_server()
        c.cite()

main()