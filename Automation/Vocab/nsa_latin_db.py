import requests, time, selenium
from selenium import webdriver
from selenium.webdriver.common.by import By






# 1020101200
# 00 titulus: 0132200 mensa: 1
# 10111 rosa: 10103
# 111 via: 1311120 
# ante: 00110001 speculum: 11
# 00111101 gemma: 00
# 110105 panis: 1031
# 020 sol: 1203001
# 212 aer: 0100021
# 11 pullus: 11001104 
# vivus: 100101031 venter: 0
# 0000 sanat: 112000
# 10 scutum: 121121 hostis: 21
# 102022 fossa: 1020
# 001 altus: 3112131
# mane: 40001011 dimidius: 11
# 00111 res: 40020
# 00 togatus: 000200 valet: 12
# 1111 tacitus: 001012
# 1 occidens: 31001010 puppis: 2
# 11010000 veretur: 001
# 100111 oportet: 1111
# 11020201 varius: 11
# 0100122 convenit: 111
# 10102 alit: 00011
# 100 cornu: 0105001
# 11 ait: 00000210 
# ianitor: 000001013 comes: 2
# 0100011110
# 1 rubet: 1

answers = """
1020101100
0001022001
00110001000
1111311120
0011000111
0011110100
1101051031
0201203001
2120100021
1111001104
1001010310
0000112000
1012112121
1020221020
0013112131
4000101111
0011140020
0000020012
1111001012
1310010102
1101000000
1001111111
1100000111
0100100111000
1010000011
10001050001
1100000210
0000010132
0100011110
11""".replace("\n", "")

