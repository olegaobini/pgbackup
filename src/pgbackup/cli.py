from argparse import ArgumentParser, Action
from pgbackup.storage import s3, local
from pgbackup.pgdump import dump
from io import BytesIO
import sys


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
                        help='How & where to store backup',
                        nargs=2,
                        action=DriverAction,
                        required=True)

    parser.add_argument(
        '--name', help='Name of the backup', nargs=1, action=NameAction, required=False)

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print('Attempting To Contacting Postgress Server')
    output = dump(args.url).communicate()[0]
    print('Successfully Concluded Contact\n')
    backup_handler(args.driver, args.destination,
                   output, name=args.name[0])


def backup_handler(driver, location, dbData, name):
    if name == None:
        name = 'backup'

    try:
        if driver == 's3':
            s3(BytesIO(dbData), location, f'{name}.tar')
        elif driver == 'local':
            with open(f'{location}/{name}.tar', 'w+b') as f:
                print(f'Backing Up Data To: {location}/{name}.tar')
                local(dbData, f)
        else:
            print(f'Invalid Driver "{driver}": (local, s3)')
    except OSError as err:
        print(
            f"OS error occurred trying to open {location}{name}.tar\nError {err}")
        sys.exit(1)
    except Exception as err:
        print(f'Unexpected Error: {err}')
        sys.exit(1)
