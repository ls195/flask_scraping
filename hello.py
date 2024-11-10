from flask import Flask, render_template, request, redirect, url_for
from functions.functions1 import search_in_soup, search_page_for_desired_link
from functions.functions_db import get_all_from_superior_kat, get_special_column


app = Flask(__name__)					#exporting file name to FLASK_APP variable



@app.route('/')
def hello_world():
	return 'Hello, Peppe8o users!'

@app.route('/show_abfrage')                                     #abfrage anzeigen
def show_abfrage():
    return render_template('abfrage.html')



@app.route('/abfrage_verarbeitung', methods=['POST'])                                             #hier landen die Parameter aus der ersten Abfrage
def abfrage_verarbeitung():
    url = request.form.get('url')
    datenschutz_param = request.form.get('datenschutz')
    if datenschutz_param ==1:
        
        desired_items = get_all_from_superior_kat(1)
        desired_items = get_special_column(desired_items, 4)
        soup=search_page_for_desired_link(url, "datenschutz", "datenschutzerklärung", "privacy-policy", "privacy", "policy")
        gefundene_items=search_in_soup(soup, desired_items, "Im Datenschutz gefunden: ")
        
        return render_template('abfrage_auswertung.html', gefundene_items=gefundene_items)


@app.route('/abfrage')
def test():
    liste=["www.google.de"]
    url=request.args.get('url')
    return render_template('abfrage.html', url=url)



if __name__ == '__main__':              #hierdurch lösst sich der TestServer mittels "python hello.py" starten
    app.run(debug=True)                 #muss hier unten stehen
    
    
    

# @app.route('/process', methods=['POST'])                                        #hier sollen die FOrmularabfragen landen
# def process_form():
#     url = request.form.get('url')
#     datenschutz_param = request.form.get('datenschutz')
#     print(f"url: {url}")
#     print(f"Datenschutzparam: {datenschutz_param}")
#     return redirect(url_for('abfrage_verarbeitung', url=url, datenschutz_param = datenschutz_param))