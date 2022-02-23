from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Irale',
    version='0.0.1',
    description='',
    long_description=readme,
    author='Swartz',
    url='https://github.com/Swartz-42/Irale_Game_Py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

