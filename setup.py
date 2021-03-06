import os

import setuptools

from currentplatform import __version__


def read(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
   name='krozark-current-platform',
   version=__version__,
   description='The aim of this project is to get the current running platform',
   long_description=read('README.md'),
   long_description_content_type="text/markdown",
   license="BSD2",
   author='Maxime Barbier',
   author_email='maxime.barbier1991+platform@gmail.com',
   url="https://github.com/Krozark/platform",
   keywords="current platform",
   packages=setuptools.find_packages(),
   classifiers=[
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      "Operating System :: OS Independent",
    ],
   python_requires='>=3.6',
)