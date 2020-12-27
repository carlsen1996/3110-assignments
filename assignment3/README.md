## 3.1
To run the first program wc.py you have to first set a path to the directory the file is in. You can do that by writing
`$ export PATH=$PATH:/.../.../...`
in the terminal where the dots are replaced by the path to the directory where the file wc.py is

Then you have to override the normal wc command by setting an alias. Do that by writing
`$ alias wc="wc.py"`
in the terminal.

These command will only work temporarly. To make them permanent you should write them in your .bashrc located in your home directory.

## 3.2
To run this program you have to have both Array.py and test_Array.py in the same folder. You run it with the line `$ pytest`
The Array.py program is automaticly imported in to the test program if they are in the same folder.
It is possible to have them in different folders, but then you have to update your $PYTHONPATH to redirect the path to the file.

I didnt watch the lecture about testing before i was finished with the assignment so i just made all the tests inside one method instead of different for each type of test. I will do that at a later date.
