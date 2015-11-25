To update the deployment, perform:

cd django/xlsform/xlsform/pyxform_interface
sudo git pull
sudo pip install -r requirements.pip

============================================
SETUP 
============================================
These are the setup instructions followed when setting up an Ubuntu 14.04 LTS instance from scratch:

Start with an AMI image from Canonical:

https://aws.amazon.com/marketplace/seller-profile/ref=dtl_pcp_sold_by?ie=UTF8&id=565feec9-3d43-413e-9760-c651546613f2

The HVM images are for larger boxes. Use the non-HVM images (PV) and select the smallest box you can (t1.tiny)

Choose the quicklaunch-1 security configuration. That sets up to use the april.pem SSH key and opens only port 80 for HTTP and port 22 for SSH

The image will be old, so first, update everything on it:

sudo apt-get update
sudo apt-get upgrade

(reboot is generally required)

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install openjdk-7-jre-headless
sudo apt-get install python-setuptools 
sudo apt-get install python2.7-dev
sudo apt-get install git-core
sudo apt-get install gcc libxml2-dev libxslt-dev libz-dev
sudo apt-get install apache2
sudo apt-get install apache2-mpm-worker
sudo apt-get install apache2-threaded-dev
sudo apt-get install python-pip
sudo apt-get --purge autoremove python-django
sudo bash
> wget https://bootstrap.pypa.io/ez_setup.py -O - | python
> exit
sudo pip install --upgrade pip

sudo pip install xlrd

sudo pip install mod_wsgi

sudo pip install Django

mkdir django
cd django

sudo mkdir xlsform
sudo django-admin startproject xlsform xlsform

cd xlsform/xlsform

sudo vi urls.py
======================================
comment out admin lines:

# from django.contrib import admin
# admin.autodiscover()

and the admin url line:
#   url(r'^admin/', include(admin.site.urls)),
  
add below that admin url line (be careful to quote the include string!):
    url(r'', include('pyxform_interface.urls')),

save and exit
======================================
sudo vi wsgi.py
======================================
add sys to the import list:
import os, sys

at the bottom of the file, BEFORE application = get_wsgi_application();, add:
sys.path.append('/home/ubuntu/django/xlsform/xlsform')

save and exit
======================================
sudo vi settings.py
======================================
under INSTALLED_APPS add:
     'pyxform_interface',

under MIDDLEWARE_CLASSES, comment out:
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

under DATABASES, change 'NAME' entry to:
     'NAME': 'undefined.db',

below USE_TZ = True, add:

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

below STATIC_URL = '/static/' add:

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
	'formatters': {
	    'basic': {
		     'format': "%(asctime)s:%(pathname)s:%(lineno)s: %(message)s",
			 'datefmt': "%d/%b/%Y %H:%M%S"
		}
	},
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
			'when': 'w0',
            'filename': '/var/log/django/django.log',
			'formatter': 'basic'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
======================================
(still within /home/ubuntu/django/xlsform/xlsform)

sudo git clone git://github.com/UW-ICTD/pyxform_interface.git
cd pyxform_interface
sudo pip install -r requirements.pip

======================================
Now, we need to configure Apache2

First, install the new mod_wsgi (mod_wsgi-py27.so) via:

sudo mod_wsgi-express install-module

cd /etc/apache2

copy the apache2.conf and other files into that directory. 

sudo a2enmod wsgi-py27
sudo a2enmod reqtimeout

Basic changes are to add <Directory> grants in apache2.conf and lower the log level to info.

Use the supplied wsgi-py27.conf and wsgi-py27.load to launch the 
pyxform_interface code with the appropriate configuration.
Set a high thread count and total connection count.
And set overall request and response data streaming timeouts.

======================================
sudo apt-get tmpreaper

sudo vi /etc/tmpreaper.conf
and comment out the SHOWWARNING=true line

sudo crontab -e

and add these lines:

@reboot mkdir -p /tmp/tmp_www-data && chgrp www-data /tmp/tmp_www-data && chown www-data /tmp/tmp_www-data

0 0 * * 1 tmpreaper --mtime-dir --runtime=480 8d /tmp/tmp_www-data

0 0 * * 1 find /tmp/tmp_www-data -empty -type d -mtime 1 -delete

0 1 * * 1 tmpreaper 30d /var/log/apache2



=====================================
Finally:

cd /tmp
mkdir tmp_www-data
sudo chgrp www-data tmp_www-data
sudo chown www-data tmp_www-data

cd /var/log
mkdir django
sudo chgrp www-data django
sudo chown www-data django

And, lastly, restart the apache2 server:
sudo /etc/init.d/apache2 restart




