#Static site generation script

#bring in utils.py which has necessary functions for site building
import utils

#bring in system functionality
import sys


def main():
	if len(sys.argv) == 1:
		utils.invalid_arg()
	else:
		command = sys.argv[1]
		if command == 'build':
			print("manage.py static site generator - build started")
			tmpl = utils.open_template()
			utils.create_main_pages(tmpl)
		elif command == 'new':
			print("manage.py static site generator - new content add started")
			utils.new_content()
		else:
			utils.invalid_arg()
	print("manage.py static site generator - run complete")


if __name__ == "__main__":
	main()


