from bs4 import BeautifulSoup
import requests as req
import matplotlib.pyplot as plt

def extract_url(url):
    soup = BeautifulSoup(url.text, "html.parser")
    souptable = soup.find('div', {'class': "mw-parser-output"})
    body = souptable.find_all('tbody')
    line = body[5].find_all('tr')
    team_line_arr = [4, 6, 16, 18, 28, 30, 40, 42]
    team_list = []
    for i in team_line_arr:
        column = line[i].find_all('td')[3].a['href']
        name = line[i].find_all('td')[3].a.text
        team_list.append([name, f"https://en.wikipedia.org{column}"])
    return team_list
    
def extract_player_url(team_list):
    
    team_players = {}
    for team in team_list:
        player_list = []
        team_html = req.get(team[1])
        soup = BeautifulSoup(team_html.text, "html.parser")
        souptable = soup.find('table', {'class': 'toccolours'})
        players = souptable.find('tbody').find_all('tr')[2].find_all('td')[0].find('tbody').find_all('tr')
        
        for player in range(1, len(players)):
            player_url = players[player].find_all('td')[2].a['href']
            player_list.append(f"https://en.wikipedia.org{player_url}")
        team_players[team[0]] = player_list
    return team_players

def extract_player_statistics(player_url):
    stats = []
    player_html = req.get(player_url)
    soup = BeautifulSoup(player_html.text, "html.parser")
    name = soup.find("h1").text
    
    try:
        souptable = soup.find('div', {'class': 'mw-parser-output'}).find_all('table')[2]
        for i in range(len(souptable.find_all("tr"))):
            if souptable.find_all("tr")[i].a != None:
                if "2019–20" in souptable.find_all("tr")[i].a["title"] or "2019" in souptable.find_all("tr")[i].a["title"]:
                    row = souptable.find_all('tr')[i].find_all('td')
                    # print(row[12].text.strip("\n"))
                    ppg = row[12].text.strip("\n")
                    bpg = row[11].text.strip("\n")
                    rbg = row[8].text.strip("\n")
                    stats = [float(ppg), float(bpg), float(rbg)]
                    
                    # print(souptable.find_all("tr")[i].a["title"])
            
    except:
        souptable = soup.find('div', {'class': 'mw-parser-output'}).find_all('table')[1]
        for i in range(len(souptable.find_all("tr"))):
            if souptable.find_all("tr")[i].a != None:
                # print(souptable.find_all("tr")[i].a)
                if "2019–20" in souptable.find_all("tr")[i].a["title"] or "2019" in souptable.find_all("tr")[i].a["title"]:
                    row = souptable.find_all('tr')[i].find_all('td')
                    # print(row[12].text.strip("\n"))
                    ppg = row[12].text.strip("\n")
                    bpg = row[11].text.strip("\n")
                    rbg = row[8].text.strip("\n")
                    stats = [float(ppg), float(bpg), float(rbg)]
                    
                    
                    # print(souptable.find_all("tr")[i].a["title"])
    try:
        if stats == []:
            souptable = soup.find('div', {'class': 'mw-parser-output'}).find_all('table')[3]
            for i in range(len(souptable.find_all("tr"))):
                if souptable.find_all("tr")[i].a != None:
                    # print(souptable.find_all("tr")[i].a)
                    if "2019–20" in souptable.find_all("tr")[i].a["title"]:
                        row = souptable.find_all('tr')[i].find_all('td')
                        # print(row[12].text.strip("\n"))
                        ppg = row[12].text.strip("\n")
                        bpg = row[11].text.strip("\n")
                        rbg = row[8].text.strip("\n")
                        stats = [float(ppg), float(bpg), float(rbg)]
    except:
        pass
    stats = [name.strip(" (Basketball)"), stats]
    return stats


    

    
                
    
    
    



resp = req.get('https://en.wikipedia.org/wiki/2020_NBA_playoffs')

team_list = extract_url(resp)
team_players = extract_player_url(team_list)
for team in team_players:
    team_names.append(team)
    # print(team)

i = 0
for team in team_players:
    stats = []
    for player in team_players[team]:
        stat = extract_player_statistics(player)
        if stat[1] != []:
            stats.append(stat)
        print(stat)
    
    team_players[team] = stats


    
    
top_players_ppg = []
top_players_bpg = []
top_players_rbg = []
for team in team_players:
    team_players[team].sort(reverse=True, key=lambda x: x[1][0])
    top_players_ppg.append({team: team_players[team][:3]})
print(top_players_ppg)
    
print("\n")
for team in team_players:
    team_players[team].sort(reverse=True, key=lambda x: x[1][1])
    top_players_bpg.append({team: team_players[team][:3]})
print(top_players_bpg)
print("\n")
for team in team_players:
    team_players[team].sort(reverse=True, key=lambda x: x[1][2])
    top_players_rbg.append({team: team_players[team][:3]})
print(top_players_rbg)



        
    



    


    
#4 6 16 18 28 30 40 42