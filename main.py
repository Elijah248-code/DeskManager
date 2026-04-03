#point d'entree de l'application Deskmanger
#Lance la base de donnée et l'interface graphique 

import os 
from database.database_manager import DeskManger 
from ui.main_window import MainWindow

def main():
    os.makedirs("data", exist_ok=True)
    db=DatabaseManger("data/deskmanger")
    app = MainWindow(db)
    app.lancer()
    db.fermer()

if __name__ == "__main__":
    main()

    