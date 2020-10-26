## Assignment 5

### 5.1
To run this program you have to write "python3 requesting_urls.py" in your terminal.

### 5.2
To run this program you have to write "python3 filter_urls.py" in your terminal.

Description of the regex:
((?<=\")[\w:/.]*(wikipedia.org)?\/wiki\/[\w()/%]+(?=\"|#))  
((?<=\")                            # This is a positive lookbehind which finds the start as a "  
    [\w:/.]*                        # This lets all the next characters be a letter, number, _, :, / or . and repeats until next part  
        (wikipedia.org)?            # This finds out if wikipedia.org is there zero or one time  
            \/wiki\/                # This always have to be a part of the string  
                [\w()/%]+           # This lets all the next characters be a letter, number, _, (, ), or % and repeats until next part  
                    (?=\"|#))       # This part is a positive lookahead which means the last part will go until it fins a "

### 5.4
To run this program you have to write "python3 time_planner.py" in your terminal