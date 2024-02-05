from flask import request, render_template, url_for, current_app

from . import michi_api, limiter
from app import db_manager
from app.utils.response import success_response, error_response

import os

@michi_api.route("/")
@limiter.limit("100/hour", override_defaults=False)
def api():
    endpoints = {
        "michis": os.environ.get("MICHIAPI_ENDPOINT") + url_for("michiapi.michis"),
        "doggos": os.environ.get("MICHIAPI_ENDPOINT") + url_for("michiapi.doggos"),
        "tags": os.environ.get("MICHIAPI_ENDPOINT") + url_for("michiapi.tags"),
    }
    if request.args.get("format") == "json":
        return success_response(endpoints=endpoints)
    
    response = success_response(endpoints=endpoints)
    context = {
        "data": response.get_data(as_text=True),
    }
    return render_template("api_show.html", **context)


#* Michis
@michi_api.route("/michis")
@limiter.limit("100/hour", override_defaults=False)
def michis():
    try:
        format = request.args.get("format")

        if format == "api":
            return render_template("api_show.html")
        else:
            michi_list = db_manager.michi_list()
            response = [michi.serialize() for michi in michi_list]
            return success_response(data=response)
    except Exception as error:
        return error_response(error)

@michi_api.route("/michis/<int:id>")
@limiter.limit("100/hour", override_defaults=False)
def michi(id):
    try:
        michi = db_manager.get_michi(id)
        serialized_michi = michi.serialize()
        return success_response(data=serialized_michi)
    except Exception as error:
        return error_response(error)


#* Doggos
@michi_api.route("/doggos")
@limiter.limit("100/hour", override_defaults=False)
def doggos():
    try:
        doggo_list = db_manager.doggo_list()
        return success_response(data=[doggo.serialize() for doggo in doggo_list])
    except Exception as error:
        return error_response(error)

@michi_api.route("/doggos/<int:id>")
@limiter.limit("100/hour", override_defaults=False)
def doggo(id):
    try:
        doggo = db_manager.get_doggo(id)
        response = success_response(data=doggo.serialize())
        return response
    except Exception as error:
        return error_response(error)


#* Tags
@michi_api.route("/tags")
@limiter.limit("100/hour", override_defaults=False)
def tags():
    try:
        tag_list = db_manager.tag_list()
        response = success_response(data=[tag.serialize() for tag in tag_list])
        return response
    except Exception as error:
        return error_response(error)

@michi_api.route("tags/<int:id>")
@limiter.limit("100/hour", override_defaults=False)
def tag(id):
    try:
        tag = db_manager.get_tag(id)
        response = success_response(data=tag.serialize())
        return response
    except Exception as error:
        return error_response(error)
