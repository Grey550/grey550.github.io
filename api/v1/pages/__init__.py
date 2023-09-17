#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_pages = Blueprint('app_pages', __name__, url_prefix='/api/v1')

from api.v1.pages.index import *
from api.v1.pages.states import *
from api.v1.pages.places import *
from api.v1.pages.places_reviews import *
from api.v1.pages.cities import *
from api.v1.pages.activities import *
from api.v1.pages.users import *
from api.v1.pages.places_activities import *