def words_raw():
    return ['fluvius', 'provincia', 'insula', 'oceanus', 'capitulum', 'oppidum', 'lapis', 'numerus', 'vir', 'sermo', 'multus', 'pensum', 'magnus', 'paucus', 'Graecus', 'femina', 'parvus', 'Romanus', 'imperium', 'quid', 'littera', 'in', 'vocabulum', 'Ubi', 'Latinus', 'puer', 'liberi', 'filia', 'mater', 'filius', 'familia', 'pater', 'puella', 'servus', 'pagina', 'novus', 'domina', 'ancilla', 'titulus', 'dominus', 'antiquus', 'Quae', 'Quis', 'Qui', 'tuus', 'ceteri', 'Cuius', 'Quot', 'meus', 'scaena', 'probus', 'ostium', 'persona', 'improbus', 'iratus', 'canta-t', 'laetus', 'pulsa-t', 'verbera-t', 'plora-t', 'voca-t', 'ride-t', 'venit', 'dormi-t', 'responde-t', 'interroga-t', 'saccus', 'Pecunia', 'vacuus', 'Sacculus', 'Nummus', 'mensa', 'habet', 'baculum', 'Nullus', 'suum', 'ponit', 'saluta-t', 'abes-t', 'sum-it', 'accusa-t', 'time-t', 'impera-t', 'tace-t', 'disced-it', 'ades-t', 'pare-t', 'villa', 'rosa', 'impluvium', 'atrium', 'lilium', 'hortus', 'nasus', 'poculum', 'pulcher', 'Cubiculum', 'foedus', 'fenestra', 'cibus', 'Aqua', 'solus', 'Nihil', 'habita-t', 'carp-it', 'malum', 'ama-t', 'delecta-t', 'ag-it', 'sine', 'ex', 'cum', 'ab', 'via', 'arbor', 'circum', 'i-t', 'porta', 'Murus', 'amica', 'equus', 'veh-it', 'umerus', 'intra-t', 'porta-t', 'inimicus', 'asinus', 'Lectica', 'fessus', 'per', 'ante', 'ad', 'post', 'longus', 'prope', 'procul', 'Quo', 'Unde', 'inter', 'Oculus', 'malum', 'Lacrima', 'pirum', 'tene-t', 'speculum', 'pila', 'canistrum', 'Ostiarius', 'formosus', 'claud-it', 'vertit', 'terge-t', 'plenus', 'caput', 'exspecta-t', 'aperi-t', 'lacrima-t', 'adit', 'exi-t', 'osculum', 'ines-t', 'da-t', 'adveni-t', 'curr-it', 'Anulus', 'Pretium', 'Tabernarius', 'Ornamentum', 'taberna', 'collum', 'orna-t', 'linea', 'pecuniosus', 'Gemma', 'pretiosus', 'margarita', 'vend-it', 'em-it', 'accip(i)-t', 'aspic(i)-t', 'consist-it', 'monstra-t', 'abi-t', 'ostend-it', 'consta-t', 'conveni-t', 'medius', 'clama-t', 'Campus', 'Canis', 'mons', 'panis', 'Pastor', 'Herba', 'vallis', 'Ovis', 'collis', 'umbra', 'Terra', 'lupus', 'caelum', 'sol', 'vestigium', 'Nubes', 'Timor', 'dens', 'niger', 'color', 'albus', 'Silva', 'sub', 'supra', 'clamor', 'es-t', 'duc-it', 'bib-it', 'relinqu-it', 'iace-t', 'luce-t', 'pet-it', 'latra-t', 'reperi-t', 'quaer-it', 'erra-t', 'ulula-t', 'bala-t', 'aer', 'animal', 'piscis', 'bestia', 'deus', 'Anima', 'homo', 'Asinus', 'avis', 'Leo', 'ala', 'petasus', 'flumen', 'pes', 'nuntius', 'Pulmo', 'Nidus', 'ferus', 'Vox', 'Nemo', 'pullus', 'ovum', 'ramus', 'Lectus', 'folium', 'pila', 'mortuus', 'nata-t', 'perterritus', 'move-t', 'vola-t', 'tenuis', 'crassus', 'spira-t', 'cap(i)-t', 'viv-it', 'fac(i)-t', 'vivus', 'par(i)-t', 'ascend-it', 'Necesse', 'occulta-t', 'aude-t', 'cad-it', 'vul-t', 'sustine-t', 'lud-it', 'can-it', 'potes-t', 'Corpus', 'Caput', 'manus', 'membrum', 'bracchium', 'Capillus', 'Os', 'Auris', 'Frons', 'Crus', 'Cerebrum', 'Viscera', 'color', 'Lingua', 'iecur', 'Cor', 'Venter', 'labrum', 'Pectus', 'Sanguis', 'medicus', 'aeger', 'sanus', 'poculum', 'ruber', 'Culter', 'flu-it', 'stultus', 'humanus', 'noster', 'sana-t', 'dic-it', 'iube-t', 'reveni-t', 'tang-it', 'arcess-it', 'sede-t', 'specta-t', 'sta-t', 'aegrota-t', 'dole-t', 'horre-t', 'infra', 'senti-t', 'de', 'gaude-t', 'palpita-t', 'puta-t', 'frater', 'Hasta', 'scutum', 'avunculus', 'arma', 'pilum', 'Nomen', 'soror', 'Miles', 'Gladius', 'Sagitta', 'fines', 'Arcus', 'pars', 'patria', 'Pugnus', 'finis', 'hostis', 'eques', 'pedes', 'bellum', 'Passus', 'tristis', 'Impetus', 'Castra', 'armatus', 'Exercitus', 'Fossa', 'dux', 'Vallum', 'brevis', 'latus', 'barbarus', 'fer-t', 'fortis', 'gravis', 'levis', 'noster', 'vester', 'altus', 'pugna-t', 'iac(i)-t', 'milita-t', 'divid-it', 'contra', 'defend-it', 'fug(i)-t', 'metu-it', 'oppugna-t', 'incol-it', 'Tempus', 'initium', 'Dies', 'Facies', 'Annus', 'Saeculum', 'mensis', 'Nox', 'Mane', 'Vesper', 'Meridies', 'lux', 'Forma', 'Hora', 'luna', 'Aequinoctium', 'Ver', 'Aestas', 'Lacus', 'Hiems', 'Nix', 'Imber', 'Autumnus', 'Glacies', 'clarus', 'dimidius', 'aequus', 'postremus', 'iniquus', 'urbs', 'obscurus', 'appella-t', 'calidus', 'exiguus', 'frigidus', 'operi-t', 'incip(i)-t', 'illustra-t', 'Calceus', 'parens', 'Nihil', 'Tabula', 'Stilus', 'res', 'Gallus', 'Toga', 'dexter', 'clausus', 'Alter', 'apertus', 'Neuter', 'Tunica', 'Vestimentum', 'nudus', 'sinister', 'purus', 'sordidus', 'togatus', 'affer-t', 'omnis', 'cuba-t', 'excita-t', 'indu-it', 'lava-t', 'ger-it', 'merg-it', 'posc-it', 'frige-t', 'sole-t', 'surg-it', 'Uterque', 'vale-t', 'Flos', 'praeter', 'vigila-t', 'Uter', 'vesti-t', 'discipulus', 'tergum', 'ianua', 'magister', 'Sella', 'ludus', 'domus', 'virga', 'Navis', 'malus', 'superior', 'prior', 'tacitus', 'inferior', 'posterior', 'severus', 'verus', 'redd-it', 'redi-t', 'recita-t', 'consid-it', 'lice-t', 'puni-t', 'desin-it', 'Navis', 'Oriens', 'Ventus', 'Occidens', 'Gubernator', 'Nauta', 'Velum', 'Merces', 'Fulgur', 'Fluctus', 'altum', 'Portus', 'locus', 'invoca-t', 'laeta-tur', 'intue-tur', 'interes-t', 'Ora', 'naviga-t', 'lab-itur', 'imple-t', 'Septentriones', 'loqu-itur', 'puppis', 'Tempestas', 'superus', 'contrarius', 'Tonitrus', 'maritimus', 'ater', 'ori-tur', 'serenus', 'occid-it', 'situs', 'proficisc-itur', 'opperi-tur', 'inferus', 'turbidus', 'cona-tur', 'conscend-it', 'complect-itur', 'turba-t', 'cern-it', 'serva-t', 'vere-tur', 'appella-t', 'tranquillus', 'sequ-itur', 'consola-tur', 'fla-t', 'fi-t', 'hauri-t', 'guberna-t', 'iacta-t', 'egred(i)-tur', 'As', 'difficilis', 'incertus', 'responsum', 'certus', 'Denarius', 'absens', 'doctus', 'piger', 'industrius', 'indoctus', 'largus', 'pravus', 'prudens', 'facilis', 'rectus', 'lauda-t', 'interpella-t', 'computa-t', 'largi-tur', 'cogita-t', 'disc-it', 'demonstra-t', 'doce-t', 'nesci-t', 'Oporte-t', 'repon-it', 'sci-t', 'parti-tur', 'prom-it', 'reprehend-it', 'toll-it', 'Quisque', 'Apis', 'Charta', 'Calamus', 'Epistula', 'Lignum', 'materia', 'Papyrus', 'Cera', 'erus', 'mollis', 'Merces', 'durus', 'mendum', 'frequens', 'rarus', 'ferrum', 'impiger', 'animadvert-it', 'add-it', 'iung-it', 'compara-t', 'varius', 'turpis', 'leg-it', 'corrig-it', 'dees-t', 'exaudi-t', 'dicta-t', 'dele-t', 'effic(i)-t', 'prem-it', 'imprim-it', 'intelleg-it', 'significa-t', 'signa-t', 'superes-t', 'adulescens', 'Columna', 'domus', 'dea', 'flos', 'coniunx', 'donum', 'Amor', 'Forum', 'Templum', 'Signum', 'pulchritudo', 'uxor', 'maritus', 'tectum', 'virgo', 'conveni-t', 'mitt-it', 'indignus', 'dives', 'dignus', 'beatus', 'auge-t', 'oscula-tur', 'minuit', 'posside-t', 'ullus', 'remitt-it', 'colloquium', 'Cunae', 'Officium', 'Infans', 'lac', 'Nutrix', 'mulier', 'Gradus', 'sermo', 'Somnus', 'silentium', 'al-it', 'umidus', 'adveh-it', 'alienus', 'care-t', 'colloqu-itur', 'fa-tur', 'dilig-it', 'non vul-t', 'mane-t', 'dece-t', 'cura-t', 'debe-t', 'occurr-it', 'vagi-t', 'perg-it', 'postula-t', 'adversus', 'sile-t', 'revert-itur', 'Bos', 'pugna', 'humus', 'Cruor', 'cornu', 'Genu', 'causa', 'Porcus', 'solum', 'validus', 'mundus', 'Aliquis', 'sordes', 'angustus', 'indignus', 'falsus', 'candidus', 'ai-t', 'cred-it', 'menti-tur', 'muta-t', 'vinc-it', 'dubita-t', 'conspic(i)-t', 'excusa-t', 'cognosc-it', 'narra-t', 'Cardo', 'Lignum', 'Fores', 'Ianitor', 'Limen', 'acced-it', 'aureus', 'Tabellarius', 'ced-it', 'ferox', 'Pallium', 'ferreus', 'admitt-it', 'pell-it', 'morde-t', 'custodi-t', 'arbitra-tur', 'mone-t', 'cave-t', 'deride-t', 'prehend-it', 'rogita-t', 'remove-t', 'retine-t', 'reced-it', 'proced-it', 'rump-it', 'sali-t', 'sin-it', 'scind-it', 'vinci-t', 'solv-it', 'terre-t', 'trem-it', 'Clavis', 'signum', 'Pudor', 'Laus', 'comes', 'promissum', 'factum', 'verbera', 'avert-it', 'planus', 'Funis', 'pallidus', 'vultus', 'integer', 'comita-tur', 'contine-t', 'mere-t', 'debe-t', 'includ-it', 'dimitt-it', 'fate-tur', 'inscrib-it', 'nega-t', 'palle-t', 'perd-it', 'Ob', 'pude-t', 'rubet', 'promitt-it', 'trad-it', 'solv-it']

