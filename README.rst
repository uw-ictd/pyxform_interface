This is a Django web interface for converting xls spreadsheets to xforms for use with Open Data Kit.

Installation
============

- Setup a Django server (for one click solutions see Turnkey and Bitnami)

- Download this repo::

	cd [your Django project directory]

	git clone git://github.com/UW-ICTD/pyxform_interface.git

- Install the dependencies::

	apt-get install openjdk-6-jre python-setuptools git-core

	easy_install pip 

	pip install -r pyxform_interface/requirements.pip

	This gets tricky if you are using bitnami.
	Don't use sudo when you run easy_install pip.
	And when use use pip do this:

	export PYTHONPATH=/opt/bitnami/python/lib/python2.6/site-packages
	pip install --install-option="--prefix=/opt/bitnami/python" -r pyxform_interface/requirements.pip

- Make the following changes to setup.py::

	If 'django.middleware.csrf.CsrfViewMiddleware' is in MIDDLEWARE_CLASSES remove it.
	Warning: this can cause issues for other apps you are running.

	Add 'pyxform_interface' to INSTALLED_APPS

- Add this line to the bottom of urls.py (in your Django project directory)::

	urlpatterns += patterns('', url(r'^xls2xform/', include('Project.pyxform_interface.urls')))

- When you are done reset the server::

	Bitnami:
	sudo /opt/bitnami/ctlscript.sh restart apache
	Turnkey:
	/etc/init.d/apache2 restart