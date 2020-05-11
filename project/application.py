import sys
from project.controller import Controller


if __name__ == '__main__':
    controller = Controller()

    sys.exit(controller.run())
