
import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

# connectin detail
MONGO_DETAILS = config('MONGO_DETAILS') # TODO: Resolve SSL Certificate Failure Error
print(MONGO_DETAILS)

# create a client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# reference a database "students"
database = client.students

# reference a collection(akin to a table in a rdbms)
student_collection = database.get_collection("students_collection")

# Note: database and student_collection are just references,
# and not actual I/O, neither requires an await expression.
# When the first I/O operation is made, both the db and collection
# will be created if they don't exist already.


# Helper function

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }

# CRUD(Create Read Update Delete) Async Operations in the database via motor:


# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True
