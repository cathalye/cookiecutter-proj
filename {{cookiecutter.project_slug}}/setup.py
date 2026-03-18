from setuptools import find_packages, setup

setup(
    name='{{cookiecutter.project_slug}}',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)
