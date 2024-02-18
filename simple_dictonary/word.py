import requests
import json

# constand
API = "https://api.dictionaryapi.dev/api/v2/entries/en/"



def query(word):
    req = requests.get(API + word)
    return req

def main() -> None:
    rsps = requests.get(API + "world").json()
    # print(json.loads(rsps))
    # print(rsps.json() == json.loads(rsps.text)) # True
    print(rsps[0]["meanings"])

if __name__ == "__main__":
    main()