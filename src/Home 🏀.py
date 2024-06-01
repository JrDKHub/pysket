import streamlit as st
import functions as fn


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

all_teams_logos = [
    "https://seeklogo.com/images/A/atlanta-hawks-logo-A108D0AC8D-seeklogo.com.png"
    , "https://seeklogo.com/images/B/boston-celtics-logo-1FE499BFC3-seeklogo.com.png"
    , "https://seeklogo.com/images/B/brooklyn-nets-logo-1CB3B4713B-seeklogo.com.png"
    , "https://seeklogo.com/images/C/chicago-bulls-logo-8530A1093D-seeklogo.com.png"
    , "https://seeklogo.com/images/C/charlotte-hornets-logo-13FDD46165-seeklogo.com.png"
    , "https://seeklogo.com/images/C/cleveland-cavaliers-logo-6D6834E042-seeklogo.com.png"
    , "https://seeklogo.com/images/D/dallas-mavericks-logo-C72AB730C9-seeklogo.com.png"
    , "https://seeklogo.com/images/D/denver-nuggets-primary-logo-2BFDC23ABD-seeklogo.com.png"
    , "https://seeklogo.com/images/D/detroit-pistons-new-2017-logo-ECAA352E29-seeklogo.com.png"
    , "https://seeklogo.com/images/G/golden-state-warriors-logo-DE064E1F7C-seeklogo.com.png"
    , "https://seeklogo.com/images/H/houston-rockets-logo-1AD80DE2AF-seeklogo.com.png"
    , "https://seeklogo.com/images/I/indiana-pacers-logo-3A75B144DB-seeklogo.com.png"
    , "https://seeklogo.com/images/L/la-clippers-logo-D831C30029-seeklogo.com.png"
    , "https://seeklogo.com/images/L/los-angeles-lakers-logo-805BBEB14F-seeklogo.com.png"
    , "https://seeklogo.com/images/M/memphis-grizzlies-logo-10817A022C-seeklogo.com.png"
    , "https://seeklogo.com/images/M/miami-heat-logo-36DD469E8A-seeklogo.com.png"
    , "https://seeklogo.com/images/M/milwaukee-bucks-logo-1FB6E617D0-seeklogo.com.png"
    , "https://seeklogo.com/images/M/minnesota-timberwolves-logo-4CC6086DA9-seeklogo.com.png"
    , "https://seeklogo.com/images/N/new-orleans-pelicans-logo-67880DAB9E-seeklogo.com.png"
    , "https://seeklogo.com/images/N/new-york-knicks-logo-2864221412-seeklogo.com.png"
    , "https://seeklogo.com/images/O/oklahoma-city-thunder-nba-logo-76BBE35B6A-seeklogo.com.png"
    , "https://seeklogo.com/images/O/orlando-magic-logo-A0B98CF6AF-seeklogo.com.png"
    , "https://images.seeklogo.com/logo-png/53/1/philadelphia-76ers-logo-png_seeklogo-533906.png"
    , "https://seeklogo.com/images/P/phoenix-suns-logo-02E098666B-seeklogo.com.png"
    , "https://seeklogo.com/images/P/portland-trail-blazers-logo-8016836772-seeklogo.com.png"
    , "https://seeklogo.com/images/S/sacramento-kings-logo-8AA2BC70E9-seeklogo.com.png"
    , "https://seeklogo.com/images/S/san-antonio-spurs-logo-48CC3826AE-seeklogo.com.png"
    , "https://seeklogo.com/images/T/toronto-raptors-logo-912C9648B5-seeklogo.com.png"
    , "https://seeklogo.com/images/U/utah-jazz-logo-C13BE7804A-seeklogo.com.png"
    , "https://seeklogo.com/images/W/washington-wizards-logo-A2FF39148C-seeklogo.com.png"
]
st.sidebar.image("assets/img/pysket.png",width=300)
st.sidebar.markdown(f"<h1 style='text-align: center;'>PYSKET</h1>", unsafe_allow_html=True)

team1, versus, team2 = st.columns([0.4, 0.2, 0.4])
st.session_state["logo_default"] = (
    "https://seeklogo.com/images/N/nba-logo-59F0731E03-seeklogo.com.png"
)
logo1 = st.session_state["logo_default"]
logo2 = st.session_state["logo_default"]


home = team1.selectbox(
    label="Choisir l'équipe à domicile",
    options= all_teams_names
    , key="Team1",
)

team_index1 = all_teams_names.index(home)
selected_team_logo = all_teams_logos[team_index1]

if home:
    logo1 = selected_team_logo
team1.image(logo1,width=200)





away = team2.selectbox(
    label="Choisir l'équipe à l'extérieur",
    options=all_teams_names
    , key="Team2"
)
team_index2 = all_teams_names.index(away)
selected_team_logo2 = all_teams_logos[team_index2]

if away :
    logo2 = selected_team_logo2
team2.image(logo2,width=200)


versus.image("https://static.vecteezy.com/ti/vecteur-libre/p3/13212902-signe-vs-ou-versus-symbole-de-competition-vectoriel.jpg")
if versus.button("Simuler la rencontre",type="primary"):
    score_home, score_away = fn.score(home, away)
    if score_home > score_away:
        code1 = "green"
        code2 = "red"
    elif score_away > score_home:
        code2 = "green"
        code1 = "red"
    else :
        code1 = "gray"
        code2 = "gray"
        
    team1.markdown(f"<h1 style='text-align: center; color:{code1};'>{round(score_home)}</h1>", unsafe_allow_html=True)   
    team2.markdown(f"<h1 style='text-align: center;color:{code2};'>{round(score_away)}</h1>", unsafe_allow_html=True)

        
    
    