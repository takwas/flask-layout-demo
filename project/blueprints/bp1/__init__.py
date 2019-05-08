from flask import Blueprint 


bp_obj = Blueprint('bp_obj', __name__)

from . import controllers
