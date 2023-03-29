import unittest
import sqlite3
import json
import os
# starter code

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


# Creates list of species ID's and numbers
def create_species_table(cur, conn):

    species = ["Rabbit",
    "Dog",
    "Cat",
    "Boa Constrictor",
    "Chinchilla",
    "Hamster",
    "Cobra",
    "Parrot",
    "Shark",
    "Goldfish",
    "Gerbil",
    "Llama",
    "Hare"
    ]

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Species (id INTEGER PRIMARY KEY, title TEXT)")
    for i in range(len(species)):
        cur.execute("INSERT INTO Species (id,title) VALUES (?,?)",(i,species[i]))
    conn.commit()

# TASK 1
# CREATE TABLE FOR PATIENTS IN DATABASE
def create_patients_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS Patients')
    cur.execute('CREATE TABLE "Patients"("pet_id" INTEGER, "name" TEXT, "species_id" INTEGER')

    


# ADD FLUFFLE TO THE TABLE
def add_fluffle(cur, conn):
    cur.execute('INSERT INTO Patients (pet_id, name, species_id) VALUES (?,?,?)', (0, "Fluffle", 0))
    conn.commit()
    

# TASK 2
# CODE TO ADD JSON TO THE TABLE
# ASSUME TABLE ALREADY EXISTS
def add_pets_from_json(filename, cur, conn):
    
    # WE GAVE YOU THIS TO READ IN DATA
    f = open(filename)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)

    # THE REST IS UP TO YOU
    count = 1
    for pet_dict in json_data: 
        id_pet = count
        count += 1
        pet_name = pet_dict["name"]
        species_name = pet_dict["species"]
        cur.execute('SELECT id from Species WHERE title = ?'(species_name))
        id_species = int(cur.fetchone()[0])
        cur.execute('INSERT INTO Patients (pet_id, name, species_id) VALUES (?,?,?)', (id_pet, pet_name, id_species))
    conn.commit()



# TASK 3
# CODE TO OUTPUT NON-AGGRESSIVE PETS
def non_aggressive_pets(aggressiveness, cur, conn):
    lst = []
    cur.execute(f"SELECT name FROM Patients WHERE aggressiveness <= '{value}'")
    for row in cur: 
        lst.append(row[0])
    return lst


def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('animal_hospital.db')
    create_species_table(cur, conn)

    create_patients_table(cur, conn)
    add_fluffle(cur, conn)
    add_pets_from_json('pets.json', cur, conn)
    ls = (non_aggressive_pets(10, cur, conn))
    print(ls)
    
    
if __name__ == "__main__":
    main()

