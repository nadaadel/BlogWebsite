#Blog Python Project 
-------------------------------------------
blog website can display most of blogs realted to different category user can read blogs and can liked the blog and dislike 
project code by django framework and responsive web design 
-------------------------------------------
#to run the project 
-------------------------------------------
1- download the repositry
2- create scema and rename it "blogdb"
3- go to project directory and open the terminal and run $ python manage.py makemigrations
4- the run $ python manage.py migrate
5-project will run on 8000 port for example : http://127.0.0.1:8000 
6- got to http://127.0.0.1:8000/blog/home and start the live run 
7- you can start add posts and categories and other featutre from admin panel in url http://127.0.0.1:8000/blog/adminModify

--------------------------------------------
#project prerequisete make sure to install 
--------------------------------------------
1- python package
2- django frame work 
3- Mysqldb python module


--------------------------------------------
#project details
--------------------------------------------
login and registeration 
-------------------------
user can register by unique username and email 

Admin Panel page contains:
--------------------------
users, posts, categories, forbidden words 

When Admin clicks on the Posts Link, It would list all posts and then admin can create post,delete and edit
When Admin clicks on the users Link, It would list all users and then admin can create user,delete
Admin can block normal user or unblock,Admin can't block another admin
Admin can promote a normal user to be an admin and unpromote
When Admin clicks on the categories Link, It would list all categories and then admin can can create category,delete and edit
When Admin clicks on the forbidden words Link, It would list all forbidden words and then admin can create forbidden word,delete and edit

-------------------
Home page contains:
-------------------
Search, Subscribe, Posts, Categories

The user can search with either title or tag.
The home page displays only five posts, and we use the paginator to paginate the rest of the query set.
The user can Subscribe to any category he likes.
When The user subscribe to any category, an Email is sent to his email account containing the user's name and the category's name.

-----------------------
post details page contains
--------------------------
image for post author and post date and user can like or dislike a certain post 
user can make comment and replay for anthor comments 
user can see the tags of post 
there are another feature in comment is a forebidden words for unploite words 

----------------------------------------------------------------------------------------------------------------------
# this project done with 4 team member 
