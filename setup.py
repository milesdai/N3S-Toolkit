from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='n3s_toolkit',
      version='0.1',
      description='National 3rosion Service puzzle-hunting resources',
      long_description=read('README.md'),
      url='https://github.com/milesdai/N3S-Toolkit',
      author='N3S',
      author_email='milesdai16@gmail.com',
      license='MIT',
      packages=['n3s_toolkit'],
      package_data={'n3s_toolkit': ['assets/*']},
      install_requires=[
          'requests',
      ],
      zip_safe=False)