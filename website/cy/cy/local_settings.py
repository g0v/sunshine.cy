DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cy', # Or path to database file if using sqlite3.
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@!*_oth(-2$r4-=03lpgv4_$06516hr!+pnba3tvfs#g$d@nwk'
