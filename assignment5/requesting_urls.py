"""
This program will take in a url or parts of a url and get the html for that page. 
It can also optionally take in parameters as part of urls. It will also optionally
make a output file of the html and save it in the requesting_urls folder.  
"""
import requests as req


resp = req.get("https://en.wikipedia.org/wiki/Studio_Ghibli")

def get_html(url, params=None, output=None):
    """
    This function takes in a url and get the html for that page. It can get parameters
    too that will be parts of the url. It can also get in a filename and save the 
    html in a text file

    parameters:
        url (String): Will be a url to a web page.
        params (Dict): A dictionary of some parameters to be concatinated to the url.
        output (String): A string that will be the filename of the output file.

    returns:
        resp (<class 'requests.models.Response'>): A html file
    """
    if url == None:
        print("No url found")
        exit(0)
    if params != None:
        resp = req.get(url, params=params)
    else:
        resp = req.get(url)
    
    if output != None:
        f = open(f"./requesting_urls/{output}.txt", "w+")
        f.write(f"{resp.url}\n\n{resp.text}")
    return resp

url1 = "https://en.wikipedia.org/wiki/Studio_Ghibli"
url2 = "https://en.wikipedia.org/wiki/Star_Wars"
url3 = "https://en.wikipedia.org/wiki/Dungeons_%26_Dragons"
params4 = {'title': 'Main_Page', 'action': 'info'}
params5 = {'title': 'Hurricane_Gonzalo', 'oldid': '83056166'}
url4_5 = "https://en.wikipedia.org/w/index.php"

resp1 = get_html(url1, None, "output1")
resp2 = get_html(url2, None, "output2")
resp3 = get_html(url3, None, "output3")
resp4 = get_html(url4_5, params4, "output4")
resp5 = get_html(url4_5, params5, "output5")
print(type(resp1))
