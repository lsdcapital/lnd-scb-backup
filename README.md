# lnd-scb

# Installation
pipenv install
pipenv shell
./compile_proto.sh

# Edit lnd-scb-backup.conf
Edit the lnd-scb-backup.conf file

Current backup methods are: (you can have multiple, seperated by a comma)
method=file,bucket

# File
# Google Bucket
https://console.cloud.google.com/storage/browser/[bucket-id]/

# TODO
By default we look for a config file lnd-scb-backup.conf. Implement command line args to specify this file
File: Implement max amount of files for rotation
AWS: Yeah

# Notes
This package was required to pipenv install google-cloud-storage on a RPI 64
apt-get install libffi-dev
