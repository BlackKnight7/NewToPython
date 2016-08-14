# NewToPython

**Demos**: Some easy demos to learn basic skills on Python

**MachineLearning**[https://github.com/BlackKnight7/NewToPython-MachineLearinng]: Some demos for maching learning. 

**BlackHat**[https://github.com/BlackKnight7/NewToPython-BlackHat]: Some hack skills of using python.

## IDE
I've used Pycharm and Vim. You can choose one of them. Or use them both.

if you want to use Pycharm, just go to download from https://www.jetbrains.com/pycharm/ 

And if you want to use Vim, it's not that easy.

Fistly, try to lean some basic form http://coolshell.cn/articles/5426.html

Then, install the python envrionmetn from http://codingpy.com/article/vim-and-python-match-in-heaven/

Don't worried too much, if you met error, please view below:

1. on windows, you met this error when intalling curl: 'mysql' is not recognized as an internal or external command, operable program or batch file. MySQL is that some of the folders that are created and added to the PATH variable upon installing MySQL contain an ampersand (&) character, which breaks when passed as a parameter.
You might find that the C:\Program Files\MySQL\MySQL Server 5.0\bin directory comes after the one with the ampersand in the PATH variable.
The solution in this case is to escape the ampersand with a caret (^), so it is ^&

2. get error when add curl.cmd, the 64 bit machine use path 'mingw64', 32 bit maching use path 'mingw'

3. get error when installing Vundle, try my config file __vimrc in git.

At end, I found it's really hard to debug python on vim. but lucky I found we can use vim in Pycharm:
https://www.jetbrains.com/help/pycharm/2016.1/tutorial-using-vim-editor-emulation-in-pycharm.html

