from flask import Blueprint, jsonify

from locsearch import download_dump, get_dump_contents, dump_query, FIELDS


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/api'
)

@bp.route('/search/<country_code>/<query>')
def show(country_code, query):
    download_dump(country_code)
    
    values = []

    for v in dump_query(get_dump_contents(country_code), name=query):
        values.append(v)

    return jsonify(values)
