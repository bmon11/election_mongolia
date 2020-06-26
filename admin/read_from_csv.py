from app.models import District
from app import db, app
import csv
import os
from datetime import datetime

with app.app_context():
    with open('districts.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dists = []
        for row in csv_reader:
            dist = District(created_at=datetime.now(),
                            code=row[0],
                            name=row[1],
                            quote=row[2])
            dists.append(dist)
        db.session.bulk_save_objects(dists)
        db.session.commit() 