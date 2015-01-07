from flask import Blueprint, render_template
from ..app import add_blueprint
import json
from ..config import settings
from os.path import join

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    """ Returns the homepage. """
    return render_template('home/index.html.slim')

add_blueprint(bp)