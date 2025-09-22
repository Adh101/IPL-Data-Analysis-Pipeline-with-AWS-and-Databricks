# ingest.py — upload all tables to S3
import os, io
from datetime import datetime
import datadotworld as dw
import boto3
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    token = os.getenv("DW_AUTH_TOKEN") or os.getenv("DW_API_TOKEN")
    if not token:
        raise RuntimeError("Set DW_AUTH_TOKEN or DW_API_TOKEN in .env")
    os.environ["DW_AUTH_TOKEN"] = token

    dataset = os.getenv("DW_DATASET", "raghu543/ipl-data-till-2017")
    bucket  = os.getenv("S3_BUCKET")
    prefix  = (os.getenv("S3_PREFIX") or "").rstrip("/")
    if not bucket:
        raise RuntimeError("Set S3_BUCKET in .env")
    return dataset, bucket, prefix

def s3():
    return boto3.client("s3")  # uses your aws configure / env / role

def upload_df(bucket: str, key: str, df):
    buf = io.StringIO()
    # optional normalization:
    # df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df.to_csv(buf, index=False)
    s3().upload_fileobj(io.BytesIO(buf.getvalue().encode("utf-8")), bucket, key)

def pull_all_and_upload(dataset: str, bucket: str, prefix: str):
    ds = dw.load_dataset(dataset)  # loads all tabular resources into dataframes
    date_part = datetime.utcnow().date().isoformat()
    base = f"{prefix}/{dataset.replace('/','_')}/{date_part}" if prefix else f"{dataset.replace('/','_')}/{date_part}"
    uploaded = []
    for name, df in ds.dataframes.items():
        key = f"{base}/{name}.csv"
        upload_df(bucket, key, df)
        uploaded.append((name, len(df), key))
    return uploaded

if __name__ == "__main__":
    dataset, bucket, prefix = load_env()
    uploaded = pull_all_and_upload(dataset, bucket, prefix)
    for name, nrows, key in uploaded:
        print(f"Uploaded {nrows:,} rows from '{name}' -> s3://{bucket}/{key}")
