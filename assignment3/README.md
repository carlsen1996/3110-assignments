## 3.1
To run the first program wc.py you have to first set a path to the directory the file is in. You can do that by writing
- export PATH=$PATH:/.../.../...
in the terminal where the dots are replaced by the path to the directory where the file wc.py is

Then you have to override the normal wc command by setting an alias. Do that by writing
- alias wc="wc.py"
in the terminal.

These command will only work temporarly. To make them permanent you should write them in your .bashrc located in your home directory.

