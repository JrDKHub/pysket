import os
import requests
from bs4 import BeautifulSoup

all_teams_names = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards",
]

# Créer un dossier pour stocker les images si nécessaire
if not os.path.exists("logos"):
    os.makedirs("logos")

for team_name in all_teams_names:
    team_name_formatted = team_name.replace(" ", "-").lower()
    url = f"https://seeklogo.com/{team_name_formatted}-logo-38E3841FE7-seeklogo.com.png"

    # Envoyer une requête HTTP pour récupérer l'image
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Enregistrer l'image sur le système local
        with open(f"logos/{team_name_formatted}.png", "wb") as f:
            f.write(response.content)
    else:
        print(f"Échec de la récupération de l'image pour {team_name}")
