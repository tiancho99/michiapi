# import csv    

# def print_michi(id, name, description, gif_url=None, **kwargs):
#     print(id, name, description, gif_url)

# with open("instance/michis.csv") as michis_file:
#     michis = csv.DictReader(michis_file)
#     print(list(michis))
# import requests

# swapi = requests.get("http://localhost:8000/api/michis").text
# print(swapi)
import requests

for _ in range(20):


    params = {"format":"json"}

    data = requests.get("http://localhost:8000/api", params=params).text

    print(data)
    print(_)

for _ in range(20):


    params = {"format":"json"}

    data = requests.get("http://localhost:8000/api/michis", params=params).text

    print(data)
    print(_)






    
    
