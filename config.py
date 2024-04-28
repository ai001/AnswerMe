# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR        = os.path.abspath(os.path.dirname(__file__))

BASE_URL        = os.path.abspath(os.path.dirname(__file__) + '/..')

HOSTNAME        = 'localhost'
EXTERNAL_HOST   = 'localhost'
PORT            = 8080
EXTERNAL_PORT   = 8080
# Define the database - we are working with
# MongoDB for this example

THREADS_PER_PAGE = 2

# UID size
UID_SIZE = 10

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "abrakadabra and you will never be able to guess this"

# Secret key for signing cookies
SECRET_KEY = 'abrakadabra and you will never be able to guess this'

# email administrator list
ADMINS = ['afsar.imam@mitie.com']