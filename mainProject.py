import requests
import json


def get_url(url):
    response = requests.request("GET", url)
    return response


def display_companies(response):
    for company in response.json():
        print(company['name'], company['id'])


def display_queue_times(response):
    print(json.dumps(response.json(), indent=4))
    for land in response.json()["lands"]:
        print(land["name"])
        for ride in land["rides"]:
            print(ride["name"], "wait_time=", str(ride["wait_time"]), "open=", ride["is_open"])


def main():
    # 1) Get the companies
    companies = get_url("https://queue-times.com/parks.json")

    # 2) Display and get the companies from user
    display_companies(companies)
    input_company_id = 16

    # 3) Get the theme parks from the user response
    theme_parks = get_url("https://queue-times.com/parks/" + str(input_company_id) + "/queue_times.json")

    # 4) Display and get the theme parks from user
    display_queue_times(theme_parks)


if __name__ == "__main__":
    main()

Message @ MichaelGerb2150
