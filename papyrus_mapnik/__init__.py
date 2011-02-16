from pyramid.config import Configurator

from papyrus_mapnik.views import load_ogcserver_config

def add_route(config):
    """ Add a route to the mapnik view callable. The OGCService
    service is made available at ``/mapnik``.

    Arguments:

    * ``config``: the ``pyramid.config.Configurator`` object.
    """
    return config.add_route('mapnik', '/mapnik{path:.*?}',
                            view='papyrus_mapnik.views:mapnik'
                            )

def includeme(config):
    """ The callable making it possible to include papyrus_mapnik
    in a Pyramid application.

    Calling ``config.include(papyrus_mapnik)`` will result in this
    callable being called.

    Arguments:

    * ``config``: the ``pyramid.config.Configurator`` object.
    """
    load_ogcserver_config(config.get_settings())
    add_route(config)

def main(global_config, **settings):
    """ Return the Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include(includeme)
    return config.make_wsgi_app()


