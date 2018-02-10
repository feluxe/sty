import sys
import os

sys.path.append(os.path.abspath(os.path.join('..', 'buildlib')))

from typing import Union
from buildlib.utils import yaml
from buildlib.cmds import semver, build
from buildlib.cmds.git import sequence as git_seq
from cmdinter import CmdFuncResult

CFG_FILE = 'Project'
CFG = yaml.load_yaml(
    file=CFG_FILE,
    keep_order=True
)

__version__ = CFG.get('version')


def get_version_from_user() -> str:
    """
    Get new Version number from user or use the one from CONFIG.yaml.
    """
    return semver.prompt.semver_num_by_choice(
        cur_version=CFG.get('version')
    )


def build_wheel(
    return_result=False,
) -> Union[CmdFuncResult, None]:
    """"""
    result = build.build_python_wheel(
        clean_dir=True
    )

    if return_result:
        return result
    else:
        print(f'\n{result.summary}')


def push_registry(
    return_result=False,
) -> Union[CmdFuncResult, None]:
    """"""
    result = build.push_python_wheel_to_pypi(
        clean_dir=True
    )

    if return_result:
        return result
    else:
        print(f'\n{result.summary}')


def bump_version(
    new_version: str = None,
    return_result: bool = False,
) -> Union[CmdFuncResult, None]:
    """
    Bump (update) version number in CONFIG.yaml.
    """

    if not new_version:
        new_version: str = get_version_from_user()

    result = build.update_version_num_in_cfg_yaml(
        config_file=CFG_FILE,
        semver_num=new_version,
    )

    if return_result:
        return result
    else:
        print(f'\n{result.summary}')


def bump_git() -> None:
    """"""
    results = []

    should_bump_version = build.prompt.should_update_version(
        default='y'
    )

    if should_bump_version:
        version = get_version_from_user()
    else:
        version = CFG.get('version')

    git_settings = git_seq.get_sequence_settings_from_user(
        should_tag_default=version != CFG.get('version'),
        should_bump_any=True,
        version=version,
    )

    if should_bump_version:
        results.append(bump_version(
            new_version=version,
            return_result=True,
        ))

    results += git_seq.bump_sequence(git_settings)

    print('')

    for result in results:
        print(result.summary)


def bump_all() -> None:
    """"""
    results = []

    should_bump_version: bool = build.prompt.should_update_version(
        default='y'
    )

    if should_bump_version:
        version = get_version_from_user()
    else:
        version = CFG.get('version')

    should_build_wheel: bool = build.prompt.should_build_wheel(
        default='y'
    )

    should_push_registry: bool = build.prompt.should_push_pypi(
        default='y' if should_bump_version else 'n'
    )

    if should_bump_version:
        results.append(bump_version(
            new_version=version,
            return_result=True,
        ))

    git_settings = git_seq.get_sequence_settings_from_user(
        should_tag_default=version != CFG.get('version'),
        version=version,
    )

    if should_build_wheel:
        results.append(build.build_python_wheel(
            clean_dir=True
        ))

    if git_settings.should_bump_any:
        results.extend(git_seq.bump_sequence(git_settings))

    if should_push_registry:
        results.append(build.push_python_wheel_to_pypi(
            clean_dir=True
        ))

    print('')

    for result in results:
        print(result.summary)
