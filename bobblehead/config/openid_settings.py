from bobblehead.settings.base import DEBUG

if DEBUG:
    REALM_URL = 'http://localhost:8000/'
    RETURN_URL = 'http://localhost:8000/user_profile/udacity_user'
else:
    REALM_URL = 'http://www.nanoprojects.org//'
    RETURN_URL = 'http://www.nanoprojects.org/user_profile/udacity_user'
