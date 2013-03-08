This is a Django web interface for `pyxform <https://github.com/UW-ICTD/pyxform>`_ (the xlsform converter for ODK Collect).

Installation
============

- Setup a Django server and project::

	Some useful links:

	https://docs.djangoproject.com/en/1.4/intro/install/
	
	http://www.robotmedia.net/2011/04/how-to-create-an-amazon-ec2-instance-with-apache-php-and-mysql-lamp/

	https://docs.djangoproject.com/en/1.4/howto/deployment/wsgi/
	
	https://code.djangoproject.com/wiki/django_apache_and_mod_wsgi#dj_survey.wsgi

	https://docs.djangoproject.com/en/1.4/ref/django-admin/#django-admin-startproject

- Install the dependencies::

	apt-get install openjdk-6-jre python-setuptools git-core

	easy_install pip 

- Download this repo and install the requirements::

	cd [your Django project directory]

	git clone git://github.com/UW-ICTD/pyxform_interface.git

	pip install -r pyxform_interface/requirements.pip

- Make the following changes to setup.py::

	If 'django.middleware.csrf.CsrfViewMiddleware' is in MIDDLEWARE_CLASSES remove it.
	Warning: this can cause issues for other apps you are running.

	Add 'pyxform_interface' to INSTALLED_APPS

- Add this line to the bottom of urls.py (in your Django project directory)::

	urlpatterns += patterns('', url(r'^xlsform/', include('pyxform_interface.urls')))

- If using mod_wsgi add this to wsgi.py::

	sys.path.append('Your Django project directory path here')

- When you are done reset the server::

	#This path varies by server
	/etc/init.d/apache2 restart

Maintenance
============

Forms are stored in the `/tmp` directory, and may need to be periodically removed. `tmpreaper <http://manpages.ubuntu.com/manpages/hardy/man8/tmpreaper.8.html>`_ can be used to remove older forms that are unlikely to be accessed.
