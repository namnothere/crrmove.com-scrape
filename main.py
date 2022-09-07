import requests
from bs4 import BeautifulSoup as bs
import csv

BASE_URL = 'https://crrmove.com/agent-roster/?view_all=1'

def get_soup(url):
    r = requests.get(url)
    return bs(r.text, 'html.parser')

def write_to_csv(data):
    with open('data.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def parseAgent(soup: bs):
    phone = soup.find('i', {'class': 'fa fa-mobile'}).next_element.text.strip()
    email = soup.find('i', {'class': 'fa fa-envelope-o'}).next_element.text.strip()
    return phone, email

def parsePage(soup: bs):
    
    table = soup.find_all('div', {'class': 'agent_unit'})
    for agent in table:
        name = agent.find('h4').text
        phone, email = parseAgent(agent)
        # print(name, phone, email)
        write_to_csv([[name, phone, email]])

write_to_csv([['Name', 'Phone', 'Email']])
soup = get_soup(BASE_URL)
parsePage(soup)