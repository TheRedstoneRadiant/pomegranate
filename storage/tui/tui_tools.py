#External/Internal/Builtin Librarys
import curses

#Function/Classes
from storage.utils import close

class TuiTOOLS:
	@staticmethod
	def exit():
		curses.endwin()
		close(1)