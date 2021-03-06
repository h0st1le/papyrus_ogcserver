""" TODO: Add in tests for 100% coverage """
import os
import unittest

from pyramid import testing

class AddRouteTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test(self):
        from papyrus_ogcserver import add_route
        route = add_route(self.config)
        from pyramid.urldispatch import Route
        self.assertTrue(isinstance(route, Route))
        self.assertEqual(route.name, 'ogcserver')
        self.assertEqual(route.pattern, '/ogcserver{path:.*?}')

class MainTests(unittest.TestCase):
    def test(self):
        from papyrus_ogcserver import main
        app = main({}, a='a')
        from pyramid.router import Router
        self.assertTrue(isinstance(app, Router))

class DummyContext:
    pass
