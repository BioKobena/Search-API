from fastapi import FastAPI
import uvicorn
from data import (get_all_teams_from_fake_db, get_team_from_fake_db, get_team_by_id)



app = FastAPI()


@app.get("/")

def index():
    return {"message" : "Welcome to F1 2021"}


@app.get("/teams")
def get_teams():
    return get_all_teams_from_fake_db()


#Path parameters
@app.get("/teams/{team}")
def get_team(team: str):
    result = get_team_from_fake_db(team)

    if result is None:
        return f"La Team {team} est inconnue"
    
    return result

#Path parameters with types

@app.get("/teams/id/{id}")
def get_team(team: str):
    result = get_team_by_id(id)

    if result is None:
        return f"La Team {team} est inconnue"
    
    return result

# @app.get("/items")

# def get_items():
#     return [
#         {"id": 1, "name": "item1"},
#         {"id": 2, "name": "item2"},
#         {"id": 3, "name": "item3"},
#         {"id": 4, "name": "item4"},
#     ]


if __name__ =='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)