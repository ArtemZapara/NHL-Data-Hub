import requests

from nhl_data_hub.config import BASE_URL

def fetch_teams(season):
    """
    Fetches a list of teams for the specified season from the NHL API.

    Args:
        season (str): The season in the format "YYYYYYYY" (e.g., "20222023").

    Returns:
        list: A list of team objects containing team information.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the API request.
    """
    url = f"{BASE_URL}/teams?season={season}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["teams"]
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data from {url}:", str(e))
        return []