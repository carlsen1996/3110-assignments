from bs4 import BeautifulSoup 
import requests as req
import re

def extract_events(url):
    table_list = []
    
    soup = BeautifulSoup(url.text, "html.parser")
    souptable = soup.find('table', {"class": 'wikitable plainrowheaders'})
    body = souptable.find('tbody')
    rows = body.find_all('tr')
    for row in rows:
        if row.find('td') != None:
            try:
                dicipline = row.find_all('td')[4].text
                if len(dicipline) > 7:
                    dicipline = row.find_all('td')[3].text
                if row.find_all('td')[4].text == "":
                    dicipline = row.find_all('td')[3].text
            except:
                try:
                    dicipline = row.find_all('td')[1].text

                    if len(dicipline) > 8:
                        dicipline = row.find_all('td')[2].text
                except:
                    pass
            try:
                date = row.find('td', {"align": 'right'}).text
            except:
                pass
            
            if date.startswith('[nb'):
                regex = "^([\[].*[\]])(.*)" # Regex used here to filter out the brackets that came in the string ex: [nb 1]
                date = re.match(regex, date)
                date = date.group(2)
                date = date.strip(" ")
            try:
                venue = row.find_all('td')[3].find_all('a')[1].text
            except:
                try:
                    venue = row.find_all('td')[2].find_all('a')[1].text
                except:
                    try:
                        venue = row.find_all('td')[1].find_all('a')[1].text
                    except:
                        pass
            dicipline = dicipline[:2]
            date = date.strip(" \xa0")
            
           
            table_list.append([date, venue, dicipline])
    return table_list
            
def make_table(table_list):
    f = open("./datetime_filter/betting_slip_empty.md", "w+")
    f.write("Date | Venue | Dicipline | Winner \n")
    f.write("--- | --- | --- | ---\n")
    for row in table_list:
        
        f.write(f"{row[0]} | {row[1]} | {row[2]} | \n")
    



resp = req.get("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup")
resp1 = req.get("https://en.wikipedia.org/wiki/2020%E2%80%9321_FIS_Alpine_Ski_World_Cup")


table_list = extract_events(resp1)
make_table(table_list)

