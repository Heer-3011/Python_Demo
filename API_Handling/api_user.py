import requests 

def fetch_random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response =requests.get(url)
    data= response.json()

    if data["success"] and "data" in data:
        user=data["data"]
        username=user["login"]["username"]
        location=user["location"]["country"]
        return username,location
    else:
        raise Exception("Failed to fetch user data")
    
def main(): 
    try:
        username,country=fetch_random_user()
        print(username)
        print(country)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()