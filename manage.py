#Static site generation script

#bring in utils.py which has necessary functions for site building
import utils

#bring in system functionality
import sys


def main():
	print("manage.py static site generator - run started")
	if len(sys.argv) == 1:
		utils.invalid_arg()
	else:
		command = sys.argv[1]
		if command == 'build':
			tmpl = utils.open_template()
			utils.create_main_pages(tmpl)
		elif command == 'new':
			utils.new_content()
		else:
			utils.invalid_arg()
	print("manage.py static site generator - run complete")


if __name__ == "__main__":
	main()


