# hier sollen die beautiful-soup funktionen stehen

from bs4 import BeautifulSoup
import requests
import requests.compat


#url = ('https://www.rebuy.de')
#url = ('https://www.gummersbach.de')

# str_var = "Im Datenschutz gefundene Begriffe: "
# gefundene_items = [] 
# nicht_gefundene_items = []

# desired_items = [
#     'Datenschutzhinweis', 'Datenschutzbeauftragt', 'erantwortlich', '6',                #später: Datenbankabfrage
#     '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '77', 
#     'Datenschutzbehörde', 'Aufsichtsbehörde', 'eschwer', 'erarbeitung', 
#     'Cookies', 'GVO', 'Dritt', 'mpfänger', 'erarbeitungszweck', 'echnologie', 
#     'auer', 'öschung', 'ideruf', 'TDDDG', 'BDSG', 'Bundesdatenschutz'
# ]



def search_page_for_desired_link(url, *desired_terms):                     #Seite nach einem bestimmten Link durchsuchen. Bsp: nach 'Datenschutzerklärung' suchen: 
                                                                           #desired_terms sind dabei die Suchbegriffe und url die ausgangs-URL, auf dessen Seite gesucht wird
    page = requests.get(url)                                                #zurück kommt ein soup-element
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



def search_in_soup(soup, desired_items, str_var):                           #innerhalb des soup-elements nutzen werden die schlagwörter gesucht
    print(str_var)  
    gefundene_items = []   #die schlagwörter, welche gefunden werden, werden im return angegeben
    nicht_gefundene_items = []
    for item in desired_items:
        if item in str(soup):
            print(f"Gefunden: {item}")           #items wurden gefunden auf website
            gefundene_items.append(item)
        else:
            print(f"NICHT gefunden: {item}")
            nicht_gefundene_items.append(item)
    return gefundene_items


    soup = search_page_for_desired_link(url, "datenschutz", "datenschutzerklärung", "privacy-policy", "privacy", "policy")

    search_in_soup(soup, desired_items, str_var)


