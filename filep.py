import  json
import csv

animes = [["name", "ranking", "genre"],
          ["Attack on titan", "S - Tier","action"],
          ["demon slayer" , "A - Tier", "action"],
          ["horimiya", "S - Tier", "Romance"]]

file_path = "output.csv"

try:
    with open(file_path, "w") as file:

        #json = json.dum()
        #csv = writer = csv.writer()
        writer = csv.writer(file)
        for anime in animes:
            writer.writerow(anime)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("the file already exsists")