def words_formated():
    original = words_raw()
    formated_words = []
    special = ["Graecus", "Romanus", "Latinus"]
    weird = ["Ubi", "Quae", "Qui", "Quis", "Quot", "abes-t", "pare-t", "Nihil", "Quo", "adit", "ines-t", "Nemo", "ruber", "dexter", "affer-t", "Ora", "ater", "Quisque", "idem", "al-it", "fa-tur", "nata-t", "par(i)-t", "non vul-t"]

    for w in original:
        if w in weird:
            continue
        elif w in special:
            formated_words.append(w.replace("-", "").replace("(", "").replace(")", ""))
        else:
            formated_words.append(w.replace("-", "").replace("(", "").replace(")", "").lower())

    return formated_words

def get_word_list():
    word_list = []
    url = "https://app.pictadicta.com/login.html"
    driver = webdriver.Chrome()
    driver.get(url)

    usr = driver.find_element(By.ID, "username")
    pwd = driver.find_element(By.ID, "password")

    usr.send_keys("dwynne-nsa")
    pwd.send_keys("tyro")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(10)

    for i in range(94):
        stages = driver.find_elements(By.CSS_SELECTOR, ".list-group-item.theme-lime")
        stages[i].click()
        time.sleep(10)
        
        while driver.current_url != "https://app.pictadicta.com/learner/play.html":
            next_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[3]/div")
            next_button.click()
            # print(driver.current_url)
            time.sleep(1)
            try:
                word = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div/strong").text
                if word != "":
                    word_list.append(word)
            except selenium.common.exceptions.NoSuchElementException:
                print("no word found")
        
        time.sleep(10)
        
    return word_list

