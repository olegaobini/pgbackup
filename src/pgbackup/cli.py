from argparse import ArgumentParser, Action


class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination


class NameAction(Action):
    def __call__(self, parser, namespace, name, option_string=None):
        namespace.name = name


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description='Create backup of postgres database')

    parser.add_argument('url', help='the postgres url')

    parser.add_argument('--driver',
                        help='how & where to store backup',
                        nargs=2,
                        action=DriverAction,
                        required=True)

    parser.add_argument(
        '--name', help='the name of the backup', nargs=1, action=NameAction, required=False)

    return parser
