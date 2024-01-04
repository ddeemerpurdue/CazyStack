from models import Cz_Overview, Cz_Gff

import sqlite3


# def add_overview(file):
    


def place_in_sqlite3(dbcanresults, db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    # cur.execute("CREATE TABLE samples(md5, file, sample_name, project)")
    cur.execute("""
        INSERT INTO samples VALUES
        ('md5_1', 'myfile.txt', 'myfile', 'Results_1')    
    """)
    con.commit()


# place_in_sqlite3('dbcanresults', 'test.db')
