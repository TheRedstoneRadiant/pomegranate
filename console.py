#External/Internal/Builtin Librarys
import os

#Functions
from consoles.console_data import command_data
from storage.utils import close, clear

try:
	clear("P0megranate Console")
	print("<'info'> for commands")
	while True:
		try:
			cmd = input("> ")
			command_data[cmd.upper()]()
		except KeyError:
			print(f"'{cmd}' is not recognized as command")

except KeyboardInterrupt:
	close(1)