from argparse import ArgumentParser, Action
import re

POSTGRES_REGEX = '^postgres:\/\/*\/'


class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description='Create backup of postgres database')

    parser.add_argument('url', help='the postgres url')
    parser.add_argument('--driver',
                        help='how & where to store backup',
                        nargs=2,
                        action=DriverAction,
                        required=True)

    return parser
