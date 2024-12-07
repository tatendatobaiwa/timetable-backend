from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def  helth_check():
    return " the health check was complete "
