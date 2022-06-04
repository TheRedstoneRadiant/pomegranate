#External Librarys
import subprocess, threading, os

#Internal Librarys
from storage.utils import clear, close
from storage.exception import CustomError

class Pomegranate:
	@staticmethod
	def console() -> None:
		os.system('start python console.py')

	def main(argv=None):
		try:
			while True:
				input("Message: ")

		except CustomError:
			return
		except KeyboardInterrupt:
			close(1)

if __name__ == '__main__':
	p0m = Pomegranate()
	while True:
		clear("P0megranate")
		console_thread = threading.Thread(target=Pomegranate.console()).start()
		p0m.main()