This is a Django web interface for converting xls spreadsheets to xforms for use with Open Data Kit.

Installation
============

- Setup a Django server (for one click solutions see Turnkey and Bitnami)

- Install some packages (may require sudo)::

	apt-get install openjdk-6-jre python-setuptools git-core
	easy_install pip 

- Download and install this repo::

	cd [your Django project directory]

	git clone git://github.com/UW-ICTD/pyxform-interface.git

	pip install -r pyxform-interface/requirements.pip

- Make some undocumented changes to setup.py to urls.py