# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_user_views.py

import os
import sys
from unittest import TestCase

from models import db, connect_db, User, Product, Type, Category, Brand
from bs4 import BeautifulSoup
from flask import g

import sqlalchemy_utils

if sqlalchemy_utils.functions.database_exists("postgresql:///makeup-test"):
    os.environ['DATABASE_URL'] = "postgresql:///makeup-test"
    print(os.environ['DATABASE_URL'])
else:
    sqlalchemy_utils.functions.create_database("postgresql:///makeup-test")

from app import app, CURR_USER_KEY, add_user_to_g


app.config['WTF_CSRF_ENABLED'] = False


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """ Create test client, add sample data. """

        db.drop_all()
        db.create_all()

        self.client = app.test_client()

        self.testuser = User.signup(email="test@test.com",
                                    password="testuser")

        self.testuser_id = 10000
        self.testuser.id = self.testuser_id

        new_brand = Brand(name="L.A. Girl")

        new_product = Product(name="Volumatic Mascara", link="https://www.ulta.com/volumatic-mascara?productId=pimprod2007350", 
                                brand_id=1, price="$3.48 - $6.99", external_product_id="203", product_type_id=1, product_site="Ulta", 
                                category_id=1, image="https://images.ulta.com/is/image/Ulta/2546830?$md$", color="Bright Blue", 
                                color_image="https://images.ulta.com/is/image/Ulta/2546821sw?$50px$", search_terms="Volumatic Mascara Bright Blue L.A. Girl")
        
        new_type = Type(name="Mascara")

        new_category = Category(name="Eyes")

        db.session.add_all([new_type, new_brand, new_category, new_product])
        db.session.commit()



    def tearDown(self):
        """ Reset after evey test. """
        resp = super().tearDown()
        db.session.rollback()

        return resp


    def test_user_collection(self):
        """ Can user see their collection after successful login?"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser_id
            resp = c.get("/collection", follow_redirects=True)
   
            self.assertEqual(resp.status_code, 200)
            self.assertIn('My Collection', str(resp.data))


    def test_users_search(self):
        """ Can the user see the search results page and are the expected results visible?"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser_id

            resp = c.get("/search?search-term=Volumatic+Mascara")
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Volumatic Mascara -Bright Blue", str(resp.data))
            self.assertIn("Search Results", str(resp.data))
            self.assertIn("Add to Collection", str(resp.data))
            self.assertIn('There are 1 results for "Volumatic Mascara"', str(resp.data))


    def test_users_add_to_collection(self):
        """ Can the user add a product to their collection?"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser_id
            
            resp = c.post("/add/1")

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json['result'], "Product added successfully")

            resp = c.get('/collection')

            self.assertEqual(resp.status_code, 200)

            self.assertIn("Volumatic Mascara -Bright Blue", str(resp.data))


    def test_users_remove_from_collection(self):
        """ Can the user remove a product from their collection?"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser_id
            
            resp = c.post("/add/1")

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json['result'], "Product added successfully")

            resp = c.get('/collection')

            self.assertEqual(resp.status_code, 200)

            self.assertIn("Volumatic Mascara -Bright Blue", str(resp.data))

            resp = c.post('/remove/1')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json['result'], "Product removed successfully")

            resp = c.get('/collection')

            self.assertEqual(resp.status_code, 200)

            self.assertNotIn("Volumatic Mascara -Bright Blue", str(resp.data))


    def test_users_logout(self):
        """ Can the user logout? """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser_id

            resp = c.post('/logout')

            self.assertEqual(resp.status_code, 302)

            resp = c.get('/collection')

            self.assertEqual(resp.status_code, 302)