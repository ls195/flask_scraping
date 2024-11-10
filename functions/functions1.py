# hier sollen die beautiful-soup funktionen stehen

from bs4 import BeautifulSoup
import requests
import requests.compat
import json

url = ('https://www.gummersbach.de')
str_var = "Im Datenschutz gefundene Begriffe: "
gefundene_items = [] 
desired_items = [
    'Datenschutzhinweis', 'Datenschutzbeauftragter', 'Verantwortliche Stelle', 
    'Rechtsgrundlage', 'Rechtsgrundlage', 'Rechtsgrundlage', 'Rechtsgrundlage', 
    'Rechtsgrundlage', 'Rechtsgrundlage', 'Rechtsgrundlage', 'Rechtsgrundlage', 
    'Rechtsgrundlage', 'Rechtsgrundlage', 'Rechtsgrundlage', 'Rechtsgrundlage', 
    'Datenschutzbehörde', 'Aufsichtsbehörde', 'Beschwerde', 'Datenverarbeitung', 
    'Cookies', 'DSGVO', 'Weitergabe an Drittländer / Di', 'Datenempfänger', 
    'Datenverarbeitungszwecke', 'genutzte Technologie', 'Dauer der Speicherung', 
    'Löschung', 'Wideruf', 'TDDDG', 'BDSG', 'BDSG'
]



def search_page_for_desired_link(url, *desired_terms):                     #Seite nach einem bestimmten Link durchsuchen. Bsp: 'Datenschutzerklärung' suchen: 

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


    #soup = BeautifulSoup(fp)

def search_in_soup(soup, desired_items, str_var):
    print(str_var)
    for item in desired_items:
        if item in str(soup):
            print(f"{item}")           #items wurden gefunden auf website
            gefundene_items.update({item : "gefunden"})
        #else:
         #   print(f"{Fore.RED}{item}{Style.RESET_ALL}")
          #  nicht_gefundene_items.update({item : "nicht_gefunden"})



soup = search_page_for_desired_link(url, "datenschutz", "datenschutzerklärung")

search_in_soup(soup, desired_items, str_var)


print(soup)
