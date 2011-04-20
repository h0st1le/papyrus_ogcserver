import time
import email
import ConfigParser

from pyramid.wsgi import wsgiapp

from ogcserver.wsgi import ogcserver_map_factory, ogcserver_wms_factory

# set default expiration time to 1 day (pulled from ogcserver.conf)
DEFAULT_EXPIRATION = 86400

# Mapnik OGCServer Service instance
_service = None
# Time limit for Cache expiration
_cache_exp = None 

def load_ogcserver_config(settings):
    """ Load the mapnik ogcserver config.

    This creates an instance of the mapnik ogcserver WSGIApp and
    stores the return value in a private global variable.

    Arguments:

    * ``settings``: a dict with a ``ogcserver_config`` key whose
      value provides the path to Mapnik OGCServer configuration file.
    
      also include either a ``mapfile`` key with path to the mapnik xml file
      or a ``server_module`` key that provides the name of the Python WMSFactory class
      for map creation"
    """
    global _service
    if hasattr(settings, 'mapfile'):
        _service = ogcserver_map_factory(settings)
    if hasattr(settings, 'server_module'):
        _service = ogcserver_wms_factory(settings)
    """ TODO: move this out of globals and pull from the _service below """
    global _cache_exp 
    try:
        _cache_exp = getattr(settings, 'maxage')
    except:
        _cache_exp = DEFAULT_EXPIRATION

@wsgiapp
def ogcserver(environ, start_response):

    # custom_start_response adds cache headers to the response
    def custom_start_response(status, headers, exc_info=None):
        headers.append(('Cache-Control', 'public, max-age=%s'
            % _cache_exp))
        headers.append(('Expires', email.Utils.formatdate(
            time.time() + float(_cache_exp), False, True)))
        return start_response(status, headers, exc_info)

    return _service.__call__(environ, custom_start_response)
