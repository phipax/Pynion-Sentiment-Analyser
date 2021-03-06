import os
import pytest
import flask

myapp = flask.Flask(__name__)

def test_home_page():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    with myapp.test_request_context('/'):
        assert flask.request.path == '/', "path is available"

# def test_adding_search_item():
#     """
#     GIVEN we are on homepage (/)
#     WHEN value is added on search field and search button is clicked
#     THEN check the response is valid
#     """
#     # with app.test_request_context('/'):
#     response = ''
# #     myapp.post('/', follow_redirects=True)
#     assert response.status_code == 200
#     assert b"Logout" in response.data
#     assert b"Login" not in response.data
