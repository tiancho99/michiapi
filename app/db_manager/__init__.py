import csv
import os

from .models import db, Michis, Doggos, Tags, michi_tag_m2m, doggo_tag_m2m


def populate_tables():
    print("HOLA")
    files_names = ["michis.csv", "doggos.csv", "tags.csv", "michi_tag_m2m.csv", "doggo_tag_m2m.csv"]
    for file in files_names:
        file_path = os.path.abspath(os.path.join("data", file))
        with open(file_path) as data_file:
            reader = list(csv.DictReader(data_file))
        if file == "michis.csv":
            db.session.execute(db.insert(Michis).values(reader))
        elif file == "doggos.csv":
            db.session.execute(db.insert(Doggos).values(reader))
        elif file == "tags.csv":
            db.session.execute(db.insert(Tags).values(reader))
        elif file == "michi_tag_m2m.csv":
            db.session.execute(db.insert(michi_tag_m2m).values(reader))
        elif file == "doggo_tag_m2m.csv":
            db.session.execute(db.insert(doggo_tag_m2m).values(reader))

    db.session.commit()


def michi_list():
    michis = db.session.execute(db.select(Michis)).scalars()
    return michis

def get_michi(id):
    michi = db.get_or_404(Michis, id)
    return michi

def doggo_list():
    doggos = db.session.execute(db.select(Doggos)).scalars()
    return doggos

def get_doggo(id):
    doggo = db.get_or_404(Doggos, id)
    return doggo

def tag_list():
    tags = db.session.execute(db.select(Tags)).scalars()
    return tags

def get_tag(id):
    tag = db.get_or_404(Tags, id)
    return tag

def michi_tags_list(id):
    michi_tags = db.session.execute(db.select(michi_tag_m2m.c.tag_id).where(michi_tag_m2m.c.michi_id==id)).scalars()
    return michi_tags

def doggo_tags_list(id):
    doggo_tags = db.session.execute(db.select(doggo_tag_m2m.c.tag_id).where(doggo_tag_m2m.c.doggo_id==id)).scalars()
    return doggo_tags
