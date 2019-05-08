import os

from project import create_app


application = create_app(os.env)


if __name__ == '__main__':
    application.run()
