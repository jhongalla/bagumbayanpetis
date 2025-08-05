import sqlite3

def connection():
    db=sqlite3.connect('./db/data.sqlite')
    return db


def create_table():
    db=connection()
    try:
        cur=db.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS PETS(
                    [PET_NO] INTEGER PRIMARY KEY NOT NULL UNIQUE,
                    [PET_NAME] TEXT NOT NULL,
                    [PET_TYPE] TEXT NOT NULL,
                    [PET_SEX] TEXT NOT NULL,
                    [PET_AGE] INTEGER,
                    [PET_BREED] TEXT,
                    [PET_COLOR] TEXT NOT NULL,
                    [PET_BIRTHDAY] REAL,
                    [PET_OWNER] TEXT NOT NULL,
                    [PET_ADDRESS] TEXT,
                    [PET_BARANGAY] TEXT NOT NULL,
                    [PET_CONTACT_NO] TEXT
                    )""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS VACCINE(
                    [ID] INTEGER PRIMARY KEY AUTOINCREMENT,
                    [PET] INTEGER NOT NULL,
                    [DATE_VACCINE] REAL NOT NULL,
                    [VACCINE] TEXT NOT NULL,
                    [LOTNO] TEXT NOT NULL,
                    [DATE_NEXT_VACCINE] REAL,
                    [VET_LIC_NO] TEXT,
                    FOREIGN KEY("PET")REFERENCES PETS("PET_NO") ON DELETE CASCADE
                    )""")
    except:
        db.rollback()
    db.commit()

def insert_pet(data):
    db=connection()
    try:
        cur=db.cursor()
        cur.execute("""INSERT INTO PETS(
                    PET_NO,PET_NAME,PET_TYPE,PET_SEX,PET_AGE,PET_BREED,PET_COLOR,PET_BIRTHDAY,PET_OWNER,PET_ADDRESS,PET_BARANGAY,PET_CONTACT_NO)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                    """,(data))
        return str('Data Successfully Save')
    except Exception as e:
        return str(e)
def sql_entry(typ,sql):
    db=connection()
    cur=db.cursor()
    try:
        if typ=='insert':
            cur.execute(sql)
            db.commit()
        elif typ=='query':
            cur.execute(sql)
            rw=cur.fetchall()
            return rw
        else:
            db.rollback()
    except Exception as e:
        db.rollback()
        return e    
create_table()
connection()