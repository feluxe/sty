from codecs import open

import toml
from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()


project = toml.load("pyproject.toml")["mewo_project"]


setup(
    name="sty",
    version=project["version"],
    author="Felix Meyer-Wolters",
    author_email="felix@meyerwolters.de",
    maintainer="Felix Meyer-Wolters",
    maintainer_email="felix@meyerwolters.de",
    url="https://github.com/feluxe/sty",
    description="String styling for your terminal",
    long_description=readme,
    long_description_content_type="text/x-rst",
    download_url="https://github.com/feluxe/sty" + "/tarball/" + project["version"],
    license="Apache 2.0",
    keywords=["styling", "color", "colour", "terminal", "ansi"],
    include_package_data=True,
    platforms="",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Typing :: Typed",
        "Topic :: Printing",
        "Topic :: Terminals",
        "Topic :: System :: Shells",
    ],
    install_requires=[],
    packages=find_packages(where=".", exclude=("tests", "tests.*")),
    package_dir={"sty": "sty"},
    package_data={},
    data_files=[],
    entry_points={"console_scripts": [], "gui_scripts": []},
    tests_require=[],
)
