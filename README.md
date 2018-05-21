

==================
==      S3      ==
==================

Configuration

Before you can begin using Boto 3, you should set up authentication credentials. Credentials for your AWS account can be found in the IAM Console. You can create or use an existing user. Go to manage access keys and generate a new set of keys.

If you have the AWS CLI installed, then you can use it to configure your credentials file:

> aws configure

Alternatively, you can create the credential file yourself. By default, its location is at ~/.aws/credentials:

> [default]
> aws_access_key_id = YOUR_ACCESS_KEY
> aws_secret_access_key = YOUR_SECRET_KEY

You may also want to set a default region. This can be done in the configuration file. By default, its location is at ~/.aws/config:

> [default]
> region=us-east-1

Alternatively, you can pass a region_name when creating clients and resources.

This sets up credentials for the default profile as well as a default region to use when creating connections. See Credentials for in-depth configuration sources and options.


============================
==   OwnCloud/NextCloud   ==
============================


