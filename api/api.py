
import requests

from service.user_service import convert_to_user


def get_data_api(url : str):
    try:
        response = requests.get(url)  # Timeout in seconds
        response.raise_for_status()
        return response.json()# Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print('Request failed:', e)

def get_users(n : int):
    users_url = f"https://randomuser.me/api?results={n}"
    return get_data_api(users_url)["results"]


def get_questions(n : int):
    questions_url = f"https://opentdb.com/api.php?amount={n}"
    return get_data_api(questions_url)["results"]
