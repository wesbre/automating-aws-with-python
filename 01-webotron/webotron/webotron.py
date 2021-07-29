import boto3
from botocore.retries import bucket
import click
from click.termui import prompt



session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')


@click.group()
def cli():
    "Webotron deployes websites to AWS"
    pass
@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_object(bucket):
    "list objects in an s3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    #list_buckets()
    cli()
