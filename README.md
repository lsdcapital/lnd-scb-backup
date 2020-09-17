# LND SCB Backup

As of lnd v0.6-beta, a new feature called Static Channel Backups (SCB) was implemented. This static backup is needed for the Data Loss Protection (DLP) feature.

For a node recovery you need
- Your wallet seed (people often back this up)
- Your latest SCB (people forget about this, and it contains all the channel information)

See the offical [LND Recovery Guide](https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md) here.

LND safely writes a SCB for us, which we need to backup. Alex Bosworth made a great [LND SCB backup](https://gist.github.com/alexbosworth/2c5e185aedbdac45a03655b709e255a3) script which used inotify-tools to watch for an update. If you are running LND in a VM this is a great option.

I wanted to run my node on Kubernetes (GKE) and ensure I had a backup of the channel file and inotify under K8 isnt a good solution.

LND SCB Backup (lnd-scb-backup) is a python script that connects and subscribes to LND gRPC ChannelBackupSubscription() where it listens for any updates to the ChannelBackup.
When receiving an update it writes the binary multiChanBackup file to a backend provider.

Current providers are
- file
- bucket (Google Bucket)

You can run multiple providers at the same time if you like.

## Installation
pipenv install  
pipenv shell  
./compile_proto.sh  

### Edit lnd-scb-backup.conf
Edit the lnd-scb-backup.conf file

Current backup methods are: (you can have multiple, seperated by a comma)  
method=file,bucket

## TODO
By default we look for a config file lnd-scb-backup.conf. Implement command line args to specify this file  
File: Implement max amount of files for rotation  
AWS: Yeah  
Write the backup verify function (and veryify) on a backup. (I've verified manually, it seems ok)  
Create a Docker build and related K8s files
Implement python logging to properly log to stdout and file (currently cheating in K8 python -u for unbuffered to get stdout)

## Notes
This package was required to pipenv install google-cloud-storage on a RPI 64  
apt-get install libffi-dev
