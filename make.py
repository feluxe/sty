import shutil
import os
import subprocess as sp
from cmdi import print_summary
from buildlib import buildmisc, git, wheel, project, yaml
from docopt import docopt
from sty import fg
import prmt

interface = """
    Install:
        pipenv install
        pipenv run python make.py

    Usage:
        make.py build wheel [options]
        make.py build docs [options]
        make.py deploy [options]
        make.py test [options]
        make.py bump [options]
        make.py git [options]
        make.py -h | --help

    Options:
    -h, --help               Show this screen.
"""

proj = yaml.loadfile('Project')


class Cfg:
    version = proj['version']
    registry = 'pypi'


def build_wheel(cfg: Cfg):
    return wheel.cmd.build(clean_dir=True)


def build_docs(cfg: Cfg):

    q = (
        f"{fg.red}WARNING{fg.rs}\n"
        "Documentation changes and code changes should use seperate commits.\n"
        "Only proceed if there are no uncommited code changes.\n\n"
        "Do you want to build the documentation pages?"
    )
    if not prmt.confirm(q, 'n'):
        return

    # Build Static Page with Sphinx
    sp.run(['make', 'html'], cwd='sphinx')

    build_html_dir = 'sphinx/_build/html'

    if os.path.isfile(f"{build_html_dir}/index.html"):
        shutil.rmtree('docs', ignore_errors=True)
        shutil.copytree(build_html_dir, 'docs')
        shutil.rmtree(build_html_dir, ignore_errors=True)

    # Create README.rst
    readme_str = ''
    docs = 'sphinx/intro/'
    files = [
        'github_readme_head.rst',
        'description.rst',
        'subscribe.rst',
        'requirements.rst',
        'github_readme_tail.rst',
    ]

    for filename in files:
        with open(docs + filename, 'r') as f:
            readme_str += f.read()

    with open('README.rst', 'w') as f:
        f.write(readme_str)


def deploy(cfg: Cfg):
    return wheel.cmd.push(clean_dir=True, repository=cfg.registry)


def test(cfg: Cfg):
    sp.run(['python', '-m', 'tests'])


def bump(cfg: Cfg):

    results = []

    if prmt.confirm("Do you want to BUMP VERSION number?", "n"):
        result = project.cmd.bump_version()
        cfg.version = result.val
        results.append(result)

    if prmt.confirm("Do you want to BUILD WHEEL?", "n"):
        results.append(build_wheel(cfg))

    if prmt.confirm("Do you want to PUSH WHEEL to PYPI?", "n"):
        results.append(deploy(cfg))

    if prmt.confirm("Do you want to BUILD DOCUMENTATION PAGES?", "n"):
        results.append(build_docs(cfg))

    new_release = cfg.version != proj['version']

    if prmt.confirm("Do you want to RUN GIT COMMANDS?", "n"):
        results.extend(git.seq.bump_git(cfg.version, new_release))

    return results


def run():

    cfg = Cfg()
    uinput = docopt(interface)
    results = []

    if uinput['build'] and uinput['wheel']:
        results.append(build_wheel(cfg))

    if uinput['build'] and uinput['docs']:
        results.append(build_docs(cfg))

    if uinput['deploy']:
        results.append(deploy(cfg))

    if uinput['test']:
        test(cfg)

    if uinput['git']:
        results.append(git.seq.bump_git(cfg.version, new_release=False))

    if uinput['bump']:
        results.extend(bump(cfg))

    if results:
        print_summary(results)


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print('\n\nScript aborted by user.')
