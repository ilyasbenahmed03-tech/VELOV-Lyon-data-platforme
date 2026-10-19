import requests
import pandas as pd
BASE = "https://download.data.grandlyon.com/files/rdata/jcd_jcdecaux.jcdvelov"
#infos fixes des stations(nom,position,capacite)
info = requests.get(f"{BASE}/station_information.json").json()
df_info = pd.DataFrame(info["data"]["stations"])
#etat en temps reel (velos dispo, places libres...)
status = requests.get(f"{BASE}/station_status.json").json()
df_status = pd.DataFrame(status["data"]["stations"])

print("Nb stations :", len(df_info))
print("\nColonnes info :", df_info.columns.tolist())
print("\nColonnes status :", df_status.columns.tolist())

#on joint les deux sur station_id 
df = df_status.merge(df_info[["station_id", "name", "lat", "lon", "capacity"]], on="station_id")
print(df[["name", "num_bikes_available", "num_docks_available", "capacity"]].head(10))