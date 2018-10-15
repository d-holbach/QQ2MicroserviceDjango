from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.qq2
students = db.students

for student in students.find():
  pprint.pprint(student)