from fastapi import FastAPI

from app.server.routes.student import router as StudentRouter

app = FastAPI()
app.include_router(StudentRouter, tags=["Student"], prefix="/student")
# The tags are identifiers used to group routes.
# Routes with the same tags are grouped into
# a section on the API documentation.


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome!!!"}
