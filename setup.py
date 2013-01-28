import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def scripts( ):
    return [os.path.join( 'bin', f ) for f in os.listdir( 'bin' )]

# The next three lines are modified from Biopython
__version__ = "Undefined"
for line in open('mutations/__init__.py'):
    if (line.startswith('__version__')):
        exec(line.strip())
        break

setup(
    name = "mutation_counts",
    version = __version__,
    author = "Tyghe Vallard",
    author_email = "vallardt@gmail.com",
    description = ("Count mutations between a reference and batch of sequences"),
    keywords = "biopython mutations count t_coffee",
    url = "https://github.com/VDBWRAIR/MutationCount",
    packages = ['mutations'],
    scripts = scripts(),
    install_requires = [
        "numpy >=1.6",
        "biopython >=1.59"
    ],
    long_description=read('README'),
)
