import mysql.connector

def get_all_from_superior_kat(superior_kat_id):
    superior_kat_id = superior_kat_id
    try:
        # Verbindung zur MariaDB-Datenbank aufbauen
        db = mysql.connector.connect(
            host="localhost",         # Der Host (localhost für lokale Verbindung)
            user="root",              # Der Benutzername (standardmäßig 'root' in XAMPP)
            password="",              # Das Passwort (standardmäßig leer in XAMPP)
            database="ap_db_1",  # Der Name der Datenbank
            port=3307                 # Der Port, Standard ist 3306
        )

        # Cursor erstellen, um Abfragen auszuführen
        cursor = db.cursor()

        # Beispielabfrage ausführen
        cursor.execute(f"SELECT * FROM desired_items where superior_kat_id = { superior_kat_id }")

        # Ergebnisse abrufen
        result = cursor.fetchall()
        for row in result:
            print(row)

        # Verbindung und Cursor schließen
        cursor.close()
        db.close()
        return result

    except mysql.connector.Error as err:
        print(f"Fehler: {err}")
        

def get_special_column(table, column):
    values = [item[column] for item in table]
    return values

desired_items=get_all_from_superior_kat(1) 
print(get_special_column(desired_items, 4))
