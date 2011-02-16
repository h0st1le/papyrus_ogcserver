papyrus_mapnik
=================

papyrus_mapnik provides an easy and convenient method for embeding
a Mapnik OGCServer into Pyramid applications.

papyrus_mapnik is based on papyrus_tilecache by Éric Lemoine
https://github.com/elemoine/papyrus_tilecache

Install
-------

Installing Papyrus in an isolated ``virtualenv`` is recommended

papyrus_mapnik is installed using the applications ``setup.py``

    $ python papyrus_mapnik/setup.py install 

Often you'll want to make papyrus_mapnik a dependency of your Pyramid
application, which is done by adding ``papyrus_mapnik`` to the
``install_requires`` list defined in the Pyramid application's ``setup.py``
file.

Embed Mapnik OGCServer
----------------------

Embeding a Mapnik OGCServer in a Pyramid application is easy.

Edit the application's ``development.ini`` file and, in the main section
(``[app:]``), set ``ogcserver_config`` to the location of the OGCServer config
file. Example::

    [app:MyApp]
    use = egg:MyApp
    ...
    ogcserver_config = %(here)s/ogcserver.conf

In this example the OGCServer config file is located at the same location as
the ``development.ini`` file. 

An example ogcserver.conf is included and additional information is available 
at the mapnik ogcserver repository https://github.com/mapnik/OGCServer regarding
the ogcserver configuration file.

The map itself is constructed in one of two ways: using either a mapnik xml file 
or using pure python through a WMSFactory. 

1.) To use an xml defined map edit the application's ``development.ini``
    file and in the main section (``[app:]``), set ``mapfile`` to the location of the 
    mapnik xml file.

2.) To use a python WMSFactory edit the application's ``development.ini``
    file and in the main section (``[app:]``), set ``server_module`` to the name of the 
    module containing the MapFactory class (without extension .py)

Now, edit the application's main file, ``__init__.py``, and register
papyrus_mapnik using the ``Configurator.include`` method::

    def main(global_config, **settings):

        config = Configurator(settings=settings)

        import papyrus_mapnik
        config.include(papyrus_mapnik)

That's it! The Pyramid application now exposes a Mapnik OGCServer service at
``/mapnik``.

`Test URL <http://localhost:23758/mapnik?LAYERS=world&FORMAT=image%2Fpng&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&EXCEPTIONS=application%2Fvnd.ogc.se_inimage&SRS=EPSG%3A4326&BBOX=-180.0000000000001,-90,119.46385052802589,209.463850528026&WIDTH=256&HEIGHT=256`_
