from setuptools import setup, find_packages

setup(
    name = 'nycpython',
    version = '1.0',
    author = 'David Christian',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
    classifiers=[
        'Framework :: Django',
        ],
)
