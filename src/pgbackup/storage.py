import logging
import boto3
from botocore.exceptions import ClientError
import os


def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close
    infile.close

    try:
        with open(f'{location}/{fname}', 'w+b') as f:
            f.write(output)
    except OSError as err:
        print(
            f"OS error occurred trying to open {location}{fname}\nError {err}")
        sys.exit(1)
    except Exception as err:
        print(f'Unexpected Error: {err}')
        sys.exit(1)


def s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
