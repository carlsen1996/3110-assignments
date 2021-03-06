from bs4 import BeautifulSoup 
import requests as req
import re

"""
This program takes a wikipedia article with a table and takes out the date, venue and 
dicipline and makes a markdown table out of it. This table will be used for betting and 
has a winner colums that you can fill inn yourself
"""

def extract_events(url):
    """
    This function takes in a url for a wikipedia article with a table and makes a list of 
    all the dates, venues and diciplines out of the html.

    parameters:
        url (String): This is a string of a url for a wikipedia article
    
    returns:
        table_list (List): This is a list of lists where the inner list have three elements 
                           which are date, venue and dicipline
    """
    table_list = []
    
    soup = BeautifulSoup(url.text, "html.parser")
    souptable = soup.find('table', {"class": 'wikitable plainrowheaders'})
    captions = get_captions(souptable)
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
            dicipline = captions.get(dicipline[:2], dicipline)
            date = date.strip(" \xa0")
            
           
            table_list.append([date, venue, dicipline])
    return table_list

def get_captions(table):
    """
    Take a bs4 table as input, returning a dictionary of discipline codes mapped to discipline names

    parameters:
        table (bs4.element.Tag): Table containing the captions

    returns:
        dict: Dictionary mapping discipline codes to names
    """
    captions = table.find('caption')
    if not captions:
        return

    captions = captions.text
    #print(captions)

    # find captured group containing 2 uppercase letters, followed by whitespace, '-' and more whitespace
    # then another captured group that contains one or more non-capturing group of one word
    # (several letters followed by non-greedy whitespace), ending on a comma or end of line
    pattern = r"([A-Z]{2})\s–\s((?:\w+\s??)+?)(?:,|$)"
    #print (re.findall(pattern, captions))
    res = {match[0]: match[1] for match in re.findall(pattern, captions)}
    #print(res)
    return res

            
def make_table(table_list):
    """
    This function takes in a list of lists of elements and makes a table which can be 
    read with the markdown formating language.

    parameters:
        table_list (List): This is a list of lists where the inner list have three elements 
                           which are date, venue and dicipline
    """
    f = open("./datetime_filter/betting_slip_empty.md", "w+", encoding='utf-8')
    f.write("Date | Venue | Dicipline | Winner \n")
    f.write("--- | --- | --- | ---\n")
    for row in table_list:
        
        f.write(f"{row[0]} | {row[1]} | {row[2]} | \n")
    

def main():
    resp = req.get("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup")
    resp1 = req.get("https://en.wikipedia.org/wiki/2020%E2%80%9321_FIS_Alpine_Ski_World_Cup")


    table_list = extract_events(resp1)
    make_table(table_list)


if __name__ == '__main__':
    main()
