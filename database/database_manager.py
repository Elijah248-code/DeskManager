#base de donnée

import sqlite3

class DatabaseManger:

    def __init__(self,db_path : str ="data/daskmanger.bd"):
        self.db = self.db_path 
        self.connexion = sqlite3.connect(self.db_path)
        self.connexion.row_factory = sqlite3.Row
        self.curseur = self.connexion.cursor()
        self.create_tables()
    
    def create_tables(self):
        self.curseur.executescript("""
            CREATE TABLE IF NOT EXISTS employes (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                nom     TEXT    NOT NULL,
                prenom  TEXT    NOT NULL,
                service TEXT    NOT NULL
            );

            CREATE TABLE IF NOT EXISTS materiels (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                type         TEXT    NOT NULL,
                marque       TEXT    NOT NULL,
                modele       TEXT    NOT NULL,
                numero_serie TEXT    NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS attributions (
                id               INTEGER PRIMARY KEY AUTOINCREMENT,
                employe_id       INTEGER NOT NULL,
                materiel_id      INTEGER NOT NULL,
                date_attribution TEXT    NOT NULL,
                FOREIGN KEY (employe_id)  REFERENCES employes(id),
                FOREIGN KEY (materiel_id) REFERENCES materiels(id)
            );
        """)
        self.connexion.commit()

    
