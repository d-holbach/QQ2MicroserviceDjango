from pymongo import MongoClient

client = MongoClient()

db = client.qq2
students = db.students

new_students = [{"vorname": "Leah",
                 "nachname": "Maier",
                 "matrikelnummer": 11169396,
                 "studiengang": "mi",
                 "semester": 2,
                 "e-mail": "leah.maier@smail.th-koeln.de"},
                {"vorname": "Alexander",
                 "nachname": "Gersten",
                 "matrikelnummer": 11113456,
                 "studiengang": "ai",
                 "semester": 4,
                 "e-mail": "alexander.gersten@smail.th-koeln.de"}]

result = students.insert_many(new_students)

print(result.inserted_ids)

