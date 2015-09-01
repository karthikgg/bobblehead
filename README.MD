Bobblehead - Student Project Idea Sharing Hub

This is a platform for posting and browsing project ideas (outside regular coursework for online education like Udacity, Coursera, etc.). The idea originated fromt the fact that after completing the Udacity nanodegree program, where do students go to advance their skills? Bobblehead portal will allow students to connect and share ideas, and maybe even collaborate on projects.


PREREQUISITES: 

- Python 2.7+
- Django 1.8
- python-openid 2.2.5
- SQLLite database (Django takes care of that, we want to change to POSTGRESQL)


KEY FEATURES:

- Project will have the following fields: "name", "instructions"/"description", "tags", "articles"/"helpful links", "complexity", "project type", "recommended people on project"
- You can see who created the project

- Users will be able to log in by authentication with Udacity using OpenID 
- Users will be able to create projects 
- Users will be able to delete the projects they have created
- Users will be able to edit projects, if they have created them

- Users will be identified by an email address, along with name, last name
- User will have a profile, which will indicate the nanodegree the user is on 
- User profile will show how many projects they have added
- User profile will show how many projects they have worked on, along with link to repo (if provided)
- User profile will show how many people like/dislike their solution


API ENDPOINTS:

- webapp/projects_JSON
	- JSON of all projects 
		- category (project category - student project, Udacity project, etc)
		- articles list
		- collaborators (# of collaborators)			
		- description (description of project)
		- title (of the project)
		- tags list
		- user (who created it) id
		- posted on (date)
		- model (webapp.project model)
		- pk (primary key)


- query_projects(request, filters)
	- Returns JSON object similar to projects_JSON, but for filters
	- filter has "type", "property", "value"
	- filters can be combined (logical AND)
	- filter type can be of type "order" (in case you want to order based on a field) or "filter" (to filter based on values)
	- define filters as below (each 'dictionary' is a separate filter, FILTER variable is the combination of 3 filters:
		FILTER = [
		    {
		        "type": "order",
		        "property": "posted",
		        "value": "a"
		    },
		    {
		        "type": "filter",
		        "property": "collaborators",
		        "value": "1"
		    },
		    {
		        "type": "filter",
		        "property": "user",
		        "value": "pshev@gmail.com"
		    }
		]

TO DOs:

Aug 27, 2015
1. create difficulty level parameter to Projects model
2. update the projects API endpoint - simplify API endpoint - title, date, difficulty, tags, username and email, project_id (primary key), description, (don't need articles, don't need collaborators, etc.)
3. Change filter/order to :
- Filter by difficulty (add difficulty)
- Filter by tag (search and send back)
- Order by date

4. Backend for tags and resources (URL)
5. tags should API endpoint that returns all tags
	- filter by tags API endpoint? 
6. redirection to desired url after logging in.
7. 

Aug 12, 2015
- Tags and Articles - comma separated tags and new text box per article (how to do this?)
- If a user gets added to a project but doesn't exist in the database, add only the email address or create an inactive profile, or something?
- Front end work - styling, templating
- API calls to filter through the projects (for index.html)
- Users can delete the projects they have created if there are no submissions
- Users can edit their submissions
- Users can comment on submissions and projects (rate projects and submissions too!)


July 28, 2015 	
- Add a link to LOGOUT the user - figure out how to log out if server closed. 
- Add Auth providers
- Add ability to create multiple tags on the fly (while creating project, currently
they need to be pre-created)
- Update user profiles to show projects the user has added, and the projects the user is working on or has worked on
- Better UI
- move all user interaction to the user_profile app (out of webapp)				
