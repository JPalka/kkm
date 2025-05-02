import datetime
from itertools import batched
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from .ticket import Ticket
import requests

class Api:
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0'
    headers = {'User-Agent': user_agent}

    def __init__(self, client_number, date, config):
        self.client_number = client_number  
        self.date = date
        self.config = config

    def get_tickets(self):
        payload = {'dateValidity': self.date, 'cardType': 'Other', 'customerCode': self.client_number}
        r = requests.get('https://www.kkm.krakow.pl/pl/sprawdz-waznosc-biletow-zapisanych-na-karcie/index,1.html', params=payload, headers=self.headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        tickets_info = soup.find('div', class_="kkm-card")
        if self.config["debug"]:
            print(tickets_info)
        tickets_info.div.extract()
        tickets_info = tickets_info.select("div:not([style])")
        if len(tickets_info) == 1:
            # [<div>Nie znaleziono żadnych biletów</div>]
            print(tickets_info[0].text)
            return([])
        else:
            tickets = list(map(self.parse_ticket_info, batched(tickets_info, 11)))
            return tickets

    def parse_ticket_info(self, ticket_info):
        return Ticket(
                self.extract_value(ticket_info[0]),
                self.extract_value(ticket_info[1]),
                self.extract_value(ticket_info[2]),
                self.extract_value(ticket_info[3]),
                self.extract_value(ticket_info[4]),
                self.extract_value(ticket_info[5]),
                self.extract_value(ticket_info[6]),
                self.extract_value(ticket_info[7]),
                self.extract_value(ticket_info[8]),
                self.extract_value(ticket_info[9]),
                self.extract_value(ticket_info[10])
                )
        return ticket_info.text

    def extract_value(self, value):
        return value.b.string


