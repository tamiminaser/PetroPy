""""This is the file that setup our PetroPy package."""

from setuptools import setup

setup(name='PetroPy',
      version='0.1', 
      packages=['petropy'], 
      license='MIT License',
      long_description=open('README.md').read(),
      install_requires=['numpy>=1.11'])