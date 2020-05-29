import click
import requests
import textwrap
from . import __version__


API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    title = data['title']
    extract = data['extract']

    click.secho(title, fg='green')
    click.secho(textwrap.fill(extract))
