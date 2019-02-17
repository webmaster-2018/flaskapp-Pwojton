import sqlite3
from modele import Uczen


def student():
    cur.execute("""
            SELECT * FROM Uczen;
        """)
    wyniki = cur.fetchall()
    for row in wyniki:
            print(row)

def main(args):
    # KONFIGURACJA ####
    baza_nazwa = 'baza'
    con = sqlite3.connect(baza_nazwa + '.db')
    cur = con.cursor()
    ###################
    student()
    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
