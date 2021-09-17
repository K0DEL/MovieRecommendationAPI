from main import db, Movie

n = db.session.query(Movie).delete()
db.session.commit()
print(n)
