import requests as req

resp = req.get("https://en.wikipedia.org/wiki/Studio_Ghibli")

def get_html(url, params=None, output=None):
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
