from flask import Flask

from locsearch.views.index import bp as index_bp
from locsearch.views.api import bp as api_bp


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(index_bp)
app.register_blueprint(api_bp)
