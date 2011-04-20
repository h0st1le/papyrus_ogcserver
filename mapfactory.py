from ogcserver.WMS import BaseWMSFactory
from mapnik import *

SHAPEFILE = '/home/h0st1le/webapps/template/papyrus_ogcserver/shapefiles/world_borders.shp'
PROJ4_STRING = '+proj=latlong +datum=WGS84'

class WMSFactory(BaseWMSFactory):
    def __init__(self):
        BaseWMSFactory.__init__(self)
        sty,rl = Style(),Rule()
        poly = PolygonSymbolizer(Color('#f2eff9'))
        line = LineSymbolizer(Color('steelblue'),.1)
        rl.symbols.extend([poly,line])
        sty.rules.append(rl)
        self.register_style('world_style',sty)
        lyr = Layer('world',PROJ4_STRING)
        lyr.datasource = Shapefile(file=SHAPEFILE)
        lyr.title = 'World Borders'
        lyr.abstract = 'Country Borders of the World'
        self.register_layer(lyr,'world_style',('world_style',))
        self.finalize()
