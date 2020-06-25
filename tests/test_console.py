import click.testing
import pytest

from hypermodern_python import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_suceeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
