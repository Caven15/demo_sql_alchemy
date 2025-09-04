from init_db import session, db_connected

if db_connected:
    print("ici on va pouvoir commencer dialoguer avec la db....")
else: 
    print("La base de donnée  n'est pas connectée...")