from pyramid.config import Configurator

from papyrus_ogcserver.views import load_ogcserver_config

def add_route(config):
    """ Add a route to the ogcserver view callable. The OGCService
    service is made available at ``/ogcserver``.

    Arguments:

    * ``config``: the ``pyramid.config.Configurator`` object.
    """
    return config.add_route('ogcserver', '/ogcserver{path:.*?}',
                            view='papyrus_ogcserver.views:ogcserver'
                            )

def includeme(config):
    """ The callable making it possible to include papyrus_ogcserver
    in a Pyramid application.

    Calling ``config.include(papyrus_ogcserver)`` will result in this
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


