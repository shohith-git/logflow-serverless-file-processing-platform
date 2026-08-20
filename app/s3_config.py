import os
import boto3

s3 = boto3.client(
    "s3",
    region_name=os.getenv("AWS_DEFAULT_REGION", "ap-south-1")
)

UPLOAD_BUCKET = os.getenv("UPLOAD_BUCKET")
REPORT_BUCKET = os.getenv("REPORT_BUCKET")