def get_bases():
    word_dict = {}
    words = words_formated()
    # words = words[words.index("adulescens"):]

    url = "https://latinwordnet.exeter.ac.uk/"

    bases = []
    special = 0
    for w in words:
        print(w)
        resp = eval(requests.get(url + f"lemmatize/{w}").text)
        if len(resp) > 1:
            print("SPECIAL:", special)
            print(answers[special])
            bases.append(resp[int(answers[special])]["lemma"]["lemma"])
            special += 1
        else:
            bases.append(resp[0]["lemma"]["lemma"])
            
    return bases

def bases():
    return ['fluuius', 'prouincia', 'insula', 'oceanus', 'capitulum', 'oppidum', 'lapis', 'numerus', 'uir', 'sermo', 'multus', 'pensum', 'magnus', 'paucus', 'Graecus', 'femina', 'paruus', 'Romanus', 'imperium', 'quid', 'littera', 'in', 'uocabulum', 'Latinus', 'puer', 'libet', 'filia', 'mater', 'filius', 'familia', 'praecogito', 'puella', 'seruos', 'pagina', 'nouus', 'domina', 'ancilla', 'titulus', 'dominus', 'antiquus', 'tuus', 'ceterum', 'cuius', 'meus', 'scaena', 'probus', 'ostium', 'persono', 'improbus', 'iratus', 'canto', 'laetus', 'pulso', 'uerbero', 'ploro', 'uoco', 'rideo', 'uenio', 'dormio', 'respondeo', 'interrogatum', 'saccus', 'pecunia', 'uacuus', 'sacculus', 'nummus', 'mensum', 'habeo', 'baculum', 'nullus', 'subinde', 'pono', 'saluto', 'sumo', 'accuso', 'timeo', 'impero', 'taceo', 'discedo', 'adedo', 'uillum', 'rosus', 'impluuium', 'atrium', 'lilium', 'hortus', 'nasus', 'poculum', 'pulcher', 'cubiculum', 'foedus', 'fenestro', 'cibus', 'aqua', 'solus', 'habito', 'carpo', 'malum', 'amo', 'delecto', 'ago', 'sine', 'ex', 'cum', 'ab', 'uia', 'arbor', 'circum', 'eo', 'porta', 'murus', 'amica', 'equus', 'ueho', 'umerus', 'intro', 'porto', 'inimicus', 'asinus', 'lectica', 'fessus', 'per', 'ante', 'ad', 'post', 'longus', 'prope', 'procul', 'unde', 'inter', 'oculus', 'malum', 'lacrima', 'pirum', 'teneo', 'speculum', 'pila', 'canistrum', 'ostiarius', 'formosus', 'claudo', 'uerto', 'tergeo', 'plenus', 'caput', 'exspecto', 'aperio', 'lacrimo', 'exeo', 'osculum', 'deiero', 'aduenio', 'curro', 'anulus', 'pretium', 'tabernarius', 'ornamentum', 'taberna', 'collum', 'orno', 'linea', 'pecuniosus', 'gemma', 'pretiosus', 'margarita', 'uendo', 'emo', 'accipio', 'aspicio', 'consisto', 'monstro', 'abeo', 'ostendo', 'consto', 'conuenio', 'medius', 'clamo', 'campus', 'canis', 'mons', 'panis', 'pastor', 'herba', 'uallis', 'ouis', 'collis', 'umbra', 'terra', 'lupus', 'caelum', 'sol', 'uestigium', 'nubes', 'timor', 'dens', 'niger', 'color', 'albus', 'silua', 'sub', 'supra', 'clamor', 'sum', 'duco', 'bibo', 'relinquo', 'iaceo', 'luceo', 'peto', 'latro', 'reperio', 'quaero', 'erro', 'ululo', 'balo', 'aer', 'animal', 'piscis', 'bestia', 'deus', 'anima', 'homo', 'asinus', 'auis', 'leo', 'ala', 'petasus', 'flumen', 'pes', 'nuntius', 'pulmo', 'nidus', 'ferus', 'uox', 'pullus', 'ouum', 'ramus', 'lectus', 'folium', 'pila', 'mortuus', 'perterritus', 'moueo', 'uolo', 'tenuis', 'crassus', 'spiro', 'capio', 'uiuo', 'facio', 'uiuus', 'ascendo', 'necesse', 'occulto', 'audeo', 'cado', 'uolo', 'sustineo', 'ludo', 'cano', 'possum', 'corpus', 'caput', 'manus', 'membrum', 'bracchium', 'capillus', 'os', 'auris', 'frons', 'crus', 'cerebrum', 'uiscera', 'color', 'lingua', 'iecur', 'cor', 'uenter', 'labrum', 'pectus', 'sanguis', 'medicus', 'aeger', 'sanus', 'poculum', 'culter', 'fluo', 'stultus', 'humanus', 'noster', 'sano', 'dico', 'iubeo', 'reuenio', 'tango', 'arcesso', 'sedo', 'specto', 'sto', 'aegroto', 'doleo', 'horreo', 'infra', 'sentio', 'de', 'gaudeo', 'palpito', 'puto', 'frater', 'hasta', 'scutum', 'auunculus', 'arma', 'pilum', 'nomen', 'soror', 'miles', 'gladius', 'sagitta', 'finis', 'arcus', 'pars', 'patria', 'pugnus', 'finis', 'hostis', 'eques', 'pedes', 'bellum', 'passus', 'tristis', 'impetus', 'castra', 'armatus', 'exercitus', 'fossa', 'dux', 'uallum', 'breuis', 'latus', 'barbarus', 'fero', 'fortis', 'grauis', 'leuis', 'noster', 'uester', 'altus', 'pugno', 'iacio', 'milito', 'diuido', 'contra', 'defendo', 'fugio', 'metuo', 'oppugno', 'incolo', 'tempus', 'initium', 'dies', 'facies', 'annus', 'saeculum', 'mensis', 'nox', 'mane', 'uesper', 'meridies', 'lux', 'forma', 'hora', 'luna', 'aequinoctium', 'uer', 'aestas', 'lacus', 'hiems', 'nix', 'imber', 'autumnus', 'glacies', 'clarus', 'dimidius', 'aequus', 'postremus', 'iniquus', 'urbs', 'obscurus', 'appello', 'calidus', 'exiguus', 'frigidus', 'operio', 'incipio', 'illustro', 'calceus', 'parens', 'tabula', 'stilus', 'res', 'gallus', 'toga', 'clausus', 'alter', 'apertus', 'neuter', 'tunica', 'uestimentum', 'nudus', 'sinister', 'purus', 'sordidus', 'togatus', 'omnis', 'cubo', 'excito', 'induo', 'lauo', 'gero', 'mergo', 'posco', 'frigeo', 'soleo', 'surgo', 'uterque', 'ualeo', 'flos', 'praeter', 'uigilo', 'uter', 'uestio', 'discipulus', 'tergum', 'ianua', 'magister', 'sella', 'ludus', 'domus', 'uirga', 'nauis', 'malus', 'superior', 'prior', 'tacitus', 'inferior', 'posterior', 'seuerus', 'uerus', 'reddo', 'redeo', 'recito', 'consido', 'licet', 'punio', 'desino', 'nauis', 'oriens', 'uentus', 'occidens', 'gubernator', 'nauta', 'uelum', 'merces', 'fulgur', 'fluctus', 'altum', 'portus', 'locus', 'inuoco', 'laetor', 'intueor', 'interest', 'nauigo', 'labor', 'impleo', 'septentriones', 'loquor', 'puppis', 'tempestas', 'superior', 'contrarius', 'tonitrus', 'maritimus', 'orior', 'serenus', 'occido', 'sino', 'proficiscor', 'opperior', 'inferus', 'turbidus', 'coniecto', 'conscendo', 'complector', 'turbo', 'cerno', 'seruo', 'uereor', 'appello', 'tranquillus', 'sequor', 'consolor', 'flo', 'fio', 'haurio', 'guberno', 'iacto', 'egredior', 'as', 'difficilis', 'incertus', 'responsio', 'certus', 'denarius', 'absens', 'doceo', 'piger', 'industrius', 'indoctus', 'largus', 'prauus', 'prudens', 'facilis', 'rectus', 'laudo', 'interpello', 'computo', 'largior', 'cogito', 'disco', 'demonstro', 'doceo', 'nescio', 'oportet', 'repono', 'scio', 'partior', 'promo', 'reprehendo', 'tollo', 'apis', 'charta', 'calamus', 'epistula', 'lignus', 'materio', 'papyrus', 'cero', 'erus', 'molle', 'merx', 'durus', 'mendum', 'frequens', 'rarus', 'ferrum', 'impiger', 'animaduerto', 'addo', 'iungo', 'comparo', 'uarus', 'turpis', 'lego', 'corrigo', 'desum', 'exaudio', 'dicto', 'deleo', 'efficio', 'premo', 'imprimo', 'intellego', 'significatum', 'signo', 'supersum', 'adulesco', 'columna', 'domus', 'dea', 'flos', 'coniunx', 'donum', 'amor', 'forum', 'templum', 'signum', 'pulchritudo', 'uxor', 'maritus', 'tectus', 'uirgo', 'conuenit', 'mitto', 'indignandus', 'diues', 'dignus', 'beatus', 'augeo', 'osculor', 'minuo', 'possideo', 'ullus', 'remitto', 'colloquium', 'cunae', 'officium', 'infans', 'lac', 'nutrix', 'mulier', 'gradus', 'sermo', 'somnus', 'sileo', 'umidus', 'adueho', 'alienus', 'careo', 'colloquor', 'diligo', 'maneo', 'deceo', 'curo', 'debeo', 'occurro', 'uagio', 'pergo', 'postulo', 'aduersus', 'sileo', 'reuertor', 'bos', 'pugna', 'humus', 'cruor', 'cornu', 'genu', 'causa', 'porcus', 'solum', 'ualidus', 'mundus', 'aliquis', 'sordido', 'angustus', 'indignandus', 'falsus', 'candidus', 'ait', 'creditum', 'mentior', 'muto', 'uincio', 'dubito', 'conspicio', 'excuso', 'cognosco', 'narratum', 'cardo', 'lignus', 'sum', 'ianitos', 'limen', 'accedo', 'aureus', 'tabellarius', 'cedo', 'ferox', 'pallium', 'ferreus', 'admitto', 'pello', 'mordeo', 'custodio', 'arbitror', 'moneo', 'cauo', 'derideo', 'prehendo', 'rogito', 'remoueo', 'retineo', 'recedo', 'procedo', 'rumpo', 'salio', 'sino', 'scindo', 'uinco', 'soluo', 'terreo', 'tremo', 'clauus', 'signum', 'pudor', 'laus', 'como', 'promissus', 'factus', 'uerbera', 'auerto', 'planus', 'funis', 'pallidus', 'uultus', 'integer', 'comito', 'contineo', 'mereo', 'debeo', 'includo', 'dimitto', 'fator', 'inscribo', 'nego', 'palleo', 'perdo', 'ob', 'pudet', 'rubetum', 'promitto', 'trado', 'soluo']

