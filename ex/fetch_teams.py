from nhl_data_hub.api import fetch_teams

def main():

    season = "20222023"
    teams = fetch_teams(season)

    if teams:
        print(f"Teams in the season {season}:")
        for team in teams:
            print(f"{team['id']:<2} | {team['name']}")

    else:
        print("No teams found for the specified season.")

if __name__ == "__main__":
    main()