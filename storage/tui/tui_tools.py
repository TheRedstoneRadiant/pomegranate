# External/Internal/Builtin Librarys
import curses
import webbrowser

# Function/Classes
from storage.utils import close


class TuiTOOLS:
    @staticmethod
    def Exit():
        curses.endwin()
        close(1)

    
    def SignUp():
        webbrowser.open("google.com")

    def Login():
        webbrowser.open("duckduckgo.com")