def sort_bases():
    words = words_formated()
    url = "https://latinwordnet.exeter.ac.uk/"
    nouns, verbs, adjectives, other = [], [], [], []
    
    i = 0
    for w in words:
        resp = eval(requests.get(url + f"lemmatize/{w}").text)
        if len(resp) == 1:
            which = 0
        else:
            which = int(answers[i])
            i += 1
        pos = resp[which]["lemma"]["morpho"][0]

        if pos == "n":
            nouns.append(w)
        elif pos == "v":
            verbs.append(w)
        elif pos == "a":
            adjectives.append(w)
        else:
            other.append(w)

    return nouns, verbs, adjectives, other

def main():
    pass

if __name__ == "__main__":
    main()

# Principle parts for verbs: v1spia--*-, * = conjugation/declension

"""
1:  part of speech

n   noun
v   verb
a   adjective
d   adverb
c   conjunction
r   adposition
p   pronoun
m   numeral
i   interjection
e   exclamation
u   punctuation

2:  person

1   first person
2   second person
3   third person

3:  number

s   singular
p   plural

4:  tense

p   present
i   imperfect
r   perfect
l   pluperfect
t   future perfect
f   future

5:  mood

i   indicative
s   subjunctive
n   infinitive
m   imperative
p   participle
d   gerund
g   gerundive

6:  voice

a   active
p   passive
d   deponent

7:  gender

m   masculine
f   feminine
n   neuter

8:  conjugation / declension

#   1 - 4 / 5

9:  degree

p   positive
c   comparative
s   superlative

"""