import logging
import boto3
from botocore.exceptions import ClientError
import os


def local(dbData, outfile):
    outfile.write(dbData)
    outfile.close


def s3(dbData, bucket, name=None):
    print('Uploadinb backup to s3 bucket')
    s3 = boto3.client('s3')
    # If S3 name was not specified, use file_name
    if name is None:
        name = os.path.basename('backup.tar')

    # Upload the file
    try:
        s3.upload_fileobj(dbData, bucket, name)
        print('Finished Uploading!')
    except ClientError as e:
        logging.error(e)
        return False
    return True
