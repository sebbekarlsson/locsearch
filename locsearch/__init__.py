import requests

import shutil

import zipfile

import csv

import io

import os


FIELDS = [
    'geonameid',
    'name',
    'asciiname',
    'alternate',
    'latitude',
    'longitude',
    'feature_class',
    'feature_code',
    'country_code',
    'cc2',
    'admin1_code',
    'admin2_code',
    'admin3_code',
    'admin4_code',
    'population',
    'elevation',
    'dem',
    'timezone',
    'modification_date'
]

def download_dump(country_code):
    c = country_code.upper()

    response = requests.get(
        f'http://download.geonames.org/export/dump/{c}.zip',
        stream=True
    )

    dest = f'{c}.zip'

    if not os.path.isfile(dest):
        print(f'Downloading {dest} ...')
        with open(dest, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

    return response


def get_dump_contents(country_code):
    c = country_code.upper()

    return zipfile.ZipFile(f'{c}.zip', 'r').open(f'{c}.txt', 'r').read().decode()


def dump_query(contents, **kwargs):
    reader = csv.DictReader(io.StringIO(contents), fieldnames=FIELDS, delimiter='\t')

    for row in reader:
        for k, v in dict(**kwargs).items():
            if v.lower() in row.get(k, '').lower():
                yield row
