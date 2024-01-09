from flask import render_template, request, url_for
from app.utils.response import success_response, error_response
import datetime

from app import create_app
from app import db_manager


app = create_app()

@app.route("/", methods=["GET"])
def home():
    try:
        michi = db_manager.get_michi(1)
        serialized_michi = michi.serialize()
        michi_tag_list = db_manager.michi_tags_list(serialized_michi["id"])
        serialized_michi["tags"] = list(michi_tag_list)
        response = success_response(data=serialized_michi)
        context = {
            "year": datetime.date.today().year,
            "data": response.get_data(as_text=True),
        }
        return render_template("index.html", **context)
    except Exception as error:
        return error_response(error)

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/populate")
# def populate():
#    db_manager.populate_tables()
#    return "success"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
