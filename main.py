from flask import render_template, request, url_for, send_from_directory
from app.utils.response import success_response, error_response
import datetime
import os

from app import create_app
from app import db_manager

app = create_app()

@app.route("/", methods=["GET"])
def home():
    michi = db_manager.get_michi(1)
    serialized_michi = michi.serialize()
    response = success_response(data=serialized_michi)
    context = {
        "year": datetime.date.today().year,
        "data": response.get_data(as_text=True),
    }
    return render_template("index.html", **context)

@app.route("/documentation")
def documentation():
    endpoint = os.environ.get("MICHIAPI_ENDPOINT")
    return render_template("documentation.html", endpoint=endpoint)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/images/michis/<file>")
def michis_images(file):
    return send_from_directory(os.path.join(app.config["UPLOAD_FOLDER"], "michis"), file)

@app.route("/images/doggos/<file>")
def doggos_images(file):
    return send_from_directory(os.path.join(app.config["UPLOAD_FOLDER"], "doggos"), file)
           
# @app.route("/populate")
# def populate():
#    db_manager.populate_tables()
#    return "success"

# @app.route("/urls")
# def urls():
#     import csv
#     with open("data/doggos.csv") as michis_file:
#         reader = csv.reader(michis_file)
#         with open("data/doggos.csv", "a") as michis_file:
#             writer = csv.writer(michis_file)
#             for row in reader:
#                 row[3] = os.path.join("http://michiapi.sebastianhernandez.dev/images/doggos",f"{row[1].lower()}-dog.gif")
#                 writer.writerow(row)

#     return "success"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
