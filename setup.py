import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'webargs>=1.5.0',
    'marshmallow>=2.10.3',
    'requests>=2.4.2',
]


setup(name='webargsclient',
      version='0.1',
      description='webargsclient',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        ],
      author='',
      author_email='',
      url='',
      keywords='webargs marshmallow http client requests',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="tests",
      # entry_points="""\
      # [paste.app_factory]
      # main = welcome:main
      # """,
      )
