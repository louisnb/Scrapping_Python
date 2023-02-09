from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


session = requests.Session()



def scrap():
    
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    
    data = []
    
    
    payload = {
    "type": "ps",
    "ps_profession": "34",
    "ps_profession_label": "Médecin généraliste",
    "ps_localisation": "HERAULT (34)",
    "localisation_category": "departements",
}
    url = "http://annuairesante.ameli.fr/recherche.html"
    page = session.post(url)
   
    soup = BeautifulSoup(page.content, "html.parser")
    medecins = soup.find_all('div', class_='item-professionnel-inner')
    
    for medecin in medecins:
            medecinNom = medecin.find('h2').text.strip() 
            medecinNum_div = medecin.find('div', class_='item left tel')
            if medecinNum_div:
                numero = medecinNum_div.text.strip()
            else:
                numero = None
            medecinAdresse = medecin.find('div', class_='item left adresse').text.strip() 
            medecinAdresse_finale = ', '.join(re.split(r'(\d+)', medecinAdresse))
            
            data.append([medecinNom, numero, medecinAdresse_finale])

    session.post(url, headers=headers, params=payload)


    dataCsv = pd.DataFrame(data, columns=['Nom', 'Numéro', 'Adresse'])
    dataCsv.to_csv("medecins.csv", encoding='UTF-16', columns=['Nom', 'Numéro', 'Adresse'])
    



scrap()