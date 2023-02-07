from selenium import webdriver
import urllib.parse
import requests
import json





def main():
    profession = ""
    departement = None
    scrap(departement=departement, professionNom=profession)

def scrap(departement, professionNom):
    
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    professionUrl = 'http://annuairesante.ameli.fr/xhr/profession?' + urllib.parse.urlencode({'acte': '', 'term':professionNom})
    profession = requests.get(professionUrl, headers=headers) 
    
    profession = profession.json()[0]  