from argparse import ArgumentParser

from locsearch import download_dump, get_dump_contents, dump_query, FIELDS

from tabulate import tabulate


def run():
    parser = ArgumentParser()
    parser.add_argument('country_code')
    parser.add_argument('query')
    
    args = parser.parse_args()

    download_dump(args.country_code)
    
    values = []

    for v in dump_query(get_dump_contents(args.country_code), name=args.query):
        values.append(v)

    print(tabulate(
        [
            [
                v['geonameid'], v['name'], v['population']
            ] for v in values
        ],
       headers=['id', 'name', 'population'])
    )
