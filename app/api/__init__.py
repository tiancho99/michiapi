from flask import Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

michi_api = Blueprint("michiapi", __name__, static_folder="../static", template_folder="../templates")

limiter = Limiter(
    get_remote_address,
    default_limits=["200/day", "100/hour"],
    storage_uri="memory://",
)

from . import routes