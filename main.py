from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import smtplib
from email.message import EmailMessage
import os
from selenium.webdriver.common.by import By
import time
from zapis import zapis


class zapis:
    def __init__(self, naslov, tekst, link):
        self.naslov = naslov
        self.tekst = tekst
        self.link = link


class zapis_za_slanje:
    def __init__(self, kljucna, naslov, tekst, link):
        self.kljucna = kljucna
        self.naslov = naslov
        self.tekst = tekst
        self.link = link


url = "https://eojn.nn.hr/SPIN/application/ipn/DocumentManagement/NewPreglediDokumenataFrm.aspx/"
service = Service("C:/Users/Komp/PycharmProjects/NarodneNovineZadnji/chromedriver.exe")
chrome_options = Options()

driver = webdriver.Chrome(
    service=service,
    options=chrome_options
)

# Otvori stranicu
driver.get(url)
print("Otvorio stranicu")
time.sleep(3)

# Inicijalizacija varijabli
lista_zapisa = []
brojac = 1
datum = "datum"
lista_za_slanje = []
global brojcanik
brojcanik=0

datum_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/h1/span[1]"

datum = driver.find_element(By.XPATH, datum_xpath).text

brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[1]"

        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[1] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik=brojcanik+1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break

brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[2]"
        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[2] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break
brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[3]"
        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[3] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break
brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[4]"
        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[4] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break
brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[5]"
        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[5] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break
brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[6]"
        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[6] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break
brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[7]"
        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[7] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break
brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[8]"

        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[8] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break
brojac = 1

# def dohvti_naslov (naslov_xpath):


while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[9]"
        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[9] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break
brojac = 1
while brojac < 10:
    try:
        naslov_xpath = "/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/div[1]/ul/li/h2[10]"

        naslov = driver.find_element(By.XPATH, naslov_xpath).text.replace("PlusMinus", "")

        objava_xpath = '/ html / body / form / div[3] / table / tbody / tr / td / div / div[2] / div[1] / ul / li / ul[10] / div / li[' + str(
            brojac) + '] / table / tbody / tr / td[3] / a'

        tekst = driver.find_element(By.XPATH, objava_xpath).text
        link = driver.find_element(By.XPATH, objava_xpath).get_attribute("href").replace(
            "NewPreglediDokumenataFrm.aspx/", "")

        brojac = brojac + 1
        brojcanik = brojcanik + 1

        lista_zapisa.append(zapis(naslov, tekst, link))
    except NoSuchElementException:
        print("Nema takvog elementa!")
        break

print(datum)
for zapis in lista_zapisa:
    print(zapis.naslov + "\n" + zapis.tekst + " ," + zapis.link)

kljucne_rijeci = [
    "geo",
    "Geo",
    "izmjer",
    "Izmjer",
    "Sken",
    "sken",
    "mjer",
    "Mjer",
    "model",
    "Model",
    "3d",
    "3D"
]

for zapis in lista_zapisa:
    for kljucna in kljucne_rijeci:
        if kljucna in zapis.tekst:
            privremeni_zapis = zapis_za_slanje(kljucna, zapis.naslov, zapis.tekst, zapis.link)
            lista_za_slanje.append(privremeni_zapis)

# EMAIL_ADRESS = os.environ.get("python_user")
# EMAIL_PASSWORD = os.environ.get("python_password")

EMAIL_PASSWORD = "ovojenekasifra1!"
EMAIL_ADRESS = "sioslav.send@gmail.com"

poruka = "Nije bilo objava koje sadrže ključne riječi. Ovo je default status poruke koju eventualni match pregazi."

for zapis_za_slanje in lista_za_slanje:
    poruka = poruka + zapis_za_slanje.naslov + "<br>" + "Po kljucnoj rijeci: " + zapis_za_slanje.kljucna + "<br>" + zapis_za_slanje.tekst.replace(str(zapis_za_slanje.kljucna), str("<mark>"+zapis_za_slanje.kljucna+"</mark>")) + ", " + zapis_za_slanje.link + "<br>" + "<br>"

msg = EmailMessage()
msg["Subject"] = "TEST objava javne nabave TEST"
msg["From"] = EMAIL_ADRESS
msg["To"] = EMAIL_ADRESS
msg.set_content(poruka)

msg.add_alternative(
    "<html><body>Broj pregledanih objava: "+ str(brojcanik) +"<br>" + poruka +"</body></html>",
    subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

for zapis_za_slanje in lista_za_slanje:
    print(
        zapis_za_slanje.naslov + "\n" + "Po kljucnoj rijeci: " + zapis_za_slanje.kljucna + "\n" + zapis_za_slanje.tekst,
        zapis_za_slanje.link)

driver.close()
