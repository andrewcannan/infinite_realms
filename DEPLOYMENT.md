# Deployment, Local Development and Version Control
----------------

<img src="./documentation/responsiveness/responsive-mockup.png">
<br><br>

**[Link to the Deployed Site](https://infinite-realms-366e4ca2f09e.herokuapp.com/)**
<br><br>
----------------

## Contents
----------------

* [Deployment Steps](#deployment-steps)
    * [Install Project Requirements](#step-1-install-project-requirements)
    * [Set Up External Database on ElephantSQL](#step-2-set-up-external-database-on-elephantsql)
    * [Heroku Setup](#step-3-heroku-setup)
    * [Connect Database to GitPod](#step-4-connect-database-to-gitpod)
    * [Fixtures](#step-5-fixtures)
    * [Create Superuser](#step-6-create-superuser)
    * [ Generate SECRET_KEY](#step-7-generate-secret_key)
    * [Deploying to Heroku](#step-8-deploying-to-heroku)
    * [Set Up Amazon Web Services (AWS) S3](#step-9-set-up-amazon-web-services-aws-s3)
    * [Connect Django to S3](#step-10-connect-django-to-s3)
    * [Set Up Stripe](#step-11-set-up-stripe)
* [Forking Repository](#forking-the-github-repository)
* [Make Local Clone](#making-a-local-clone)
* [Version Control](#version-control)


<br><br>

## Deployment Steps
----------------

Infinite Realms is deployed on Heroku and utilizes AWS S3 for static file storage.

### Step 1: Install Project Requirements

1. In the root directory of the project create a requirements.txt file containing project dependencies using:

```bash
pip3 freeze > requirements.txt
```
<br><br>

### Step 2: Set Up External Database on ElephantSQL

1.  Navigate to [ElephantSQL.com](https://www.elephantsql.com/) and click "Get a managed database today."

2.  Select "Tiny Turtle" and click "Try now for FREE."

3.  Log in with GitHub and authorize ElephantSQL.

4.  Create a new team with your desired name, agree to the terms, provide your email, and click "Create Team."

5.  Create a new instance.
<br><br>

### Step 3: Heroku Setup

1.  Go to [Heroku.com](https://www.heroku.com/) and log in.
2.  Click "New" > "Create new app." Add a name and select your location.
3.  Add `DATABASE_URL` in the settings under "Config Vars" with value of the URL from ElephantSQL"
<br><br>

### Step 4: Connect Database to GitPod

1. If using `env.py` file to store environment variables, add the following:

```python
os.environ.setdefault("DATABASE_URL", "the_copied_database_url")
```

Alternatively, add as a GitPod environment variable if using GitPod.

2. Install `dj-database-url` and `psycopg2`:

```bash
pip3 install dj_database_url==0.5.0 psycopg2
pip3 freeze --local > requirements.txt
```

3. In `settings.py`, import `dj_database_url`:

```python
import os
import dj_database_url
```

4. Temporarily replace the default database setting by commenting it out and adding:

```python
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

5. Verify the connection with:

```bash
python3 manage.py showmigrations
```

6. Then apply the migrations:

```bash
python3 manage.py migrate
```
<br><br>

### Step 5: Fixtures

If you manually added data via the Django admin and didn't use fixtures, you'll need to transfer the data from GitPod to your new database using the `dumpdata` and `loaddata` commands.

#### Dumping Data

1.  Ensure GitPod is connected to SQLite by temporarily commenting out the `DATABASE_URL` settings in `settings.py`:

```python
# if "DATABASE_URL" in os.environ:
#    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
# else:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
```

2.  Save the `settings.py` file.

3.  With GitPod connected to SQLite, use the following command to dump data from a specific app:

```bash
python3 manage.py dumpdata app_name > filename.json
```

For example, to dump data from the `products` app:

```bash
python3 manage.py dumpdata products > products.json
```

#### Loading Data

1. After dumping the data, you can now load it into the new database.

```bash
python3 manage.py loaddata products.json
```

2. You should see a confirmation message like:

```bash
Installed X object(s) from 1 fixtures
```

If you have multiple apps with interdependencies, ensure you load data in the correct order to avoid fixture errors.

If you used fixtures for your project, reconnect GitPod to the external Postgres database by uncommenting the `DATABASE_URL` settings in `settings.py`.

```python
if "DATABASE_URL" in os.environ:
    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```

Then, run `python3 manage.py migrate` to ensure migrations are made to the external database.

Then, follow steps to load data outlined above.
<br><br>

### Step 6: Create Superuser

```bash
python3 manage.py createsuperuser
```
<br><br>

### Step 7: Generate SECRET_KEY

1. Generate a new secret key at https://djecrety.ir/.

2. Add this as a new Config Var on Heroku.

3. Add the same variable to either your `env.py` file or GitPod environment variables.

4. Then, adjust the variable `SECRET_KEY` in `settings.py` to:

```python
SECRET_KEY = os.environ.get('SECRET_KEY', '')
```
<br><br>

### Step 8: Deploying to Heroku

1. Install `gunicorn` and add it to `requirements.txt`:

```bash
pip3 install gunicorn
pip3 freeze > requirements.txt
```

2. Create a `Procfile` with:

```makefile
web: gunicorn infinite_realms.wsgi:application
```

3. Temporarily disable `collectstatic`:

```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name
```

Alternatively, add DISABLE_COLLECTSTATIC with a value of 1 to Heroku Config Vars

4. Add the Heroku app's hostname to `ALLOWED_HOSTS` in `settings.py`.

Add, commit, and push changes to GitHub, then deploy to Heroku with:

```bash
git push heroku main
```
<br><br>

### Step 9: Set Up Amazon Web Services (AWS) S3

1. Creating an AWS Account

*  Visit [aws.amazon.com](https://aws.amazon.com/) and click on "Create an AWS Account."
*  Provide your email, create a password, and choose a username for your account. Click "Continue."
*  Select "Personal" for the account type and fill out the required information. Click "Create Account and Continue."
*  Enter your credit card information for billing if the account exceeds free usage limits.
*  Complete the verification process, confirming all necessary details.

2. Creating a Bucket

*  Sign in to your AWS account and find S3 using the search bar. Select and navigate to S3.
*  Click "Create Bucket" and in the General Configuration section, give your bucket a name (preferably matching your project). Choose a region closest to you.
*  Under Object Ownership, select "ACLs enabled" and choose "Bucket owner preferred."
*  In the Block Public Access settings section, uncheck "Block all public access" and acknowledge that this may make the bucket and objects public. Click "Create Bucket."
*  Select the newly created bucket, go to the "Properties" tab, and scroll down to "Static Web Hosting." Enable static web hosting, check "Host a static website," and add "index.html" and "error.html" as Index and Error documents respectively. Click "Save."
*  Open the "Permissions" tab and copy the ARN (Amazon Resource Name).
*  Navigate to the Bucket Policy section, click "Edit," and select "Policy Generator." Choose S3 bucket policy as the policy type. Add `*` for the principal and select "GetObject" from the Actions dropdown.
*  Paste the ARN into the ARN input field and click "Add Statement." Generate the policy, copy it, and paste it into the bucket policy editor. Add `/*` at the end of the resource value to allow access to all resources. Click "Save."
*  In the CORS section, apply the provided CORS configuration.

```json
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

3. Creating IAM Group, Policies, and Users

*  Find IAM using the search bar and navigate to IAM to create a group, access policy, and user.
*  Create a group with a name (e.g., `manage-infinite-realms`).
*  Create a policy by importing the pre-built "AmazonS3FullAccess" policy and customize it with the S3 ARN.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*",
            ]
        }
    ]
}
```

*  Attach the policy to the group.
*  Create a user (e.g., `infinite-realms-staticfiles-user`) with programmatic access.
*  Add the user to the group and complete the user creation process.
*  Download the .csv file containing the user's access key and secret access key for authentication in your Django app.

This process sets up Amazon S3 for hosting static files and images, allowing your Django application to utilize AWS services for file storage.
<br><br>

### Step 10: Connect Django to S3

1. Install `boto3` and `django-storages`, and add them to `requirements.txt`.

```bash
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```

2. Configure AWS settings in `settings.py`.

```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

3. Create `custom_storages.py` and set storage classes.

```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

4. Set static and media in `settings.py` and override static and media URLs.

```python
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

5. Add AWS keys from the downloaded `.csv` file to Heroku Config Vars. Also, setting a variable `USE_AWS` to value `True`.

6. Remove `COLLECTSTATIC` variable from Heroku Config Vars.

7. After saving the settings.py file, ensure you've added all these modifications, commit them, and proceed to perform a `git push`. This action will automatically trigger a deployment on Heroku. Upon checking the build log, you'll observe that all static files were successfully collected.

8. Media files will need to be uploaded to the S3 bucket in a folder called `media` and granted public read access.
<br><br>

### Step 11: Set Up Stripe

1. Obtain API keys from Stripe and add them as Heroku Config Vars.
2. Set up webhooks on Stripe dashboard and add endpoint URLs and add this key to heroku.
<br><br>

## Forking the GitHub Repository
----------------

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.
<br><br>


## Making a Local Clone
----------------

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
<br><br>

## Version Control
----------------

Workflow controlled using Git and GitHub. It helps you track different versions of your code and collaborate with other developers. Version control allows you to keep track of your work and helps you to easily explore the changes you have made.

You can think of a repository as a “main folder”, everything associated with a specific project should be kept in a repo for that project.
You will have a local copy (on your computer) and an online copy (on GitHub) of all the files in the repository.

Once Changes on your local copy have been saved they can be added to the staging area using ```Git -add```. And then committed using ```Git commit``` along with your message, meaning they will be saved as a version of the repository which is then ready to be pushed, using ```Git push```, up to the online copy of your repository.
<br><br>