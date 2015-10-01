Bobblehead - Student Project Idea Sharing Hub

This is a platform for posting and browsing project ideas (outside regular coursework for online education like Udacity, Coursera, etc.). The idea originated fromt the fact that after completing the Udacity nanodegree program, where do students go to advance their skills? Bobblehead portal will allow students to connect and share ideas, and maybe even collaborate on projects.


PREREQUISITES: 

- Python 2.7+
- Django 1.8
- python-openid 2.2.5
- SQLLite database (Django takes care of that, we want to change to POSTGRESQL)
- If using PostgreSQL backend 
	- install postgresql http://www.postgresql.org/download/
	- install psycopg2 for talking to postgres thru python
		http://initd.org/psycopg/docs/install.html
	- create a database with a name 
	- create a user for django to access database with
	- open the file config/db_settings.py and fill in the details 
	- some clues here : https://wiki.postgresql.org/wiki/First_steps

- Set 'DEBUG' value in bobblehead/settings/base.py to 'True' if running locally.
- Update config/django_secret.py with the django secret


KEY FEATURES:

- if you want to use SQLite, comment out the links from base.py and local.py
- Don't use SQLite in production!

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
		- user (who created it) email and nickname
		- posted on (date)
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


ISSUES:

Sept 29, 2015
1. Tags and resources with commas should be separated correctly (UI only, backend works correctly) 
	-> (FIXED) 

2. Editing projects have old view and incorrectly populated fields 
	-> (OPEN - Front end) Also, the form is considered invalid! Difficulty missing, and tags list missing. Probably because of the old template

3. submission from newly created project, also has old view
	-> (OPEN - Front end)

4. Submission page has one extra field beside submit, not sure for what it will be used
	-> (OPEN - Front end) this will be taken care of/removed with the new templates

5. Submission: viewing the submission, list of members is missing
	-> (OPEN - Front end) this will be taken care of with the new templates

6. Submission view is old 
	-> (OPEN - Front end) will be fixed with new front end updates

7. Each submission should also display members of the project on the project page, right now it only shows submission links
	-> (Future - Backend) ideall we should be able to see "teams" or "individual" attempts. This needs more work. V2

8.  Submission edit is not working
	-> (OPEN - Backend) lets not worry about submission edit or delete right now. for it to be useful, its implementation is going to be a bit more complicated. See in todos below.

9. After you hit delete and click on X icon, it should redirect back to the project page, right now it goes to the home page
	-> (FIXED - Not an issue?) Once the project is deleted it should redirect to home page, yes??

10. Difficulty field is missing on the projects, both editing and viewing
	-> (OPEN - Front end) Needs to be fixed on front end.

11. Home page filter doesn't filter according to the difficult level, may be because we don't store the difficulty field in the database
	-> (OPEN - Front end) not yet implemented. WIll be done soon on front end.

12. collaborators min should be 1, right now it takes 0 and negative values
	-> (Future - Front/back) Right now we ignore this field. 
	-> (OPEN - Front end) field needs to be removed from edit projects

13. Project page should have both created on and last updated dates, and created by, updated by (if updated by another person?)
	-> Needs to be updated on front end. only the person who created can update/delete

14. Edit project, only title editing seems to be working
	-> (OPEN - Front end) Form is old. Needs the new template before this can work.

15. After editing project, submissions are not shown
	-> (FIXED) we weren't returning the submissions after an edit, only the project!

16. If a person X creates a project, can person Y delete the project? Some one might just delete every project (worst case)
	-> (FIXED) only person who created a project can delete/edit

17. If a person X creates a project, can the person Y edit it? 
	-> (FIXED) nope, only person who created can edit/delete. Don't want random people able to change project details.

18. Project edit/delete. Right now the back end rejects attempts to make changes. 
	The front end should first stop the user from trying as well.
	-> (OPEN - Front end)

19. The website is difficult to use! We need to include more tips or make the design more user friendly. 
	-> (OPEN - Front end/Back end)

20. Edit/delete should be done using templating
	-> (FIXED)

21. Edit projects tags/articles are rewritten instead of appended.
	-> (OPEN -backend)

22. Substrings allowed for tags/articles 
	-> (OPEN - Front end)

23. When looking at a user's profile, the submissions links don't go anywhere
	-> (OPEN - backend)

24. Submissions front end needs updating 
	-> (OPEN - front end)



TO DOs:

Sept 28, 2015
1. comments 
	- add ability for users to comment

2. tag users 
	- in projects and in comments

3. teams/individual submissions
	- Instead of 'submissions' i would like to have 'currently in progress' as well
	- If it is a team project in progress, I would like the viewers to see if there is an opening on the team. Who to contact? Etc. 
	- Individual and teams with 'currently in progress' should be able to have discussions on the submission. Comments.

4. ability to view code, a-la udacity project review. Comment and marking on the code like Udacity's project submissions 

5. More details on submissions. 

Aug 27, 2015
1. create difficulty level parameter to Projects model
	- DONE Sept 1, 2015 - need to update the front end forms to add a 'difficulty parameter'.
2. update the projects API endpoint - simplify API endpoint - title, date, difficulty, tags, username and email, project_id (primary key), description, (don't need articles, don't need collaborators, etc.)
	- DONE Sept 1, 2015
3. Change filter/order to :
- Filter by difficulty (add difficulty)
- Filter by tag (search and send back)
- Order by date

4. Backend for tags and resources (URL)
	- DONE Sept 2, 2015 - added tags.
5. tags should API endpoint that returns all tags
	- DONE Sept 2, 2015 - filter by tags API endpoint added
6. redirection to desired url after logging in.
	- still under work.

7. show teams working on the project at the time

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
