#External/Internal/Builtin Librarys
import os

class Console:
	@staticmethod
	def info():
		print("""
-----
<'cd'> -> [ARGVs: 1] -id/username		Switches to specified DM
<'ls'> -> [ARGVs: 0] 				List all DMs
<'rm'> -> [ARGVs: 1] -id/username		Remove a user
<'pwd'> -> [ARGVs: 0] 				List current DM's information
<'whoami'> -> [ARGVs: 0]			Displays your user information
<'mkdir'> -> [ARGVs: 1]	-id/username		Add a friend
<'clear'> -> [ARGVs: 0]				Clear Console
-----
			""")

	def clear() -> None:
		"""Clear Console"""
		os.system("cls") if os.name == "nt" else os.system("clear")