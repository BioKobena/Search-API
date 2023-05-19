from typing import Union

f1_teams = [
    {
        "team": "Mercedes",
        "drivers": ["Lewis Hamilton", "Valtteri Bottas"],
        "engine": "Mercedes",
    },
    {
        "team": "Red Bull Racing",
        "drivers": ["Max Verstappen", "Sergio Perez"],
        "engine": "Honda",
    },
    {
        "team": "Aston Martin",
        "drivers": ["Sebastian Vettel", "Lance Stroll"],
        "engine": "Mercedes",
    },
    {
        "team": "Haas",
        "drivers": ["Nikita Mazepin", "Mick Shumarcher"],
        "engine": "Ferrari",
    },
    {
        "team": "Williams",
        "drivers": ["Geor Russell", "Nicholas Latifi"],
        "engine": "Mercedes",
    },
]



def get_all_teams_from_fake_db() -> list:
    """Rturn a list of F1 teams"""
    return f1_teams




def get_all_teams_from_fake_db(team: str) -> Union[dict, None]:
    for f1_team in f1_teams:
        if f1_team.lower() == f1_team.get("team").lower():
            return f1_team
    return None
