This is a Django web interface for [pyxform](https://github.com/UW-ICTD/pyxform) (the xlsform converter for ODK Collect).

Installation
============

- Setup a Django server and project:

See config/README.txt for all the details.

Maintenance
============

Logs are stored in `/var/log/apache2` and `/var/log/django` and may need to be periodically removed to free up disk space.

Forms are stored in the `/tmp/tmp_www-data` directory, and may need to be periodically removed to free up disk space.

This doesn't need to happen very often. AWS instances come with an ~8GB drive mounted.
[tmpreaper](http://manpages.ubuntu.com/manpages/hardy/man8/tmpreaper.8.html>) can be used to remove older forms that are unlikely to be accessed.

## Updating the server

To get the latest server packages and libraries, run:

```bash
sudo apt-get update
sudo apt-get upgrade
```

To update the pyxform_interface files:

```bash
#cd to the pyxform_interface directory
cd ~/django/xlsform/xlsform/pyxform_interface
#get the latest copy of this repo
sudo git pull
#install the latest version of pyxform from the repository listed in requirements.pip
sudo pip3 install -r requirements.pip
#restart apache for changes to take effect
sudo apache2ctl graceful
```
The [UW-ICTD pyxform repository](https://github.com/UW-ICTD/pyxform) will be used for the update.
This can be set to another repository in the requirements.pip file.

