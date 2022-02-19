from email.mime import base
from flask import Blueprint

base = Blueprint('base', __name__, url_prefix='/api')

from ..routes import *