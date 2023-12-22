import requests

def get_steam_ids(game_names):
    steam_ids = {}

    for game_name in game_names:
        search_url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
        response = requests.get(search_url)
        app_list = response.json()['applist']['apps']

        # find id with name
        for app in app_list:
            if app['name'].lower() == game_name.lower():
                steam_ids[game_name] = app['appid']
                break

        # if not found
        if game_name not in steam_ids:
            steam_ids[game_name] = None

    return steam_ids

# Example
game_names = [
    "Guilty Gear -Strive-",
    "Wo Long: Fallen Dynasty",
    "Merge & Blade",
    "Soul Hackers 2",
    "Atomic Heart",
    "Shadow Warrior 3: Definitive Edition",
    "Madden NFL 23",
    "SD Gundam Battle Alliance"
]

steam_ids = get_steam_ids(game_names)

# Showing results
for game_name, steam_id in steam_ids.items():
    if steam_id:
        print(f"{steam_id}")
    else:
        print(f"{game_name} not found.")

