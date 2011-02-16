import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = ['pyramid', 'WebError', 'ogcserver']

setup(name='papyrus_mapnik',
      version='0.1',
      description='papyrus_mapnik',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Justin Penka',
      author_email='jpenka@gmail.com',
      url='https://github.com/h0st1le/papyrus_mapnik',
      keywords='web geospatial papyrus mapnik ogcserver pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="papyrus_mapnik",
      entry_points = """\
      [paste.app_factory]
      main = papyrus_mapnik:main
      """,
      paster_plugins=['pyramid'],
      )
