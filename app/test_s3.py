from s3_config import s3, UPLOAD_BUCKET

try:
    response = s3.list_objects_v2(Bucket=UPLOAD_BUCKET)
    print("✅ Successfully connected to S3!")
    print(f"Bucket: {UPLOAD_BUCKET}")
except Exception as e:
    print("❌ Failed to connect to S3")
    print(e)