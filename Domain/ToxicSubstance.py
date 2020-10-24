import sqlite3

conn = sqlite3.connect('Navio.db')

def InsertToxicSubstance(toxicSubstanceName, toxicSubstanceQuantity):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO ToxicSubstance (Name, Quantity) VALUES ('{toxicSubstanceName}', '{toxicSubstanceQuantity}');")
    
    conn.commit()

def GetToxicSubstances():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ToxicSubstance;")

    toxicSubstances = []
    for toxicSubstance in cursor.fetchall():
        toxicSubstances.append(str(toxicSubstance))
    return toxicSubstances

def UpdateToxicSubstanceName(substanceId, substanceName):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE ToxicSubstance SET Name = '{substanceName}' WHERE Id = '{substanceId}';")
    
    conn.commit()

def UpdateToxicSubstanceQuantity(substanceId, substanceQuantity):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE ToxicSubstance SET Quantity = '{substanceQuantity}' WHERE Id = '{substanceId}';")
    
    conn.commit()

def UpdateToxicSubstanceQuantityAndName(substanceId, substanceName, substanceQuantity):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE ToxicSubstance SET Quantity = '{substanceQuantity}', Name = '{substanceName}' WHERE Id = '{substanceId}';")
    
    conn.commit()

def DeleteToxicSubstance(toxicSubstanceId):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM ToxicSubstance WHERE Id = '{toxicSubstanceId}';")
    
    conn.commit()