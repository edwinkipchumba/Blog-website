from flask import Blueprint

main = Blueprint('main',__name__)

# importing error
from . import views,error
