import curses
import tui_ascii_art

class TUI:
    def __init__(self):
        
        
        self.menu_args = ["Sign Up", "Login", "Exit"]
        self.ascii_art = tui_ascii_art.main_title
        curses.wrapper(self.main)

    def tui_mainmenu_show(self, stdscr, selected_row_idx):
        stdscr.clear()


        height, width = stdscr.getmaxyx()
        for idx, row in enumerate(self.menu_args):
            x = width//2 - len(row) //2
            y = height //2 - len(self.menu_args) + idx
            
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
            

            
            stdscr.refresh()
        # now show ascii at top
            


        stdscr.refresh()



    def main(self, stdscr):


        curses.curs_set(0)  # invis cursor
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.current_row_idx = 0
        self.tui_mainmenu_show(stdscr, self.current_row_idx)
        while True:
            self.key = stdscr.getch()
            stdscr.clear()
            if self.key == curses.KEY_UP and self.current_row_idx > 0:
                self.current_row_idx -=1
            elif self.key == curses.KEY_DOWN and self.current_row_idx < len(self.menu_args) - 1:
                self.current_row_idx +=1

            elif self.key == curses.KEY_ENTER or self.key in [10, 13]:
                stdscr.addstr(0,0, f"You Pressed: {self.menu_args[self.current_row_idx]}")
                stdscr.getch()
                if self.current_row_idx == len(self.menu_args) - 1:
                    break
            self.tui_mainmenu_show(stdscr, self.current_row_idx)

            stdscr.refresh()




textuserinterface = TUI()
