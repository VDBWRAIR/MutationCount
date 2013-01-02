import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mutation_counts",
    version = "0.0.1",
    author = "Tyghe Vallard",
    author_email = "vallardt@gmail.com",
    description = ("Count mutations between a reference and batch of sequences"),
    keywords = "biopython mutations count t_coffee",
    url = "https://github.com/VDBWRAIR/MutationCount",
    packages = ['mutations'],
    scripts = [
        'mutations/mutalign',
    ],
    data_files = [
        ('bin', ['mutations/ext/bin/t_coffee']),
    ],
    install_requires = [
        "numpy >=1.6",
        "biopython >=1.59"
    ],
    long_description=read('README'),
)
