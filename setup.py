from setuptools import setup, find_packages


setup(
    name='locsearch',
    version='1.0.0',
    install_requires=[
        'requests',
        'unicodecsv',
        'tabulate',
        'flask'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'locsearch = locsearch.bin:run'
        ]
    }
)
