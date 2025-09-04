from services.menu import Menu
from init_db import session, db_connected

if db_connected:
    menu = Menu(session)
    menu.test()
else: 
    print("La base de donnée  n'est pas connectée...")