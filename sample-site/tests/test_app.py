import os
import sys
import pytest
import flask
from unittest import mock

job_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(job_path)

from app import app


@pytest.fixture()
def flask_app():
    flask_app = app
    flask_app.config.update(
        {
            "TESTING": True,
        }
    )

    yield flask_app


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()


def test_generate_page_potato(client):
    response = client.get("/")
    assert b"Po-tay-toes" in response.data


@mock.patch("app.picture", "carrots.jpeg")
def test_generate_page_other_veg(client):
    response = client.get("/")
    assert b"Oh no" in response.data
