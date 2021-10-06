###########################################################   README:   #####################################################################
# Programma ir izveidota numuru validācijai, lai varētu identificēt numura turētāju / pakalpojumu nodrošinātāju.
# Programma ir uzlabojama, jo pēc vairāk, kā 5 mēģinājumiem īsā laika periodā web lapas (https://www.numuri.lv/default.aspx un https://www.numberingplans.com/?page=analysis&sub=phonenr)
# prasa autorizāciju.

# Daži piemēri ārzemju numuriem, testu veikšanai: (piem. 3726750540 / 4721898055)

#################################################   NUMURU VALIDĀCIJAS PROGRAMMA:   ##########################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

num = input('Ievadiet telefona numuru ar valsts prefiksu, bet bez "+" : ')
num = str(num)


def num_latvija(num):
    url = "https://www.numuri.lv/default.aspx"
    driver.get(url)
    search = driver.find_element_by_id("nusa_id_txtBox_15")
    # search = driver.find_element_by_id("nusa_id_txtBox_9")
    # search = driver.find_element_by_id("nusa_id_txtBox_16") # Mēdz mainīties, ja programma nestrādā ar šo ID parametru jāsāk HTML pārbaude.
    # search = driver.find_element_by_id("nusa_id_txtBox_3")
    search.send_keys(num[3:])
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    html = driver.page_source
    df = pd.read_html(html)
    print(df[0])


def num_world(num):
    try:
        url = "https://www.numberingplans.com/?page=analysis&sub=phonenr"

        driver.get(url)
        search = driver.find_element_by_name("i")
        search.send_keys(num)
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        html = driver.page_source
        df = pd.read_html(html)
        df = df[0]
        df.iat[1, 0] = "Phone number"
        df.iat[1, 1] = f"+{num}"
        df = df.iloc[1:, :]
        print(df)

    except ValueError:
        print(
            'Ir radusies kļūda. Lūdzu ievadiet standartiem atbilstošu telefona numuru ar valsts prefiksu, bet bez "+".'
        )


if num.startswith(str(371)):
    num_latvija(num)
else:
    num_world(num)

driver.quit()
