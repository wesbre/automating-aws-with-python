#  Create Bucket

 new_bucket = s3.create_bucket(Bucket='automationaws-wb-website',CreateBucketConfiguration={'LocationConstraint': session.region_name})

# Upload Files
new_bucket.upload_file('index.html', 'index.html', ExtraArgs={'ContentType': 'text/html'})

# Adding policy
policy = """
    ...: {
    ...:     "Version": "2012-10-17",
    ...:     "Statement": [
    ...:         {
    ...:             "Sid": "PublicReadGetObject",
    ...:             "Effect": "Allow",
    ...:             "Principal": "*",
    ...:             "Action": [
    ...:                 "s3:GetObject"
    ...:             ],
    ...:             "Resource": [
    ...:                 "arn:aws:s3:::%s/*"
    ...:             ]
    ...:         }
    ...:     ]
    ...: }
    ...: """ % new_bucket.name

# Update policy on s3
policy = policy.strip()
pol = new_bucket.Policy()
pol.put(Policy=policy)