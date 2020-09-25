import uvicorn

if __name__ == "__main__":
    # run a uvicorn server on port 8000 and reload on every file change
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
