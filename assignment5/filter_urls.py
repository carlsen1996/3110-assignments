import re
import requests as req
"""
This program takes a wikipedia article and finds all the links to other wikipedia articles 
inside it and saves it to a file.
"""


def find_urls(url):
    """
    This function takes in a url of a wikipedia article and finds all the links to other 
    wikipedia articles with regex.

    parameters:
        url (String): Takes a string of a url to a wikipedia article
    
    returns:
        matches (List): a list of tuples where the first part of the tuple is a string 
        with a link to the other articles
    """
    resp = req.get(url)
    regex = r'((?<=\")[\w:/.]*(wikipedia.org)?\/wiki\/[\w()/%]+(?=\"|#))' #how this works described in the README
    matches = re.findall(regex, resp.text)
    return matches


def write_f(matches, file):
    """
    This function will take in a list of matches and a file to write the list in to.

    parameters:
        matches (List): A list of tuples that have a string of the url to a new article.
        file (File): A .txt file that will be written to.
    """
    for match in matches:
        if match[0].startswith("/wiki/"):
            file.write(f"https://www.wikipedia.org{match[0]}\n")
        else:
            file.write(f"{match[0]}\n")

matches1 = find_urls("https://en.wikipedia.org/wiki/Nobel_Prize")
matches2 = find_urls("https://en.wikipedia.org/wiki/Bundesliga")
matches3 = find_urls("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup")
file1 = open("./filter_urls/output1.txt", "w+")
file2 = open("./filter_urls/output2.txt", "w+")
file3 = open("./filter_urls/output3.txt", "w+")
write_f(matches1, file1)
write_f(matches2, file2)
write_f(matches3, file3)



