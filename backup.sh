#!/bin/bash

source backup.conf

db_list="$1"

while read -r line
do

DBNAME=$line
NOW=$(date +"%d-%m-%Y_%H-%M-%S")
FILENAME="$HOSTNAME""_""$DBNAME""_""$NOW"".zip"

./backup.py $HOSTNAME $PORT $MASTER_PWD $DBNAME $FILENAME

if [ $BACKUP_METHOD == "S3" ]
then
    #S3_PATH=s3://$S3_BUCKET/$S3_PATH/
    #aws s3 mv $FILENAME $S3_PATH
    ./upload_s3.py $FILENAME
elif [ $BACKUP_METHOD == "NC" ]
then
    ./upload_nc.py $FILENAME
fi

rm $FILENAME

SLACK_MESSAGE="Odoo database \"$DBNAME\" on server \"$SERVERNAME\" has been successfully backed up to Amazone S3 Bucket \"$S3_BUCKET\"."
curl -X POST --data-urlencode "payload={ 'text': '$SLACK_MESSAGE',}" $SLACK_HOOK

done < "$db_list"

exit $?

