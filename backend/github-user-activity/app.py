import requests
from events import UserGithubEvents as Github
BASE_URL = 'https://api.github.com/users'

username = input("Ingrese nombre de usuario: ").strip()

url = f"{BASE_URL}/{username}/events"

response = requests.get(url=url)
data = response.json()

try:
    eventsGithub = Github()
    eventsGithub.get_events(data)
    eventsGithub.list_events()

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
except requests.exceptions.ConnectionError:
    print("Error de conexión. Verifica tu conexión a Internet.")
except requests.exceptions.Timeout:
    print("Tiempo de espera agotado. La API tardó demasiado en responder.")
except requests.exceptions.RequestException as err:
    print(f"Error inesperado: {err}")
