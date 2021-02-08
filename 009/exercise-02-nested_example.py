travel_log = {
    "France": {"Cities_visited": ["Paris", "Lille", "Dijon"], "Total_visited": 12},
    "germany": {"Favourities_places": ["Bes", "Tes", "Manga"], "Next_visite" :["Berlin", "Hamburg", "Stuttgart"]},
}

travel_log_nesting = [
    {
        "country": "France",
        "Cities_visited": ["Paris", "Lille", "Dijon"],
        "Total_visited": 12
    },
    {
        "country": "germany",
        "Favourities_places": ["Bes", "Tes", "Manga"], 
        "Next_visite" :["Berlin", "Hamburg", "Stuttgart"]
    },

]

for item in travel_log_nesting:
    print(item)

for key in travel_log:
    print(key)