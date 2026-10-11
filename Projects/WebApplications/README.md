# Python Crash Course - Learning Logs Web App

> [!NOTE]
> Project/WebApplications does not contain all files needed to recreate this project.
> Django generates many files, some may contain sensitive project data, therefore
> I have only included files I have added to or created.


**Chapter 18**  
 - Planning:
   - Writing a specification for the project.
     - Web app called Learning Log
     - Allow users to log the topics their interested in
     - Users can make journal entries as they learn about each topic
     - Home page will describe the site and encourage users to register or login
     - When logged in, a user can:
       - create new topics
       - add new entries
       - read and edit existing entries

 - Preparing: 
   - Set up a venv virtual environment
   - Install and create a new <b><u>Django</u></b> project
     - Create and set up database with manage.py migrate
   - Ensure the new project is working with manage.py runserver, visit site

 - <u>Coding: Creating a Basic Functional App</u>
   - Django generated files with manage.py startapp project
   - Define models, activate models
   - Create project superuser, set up admin site
   - Mapping urls, adding views, creating html pages
     - extending html pages from a base html page

**Chapter 19**  
 - <u>Coding: Onwership and Related Access Restrictions</u>
   - Allowing users to add new topics
     - Users own and only see topics they created
     - Users can only add entries to their owned topics
     - Users can only edit their own entries

**Chapter 20**  
  - <u>Coding: Styling and Deploying</u>
    - While in virtual environment: pip install <b>django-bootstrap5</b>
    - Completely refactor base html with bootstrap styling
      - All pages have collapsible nav bar and page header
    - Refactor accounts and learning logs pages with bootstrap styling
      - Index gets a jumbotron to encourage registration and log in
      - Entries are viewed as a card style
      - Overall general sense of professional styling
  
  - Deploying