import os
from docopt import docopt
import builder
from builder import CFG


def _get_user_input() -> dict:
    """"""
    return docopt(
        doc=open(f'{os.path.dirname(__file__)}/interface.txt', 'r').read(),
        version=CFG.get('version'),
    )


def render() -> None:
    """
    Run command line interface.
    """

    # Get user input.
    uinput: dict = _get_user_input()

    if uinput['build'] and uinput['wheel']:
        builder.build_wheel()

    elif uinput['push'] and uinput['registry']:
        builder.push_registry()

    elif uinput['bump'] and uinput['version']:
        builder.bump_version()

    elif uinput['bump'] and uinput['git']:
        builder.bump_git()

    elif uinput['bump']:
        builder.bump_all()
