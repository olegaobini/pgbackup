import sys
import subprocess

POSTGRES_REGEX = '^postgres:\/\/*\/'


def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE), True
    except OSError as err:
        print(f'Error: {err}')
        sys.exit(1)
