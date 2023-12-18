import random
import requests
import json
from bs4 import BeautifulSoup
from typing import List


class JsonGen:
    """
    Class used to generate a json data to use in testing.
    The json data will have the fields:
    name, age, hobby, city
    """

    # Include your user agent here or let the default.
    USER_AGENT = """Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)\
    Gecko/20100101 Firefox/15.0.1"""
    # Constants to represent the dictionary keys.
    NAME = "name"
    HOBBY = "hobby"
    CITY = "city"

    # Constants to represent the dictionary values.
    URL = "url"
    SELECTOR = "selector"
    DATA = "data"

    # Default name of the output file.
    JSON_FILE = "output.json"

    def __init__(self):
        # The json_fields dictionary will have the information to help to get the json data.
        # The self.URL in the dictionary will be used to get the webpage, and the self.SELECTOR will
        # be used create a list with the tag informations.
        # After that, the tag list will be used to mount the json file.
        self.json_fields = {
            self.NAME: {
                self.URL: "https://en.wikipedia.org/wiki/List_of_most_popular_given_names",
                self.SELECTOR: ".wikitable > tbody > tr > td > a"
            },
            self.HOBBY:
                {self.URL: "https://simple.wikipedia.org/wiki/List_of_hobbies",
                 self.SELECTOR: ".div-col > ul > li > a"
                 },
            self.CITY:
                {self.URL: "https://en.wikipedia.org/wiki/List_of_largest_cities",
                 self.SELECTOR: "table > tbody > tr > th > a"
                 },
        }

    def get_html_page(self, item_type: str) -> str:
        """
        Makes a get request and returns the html page.

        :param item_type: the dictionary key in self.json_fields.
        return: a string represents the html page.
        """
        # Custom agent that will be used in the get request.
        custom_header = {
            "user-agent": self.USER_AGENT
        }
        url = self.json_fields[item_type][self.URL]
        print(f"\n[+] Trying to get the page {url}")
        response = requests.get(url, headers=custom_header)
        print("[+] Page got!\n")
        return response.text

    def get_tag_info(self, soup: BeautifulSoup, item_type: str) -> List[str]:
        """
        Uses the soup object to extract the tag information using the selector in self.json_fields[item_type][self.SELECTOR].

        :param soup: BeautifulSoup object to parse the html tags.
        :param item_type: a key representing an item in the dictionary self.json_fields.
        return: a list of all items in the that matches the css selector.
        """

        print(f"\n[+] Extracting tags for the {item_type}...")
        tag_list_obj = soup.select(self.json_fields[item_type][self.SELECTOR])
        tag_list_text = [tag.getText() for tag in tag_list_obj]
        print(f"[+] Tag information extracted\n")
        return tag_list_text

    def mount_json_data(self) -> None:
        """
        Get all the necessary information to mount the json file using self.json_fields items.
        return: None.
        """
        print("\n[+] Getting all information...")
        # Loop through each key of the dictionary.
        # Each key in the dictionary represents an item that the json file will have.
        for key in self.json_fields:
            # Get the html page in the site specified in self.json_fields[key][self.URL]:
            html_page = self.get_html_page(key)
            # Make a soup object to parse the html page and extract a list of tags.
            soup = BeautifulSoup(html_page, "html.parser")
            # Extract the tag information in the html.
            self.json_fields[key][self.DATA] = self.get_tag_info(soup, key)

        # TODO: Improve the finding of cities.
        # Remove information that is not a valid city in the city data.
        aux_list = self.json_fields[self.CITY][self.DATA]
        self.json_fields[self.CITY][self.DATA] = aux_list[4:-10]
        print("[+] All information got\n")

    def write_json_file(self, data: str) -> None:
        """
        Writes a json file containing data.

        :param data: a string representing the json data.
        :return: None.
        """
        print(f"\n[+] Writing the json file {self.JSON_FILE}")
        with open(self.JSON_FILE, "w") as output_file:
            output_file.write(f"{data}\n")
        print(f"[+] Json file created\n")

    def get_json_data(self) -> str:
        """
        Creates a json using the information in self.json_fields.

        return: a json string with random values for testing.
        """
        json_lines = int(input("Enter the number of lines that the json must have: "))
        object_list = []
        print(f"\n[+] Creating the json...")
        for _ in range(json_lines):
            # Get random values to fill the json fields.
            random_name = random.choice(self.json_fields[self.NAME][self.DATA])
            random_age = random.randint(16, 80)
            random_hobby = random.choice(self.json_fields[self.HOBBY][self.DATA])
            random_city = random.choice(self.json_fields[self.CITY][self.DATA])

            json_dict = {
                "name": random_name,
                "age": random_age,
                "hobby": random_hobby,
                "city": random_city
            }
            object_list.append(json_dict)
        # Transform the dictionary in a valid json.
        return json.dumps(object_list)

    def main(self):
        self.mount_json_data()
        json_data = self.get_json_data()
        self.write_json_file(json_data)


if __name__ == "__main__":
    json_gen_obj = JsonGen()
    json_gen_obj.main()








