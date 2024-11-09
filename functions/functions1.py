# hier sollen die beautiful-soup funktionen stehen

from bs4 import BeautifulSoup
import requests
import requests.compat
from colorama import Fore, Style
import json

url = ('https://www.gummersbach.de')


def get_some_page(url, *desired_terms):                     #Seite nach einem bestimmten Link durchsuchen. Bsp: 'Datenschutzerklärung' suchen: 
                                                            #get_some_page('https://www.covestro.com/de/company/covestro-worldwide/deutschland/', 'datenschutz', 'Datenschutz', 'DATENSCHUTZ', 'privacy', 'PRIVACY', 'Privacy')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    for link in soup.find_all('a'):
        link_str = str(link)
   
        if any(word in link_str for word in desired_terms):             #Datenschutz, daten schutz
            print(link_str)
            new_url = link['href']
            if not new_url.startswith('http'):
                new_url = requests.compat.urljoin(url, new_url)
                print(f"Neue URL: {new_url}")
                
                
            new_response = requests.get(new_url)
            new_soup = BeautifulSoup(new_response.text, 'html.parser')
            #print(new_soup)
                         
    return new_soup

    #with open("https://www.rebuy.de"):
    #soup = BeautifulSoup(fp)

get_some_page(url, "datenschutz", "datenschutzerklärung")

print(soup)
