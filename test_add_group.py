# -*- coding: utf-8 -*-
#from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(self):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="dfrfgwrgw", header="gfsgwrgwg", footer="gwrgwgwrg"))
    app.return_to_groups_page()
    app.logout()

def test_add_empty_group(self):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.return_to_groups_page()
    app.logout()