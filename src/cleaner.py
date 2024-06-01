import pandas as pd

def clean_data():
    # lecture du fichier
    with open("src/assets/stats.txt", "r") as file:
        lines = file.readlines()
    
    # réécriture dans le fichier sauf les 5 dernières lignes
    with open("src/assets/stats.txt", "w") as file:
        file.writelines(lines[5:-1])
    
    # ouverture du fichier avec pandas
    df = pd.read_csv("src/assets/stats.txt")
    
    # suppression des colonnes 
    columns_to_drop = ["Unnamed: 22", "Unnamed: 27", "Unnamed: 17"]
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], axis=1, inplace=True)
    df['Team'] = df['Team'].str.replace(r'\*$', '', regex=True)
    
    # génération du fichier csv
    df.to_csv("src/assets/data.csv", index=False)
    print("clean")
    

# activation du nettoyage
cleaned_data = clean_data()
