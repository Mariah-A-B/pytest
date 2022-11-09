import comp630 
import logging
import boto3

def s3_upload(profile, file_name, bucket, object_name=None):
    session = boto3.Session(profile_name=profile)
    if object_name is None:
        object_name = file_name
    s3 = boto3.client("s3", region_name="us-east-1")
    try:
        response = s3.upload_file(file_name, bucket, object_name)
        print(f'Upload Response: {response}')
    except ClientError as e:
        logging.error(e)
        return False

    return True

def s3_download(profile, file_name, bucket, file_out):
    session = boto3.Session(profile_name=profile)
    s3 = boto3.client("s3", region_name="us-east-1")
    try:
        s3.download_file(bucket, object_name, file_out)
        print(f'Download Response: {response}')
    except ClientError as e:
        print(e)
        return False

    return True