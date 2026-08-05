from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
app = FastAPI()

simulation_state = {
    "tick": "",
    "agents": [],
    "relationships": [],
    "events": []
}


@app.get("/state")
def state():

    with open("simulation_state.json", encoding="utf8") as f:
        return json.load(f)


@app.get("/", response_class=HTMLResponse)
def home():

   with open("viculus_ui.html", encoding="utf8") as f:

        return f.read()