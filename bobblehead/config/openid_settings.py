from bobblehead.settings.base import DEBUG, LOCAL_TEST

if DEBUG and not LOCAL_TEST:
    REALM_URL = 'http://localhost:8000/'
    RETURN_URL = 'http://localhost:8000/user_profile/udacity_user'
elif not DEBUG and LOCAL_TEST:
    REALM_URL = 'http://localhost:8080/'
    RETURN_URL = 'http://localhost:8080/user_profile/udacity_user'
else:
    REALM_URL = 'http://www.nanoprojects.org//'
    RETURN_URL = 'http://www.nanoprojects.org/user_profile/udacity_user'
