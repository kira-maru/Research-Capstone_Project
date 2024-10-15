from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
resp = response.text
bs = BeautifulSoup(resp, "html.parser")


class ResearchBrain:
    """Gets data from provided website"""
    def __init__(self):
        self.prices = ""
        self.links = ""
        self.addresses = ""
        self.get_properties()

    def get_properties(self):
        """Gets prices, addresses, links, puts them and returns them as lists"""
        prices = bs.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        self.prices = [price.get_text().replace("/mo", "").split("+")[0] for price in prices if "$" in price.text]

        addresses = bs.find_all(name="address")
        address_pattern = r'\d+ \w+ (Street),?\s*|#|[|]'
        self.addresses = [re.sub(address_pattern, "", address.text).strip().replace("  ", " ") for address in addresses]

        links = bs.find_all(class_="StyledPropertyCardDataWrapper")
        self.links = [link.find('a')["href"] for link in links]

        return self.prices, self.addresses, self.links

