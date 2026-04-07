#base de donnée

import sqlite3

class DatabaseManager:

    def __init__(self,db_path : str ="data/daskmanger.db"):
        self.db = db_path 
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

        #méthode CRU : create , read , update

        #employé 

    def ajout_employe(self, nom:str, prenom:str ,service:str) ->int:
        """Ajout un nouvel employe a la base donnée"""
        self.curseur.execute(
            "INSERT INTO employes (nom, prenom ,service) VALUES(?,?,?)",(nom, prenom, service)
        )
        self.connexion.commit()
        return self.curseur.lastrowid
    
    def modifier_employe(self,id:int, nom:str, prenom:str, service:str):
         """Modifier un employe"""
         self.curseur.execute(
             "UPDATE employes SET nom=? prenom=? service=? WHERE id=?"
             (nom, prenom, service, id)
        
        )
         self.connexion.commit()


    def suprimer_employe(self, id:int ) ->None:
        """Supprimer un employe"""
        self.curseur.execute("DELETE FROM attributions WHERE employe_id=?", (id))
        self.curseur.execute("DELETE FROM employee WHERE id=?",(id))
        self.connexion.commit()

    

    def get_all_employes(self) ->list: 
        self.curseur.execute("SELECT * FROM employer ORDER BY nom, prenom")
        return self.curseur.fetchall()