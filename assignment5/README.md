## Assignment 5

### Dependencies
BeautifulSoup from bs4
requests
matplotlib.pyplot
re

### 5.1
To run this program you have to write "python3 requesting_urls.py" in your terminal.
The output is saved in the requesting_urls folder.

### 5.2
To run this program you have to write "python3 filter_urls.py" in your terminal.
The files is saved in the folder filter_urls.

Description of the regex:
((?<=\")[\w:/.]*(wikipedia.org)?\/wiki\/[\w()/%]+(?=\"|#))  
((?<=\")                            # This is a positive lookbehind which finds the start as a "  
    [\w:/.]*                        # This lets all the next characters be a letter, number, _, :, / or . and repeats until next part  
        (wikipedia.org)?            # This finds out if wikipedia.org is there zero or one time  
            \/wiki\/                # This always have to be a part of the string  
                [\w()/%]+           # This lets all the next characters be a letter, number, _, (, ), or % and repeats until next part  
                    (?=\"|#))       # This part is a positive lookahead which means the last part will go until it fins a "

### 5.4
To run this program you have to write "python3 time_planner.py" in your terminal.
The betting slip is saved in the folder datetime_filter.

### 5.5
To run this program you have to write "python3 fetch_player_statistics.py" in your terminal.
The outputs is saved in the folder NBA_player_statistics.