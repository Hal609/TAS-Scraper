import requests
import pandas as pd

BASE_URL = 'https://tasvideos.org/api/v1'

# Fetch the list of publications
def get_publications():
    response = requests.get(f"{BASE_URL}/publications")
    response.raise_for_status()  # Raises an error if the request failed
    return response.json()

# Fetch details for a specific movie by ID
def get_publication_details(movie_id):
    response = requests.get(f"{BASE_URL}/publications/{movie_id}")
    response.raise_for_status()
    return response.json()

# Example usage:
publications = get_publications()
df = pd.json_normalize(publications)
print(f"Total publications: {len(publications)}")
# print("First publication:", publications[0])

movie_detail = get_publication_details(1)  # Get details for publication with ID = 1
print("Publication #1 details:", movie_detail)