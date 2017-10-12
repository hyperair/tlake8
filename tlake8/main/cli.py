import re
import sys

from flake8.main.cli import main as flake8_main

from tlake8.monkey import patch_flake8


def main():
    patch_flake8()

    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    return flake8_main()


if __name__ == '__main__':
    sys.exit(main())
