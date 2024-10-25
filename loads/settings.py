import json

with open("settings.json", "r", encoding="utf-8") as settings:
    settings = json.load(settings)
    PrintConsoleField = settings["Print Console Field"]
    
    if PrintConsoleField:
        SnakeLike_o = settings["Snake Like 'o' "]
        FoodLike_f = settings["Food Like 'f' "]

    print(PrintConsoleField, SnakeLike_o, FoodLike_f)