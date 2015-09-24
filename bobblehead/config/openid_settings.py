from bobblehead.settings.base import DEBUG

if DEBUG:
	REALM_URL = 'http://localhost:8000/'
	RETURN_URL = 'http://localhost:8000/user_profile/udacity_user'
else:
	REALM_URL = 'http://ec2-52-88-70-138.us-west-2.compute.amazonaws.com//'
	RETURN_URL = 'http://ec2-52-88-70-138.us-west-2.compute.amazonaws.com/user_profile/udacity_user'
