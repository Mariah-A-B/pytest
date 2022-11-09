import os
import pytest
import boto3
from moto import mock_s3
from botocore.exceptions import ClientError

test_bucket = "s3_kgitlitz_bkt"
test_file = "test.txt"
object_name = "hello"

@mock_s3 
def test_s3():
    session = boto3.Session(profile_name='localstack')
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=test_bucket)

    try:
        response = s3.upload_file(test_file, test_bucket, object_name)
        print(f'Upload Response: {response}')
    except ClientError as e:
        print("error: ", e)
        return False

    x = input("get: ")
    s3.download_file(test_bucket, object_name, "test2.txt")
    return True
