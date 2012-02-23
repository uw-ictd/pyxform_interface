This is a Django web interface for converting xls spreadsheets to xforms for use with Open Data Kit.

Installation
============

- Setup a Django server (for one click solutions see Turnkey and Bitnami)

- Download and this repo::

	cd [your Django project directory]

	git clone git://github.com/UW-ICTD/pyxform-interface.git

- Install the dependencies::

	#Here things become a bit tricky if you use bitnami

	apt-get install openjdk-6-jre python-setuptools git-core

	easy_install pip 

	pip install -r pyxform-interface/requirements.pip

- Make some undocumented changes to setup.py to urls.py

- When you are done reset the server::

	Bitnami:
	sudo /opt/bitnami/ctlscript.sh restart apache
	Turnkey:
	/etc/init.d/apache2 restart
	