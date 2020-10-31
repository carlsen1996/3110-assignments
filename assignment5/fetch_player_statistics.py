from bs4 import BeautifulSoup
import requests as req
import matplotlib.pyplot as plt
import json
import os
"""
This program will take use a wikipedia article about a season of the NBA playoffs 
and find all the teams in the conference semifinals. Then it will find all the 
players in those teams and rank them after points per game, blocks per game and 
rebounds per game and put it in a bar chart. Then it will save it as a png picture.
"""

def extract_url(url):
    """
    This function will take in a string thats a url and get out the team names and
    save it in a list.

    parameters:
        url (String): A string of a url linking to a season of the NBA playoffs.

    returns:
        team_list (List): A list containing a list of urls to the teams in the semifinals.
    """
    soup = BeautifulSoup(url.text, "html.parser")
    souptable = soup.find('div', {'class': "mw-parser-output"})
    body = souptable.find_all('tbody')
    line = body[5].find_all('tr')
    team_line_arr = [4, 6, 16, 18, 28, 30, 40, 42] #this i counted myself because i dont know how else i would distiguish between the rows
    team_list = []
    for i in team_line_arr:
        column = line[i].find_all('td')[3].a['href']
        name = line[i].find_all('td')[3].a.text
        team_list.append([name, f"https://en.wikipedia.org{column}"])
    return team_list
    
def extract_player_url(team_list):
    """
    This function will take in a list of teams and find all the players playing 
    that year. It will then save all those players and their wikipedia urls to 
    a list.

    parameters:
        team_list (List): A list containining a list of urls to the teams in the semifinals.
    
    returns:
        team_players (Dictionary): A dictionary where the key is the name of the team 
                                   and the values is a list of names of names of players
                                   and their urls.
    """
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
    """
    This function will take in player urls and find their statistics for that year 
    and return them. Its using try because the tables are not all the same and will
    return errors if not handled properly.

    parameters:
        player_url (String): A string of a url of a player.
    
    returns:
        stats (List): A list containing the name of the player and a list of 
                      the required stats in floats.
    """
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
                    ppg = row[12].text.strip("\n")
                    bpg = row[11].text.strip("\n")
                    rbg = row[8].text.strip("\n")
                    stats = [float(ppg), float(bpg), float(rbg)]
                    
            
    except:
        souptable = soup.find('div', {'class': 'mw-parser-output'}).find_all('table')[1]
        for i in range(len(souptable.find_all("tr"))):
            if souptable.find_all("tr")[i].a != None:
                if "2019–20" in souptable.find_all("tr")[i].a["title"] or "2019" in souptable.find_all("tr")[i].a["title"]:
                    row = souptable.find_all('tr')[i].find_all('td')
                    ppg = row[12].text.strip("\n")
                    bpg = row[11].text.strip("\n")
                    rbg = row[8].text.strip("\n")
                    stats = [float(ppg), float(bpg), float(rbg)]

    try:
        if stats == []:
            souptable = soup.find('div', {'class': 'mw-parser-output'}).find_all('table')[3]
            for i in range(len(souptable.find_all("tr"))):
                if souptable.find_all("tr")[i].a != None:
                    if "2019–20" in souptable.find_all("tr")[i].a["title"]:
                        row = souptable.find_all('tr')[i].find_all('td')
                        ppg = row[12].text.strip("\n")
                        bpg = row[11].text.strip("\n")
                        rbg = row[8].text.strip("\n")
                        stats = [float(ppg), float(bpg), float(rbg)]
    except:
        pass
    stats = [name.strip(" (Basketball)"), stats] #strips the extra string describing the name
    return stats

def plot(top_players, typep):
    """
    This function takes in the three top players of each team at a spesific stat and 
    plots it in a bar diagram using pyplot. It saves the png files in the folder 
    NBA_player_statistics.

    parameters:
        top_players (List): This is a list of dictionaries where the keys are the name 
                            of the team and the values are a list of the player name 
                            and a list of the stats.

        typep (String): A string determening what kind of stats the players are sorted
                        after. (ppg, bpg, rbg)
    returns: 
        None
    """

    labels = []
    all_points = []
    for team_stat in top_players:
        for name in team_stat:
            points = []
            for players in team_stat.values():
                for player in players:
                    labels.append(f"{player[0]}")
                    if typep == "ppg":
                        points.append(player[1][0])
                    elif typep == "bpg":
                        points.append(player[1][1])
                    elif typep == "rbg":
                        points.append(player[1][2])
        # for each team, add the points to the bar plot with the team label in order to get teams grouped by color
            all_points.extend(points)
            plt.bar(range(len(all_points) - len(points), len(all_points)), points, label=name)

    plt.xlabel("Players")
    if typep == "ppg":
        plt.ylabel("Points")
    elif typep == "bpg":
        plt.ylabel("Blocks")
    elif typep == "rbg":
        plt.ylabel("Rebounds")
    
    plt.xticks(range(len(all_points)), labels, rotation=90)
    plt.legend(title="Teams:", loc="lower left", bbox_to_anchor=(1, 0))
    plt.tight_layout()
    
    plt.savefig(f"./NBA_player_statistics/players_over_{typep}.png", bbox_inches='tight')

    plt.show()
    plt.close()  
    

def main():
    stats_file = "NBA_player_statistics/stats.json"
    if os.path.exists(stats_file):
        team_players = json.load(open(stats_file))
        print("Loaded stats from file:", stats_file)
    else:

        resp = req.get('https://en.wikipedia.org/wiki/2020_NBA_playoffs')
        team_names = []
        team_list = extract_url(resp)
        team_players = extract_player_url(team_list)

        for team in team_players:
            team_names.append(team)

        for team in team_players:
            stats = []
            for player in team_players[team]:
                stat = extract_player_statistics(player)
                if stat[1] != []: # used to filter out the players that doesnt have stats for that season
                    stats.append(stat)
            team_players[team] = stats

        json.dump(team_players, open(stats_file, 'w'))

    top_players_ppg = []
    top_players_bpg = []
    top_players_rbg = []
    """
    This sorts the players after the spesific stats required
    """
    for team in team_players:
        team_players[team].sort(reverse=True, key=lambda x: x[1][0])
        top_players_ppg.append({team: team_players[team][:3]})

    for team in team_players:
        team_players[team].sort(reverse=True, key=lambda x: x[1][1])
        top_players_bpg.append({team: team_players[team][:3]})

    for team in team_players:
        team_players[team].sort(reverse=True, key=lambda x: x[1][2])
        top_players_rbg.append({team: team_players[team][:3]})

    plot(top_players_ppg, "ppg")
    plot(top_players_bpg, "bpg")
    plot(top_players_rbg, "rbg")


if __name__ == '__main__':
    main()