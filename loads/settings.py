import json

with open("settings.json", "r", encoding="utf-8") as settings:
    settings = json.load(settings)
    PrintConsoleField = settings["Print Console Field"]
    
    if PrintConsoleField:
        SnakeLike_o = settings["Snake Like 'o' "]
        FoodLike_f = settings["Food Like 'f' "]
<<<<<<< HEAD

    #print(PrintConsoleField, SnakeLike_o, FoodLike_f)
=======
>>>>>>> 5877d8b1d65de8b3b13bd536017004359b4f2bd9
