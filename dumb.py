from models import db, connect_db, Product, Brand
from app import app
import sys
from sqlalchemy.sql.expression import func

from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///makeup3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

make_searchable(db.metadata)

class ArticleQuery(BaseQuery, SearchQueryMixin):
    pass


class Article(db.Model):
    query_class = ArticleQuery
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255))
    content = db.Column(db.UnicodeText)
    search_vector = db.Column(TSVectorType('name', 'content'))

class Brand(db.Model):
    query_class = ArticleQuery
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)


db.drop_all()
db.configure_mappers() #very important!
db.create_all()
db.session.commit()

a1 = Article(name='Finland', content='This is a country.')
a2 = Article(name='Findland', content='This is a 2nd country.')

db.session.add_all([a1,a2])
db.session.commit()

results = Article.query.search(u'Finland').limit(5).all()
brands = Brand.query.search('Tarte').limit(5).all()
print(results, file=sys.stderr)
for result in results:
    print(result.name)