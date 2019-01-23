import shutil
import os
import subprocess as sp
from cmdi import print_summary
from buildlib import buildmisc, git, wheel, project, yaml
from docopt import docopt

interface = """
    Install:
        pipenv install
        pipenv run python make.py

    Usage:
        make.py build [options]
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


def build_docs():
    sp.run(['make', 'html'], cwd='sphinx')

    build_html_dir = 'sphinx/_build/html'

    if os.path.isfile(f"{build_html_dir}/index.html"):
        shutil.rmtree('docs', ignore_errors=True)
        shutil.copytree(build_html_dir, 'docs')
        shutil.rmtree(build_html_dir, ignore_errors=True)


def create_readme():

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


def build(cfg: Cfg):

    build_docs()
    create_readme()

    return wheel.cmd.build(clean_dir=True)


def deploy(cfg: Cfg):
    return wheel.cmd.push(clean_dir=True, repository=cfg.registry)


def test(cfg: Cfg):
    sp.run(['python', '-m', 'tests'])


def bump(cfg: Cfg):

    results = []

    if project.prompt.should_bump_version():
        result = project.cmd.bump_version()
        cfg.version = result.val
        results.append(result)

    build(cfg)

    if wheel.prompt.should_push('PYPI'):
        results.append(deploy(cfg))

    new_release = cfg.version != proj['version']

    results.extend(git.seq.bump_git(cfg.version, new_release))

    return results


def run():

    cfg = Cfg()
    uinput = docopt(interface)
    results = []

    if uinput['build']:
        results.append(build(cfg))

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
