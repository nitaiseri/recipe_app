from fastapi import FastAPI, HTTPException
from fastapi import Request, status, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from server_utils import *
import uvicorn
import requests
from data_base.db_maneger import db_manager

app = FastAPI()
app.mount("/client", StaticFiles(directory="client"), name="client")

# Routes

@app.get('/sanity')
def sanity():
    return "OK"

@app.get('/')
def root():
    return FileResponse('./client/index.html')

@app.get("/recipes/{ingredient}")
def get_recipes(ingredient, sensitivity = None):
    raw_recipes = requests.get(f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}")
    try:
        recipes = parse_recipes_data(raw_recipes.json()["results"])
        if sensitivity is not None:
            recipes = filter_by_sensitivity(recipes, sensitivity)
        return recipes
    except:
        if raw_recipes and raw_recipes.status_code == 404:
            raise HTTPException(status_code=raw_recipes.status_code)
        raise HTTPException(status_code=404, detail="Invalid parameters")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000,reload=True)

