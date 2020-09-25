from typing import Optional

from pydantic import BaseModel, EmailStr, Field

'''
Define the Schema for which data will be based on, which will represent
how data is stored in the MongoDB databse.
This schema will help users send HTTP request with the proper shape to the API
- the type of data to send and how to send it.
Here Pydantic Schema is used for validating data along with serializing
(JSON to Python) and deserializing (Python to JSON).
Note that pydantic does NOT serve as a Mongo shcema validator.
'''


class StudentSchema(BaseModel):
    fullname: str = Field(...)  # "..." means the field is required.
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)  # year should be 1 to 8 inclusive.
    gpa: float = Field(..., le=4.0)  # gpa should be less than 4.0

    # This is a common use case of adding an example that will be shown in the docs.
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "johndoe@example.com",
                "course_of_study": "Computer Science",
                "year": 2,
                "gpa": "3.0",
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    # This is a common use case of adding an example that will be shown in the docs.
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "johndoe@example.com",
                "course_of_study": "Statistics",
                "year": 4,
                "gpa": "4.0",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
