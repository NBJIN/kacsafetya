# KACSafety

## About

#### This is a fictional website for educational purposes for a health and safety training company called KAC Safety.  The comapny provides consulation in realtion to health and safety but also provides training courses in which a visitor can view the details on each course and purchase same through a stripe payment process.  The company offers both online and classroom based courses in health and in safety.  This is a full stack e commerce project.  The following languages have been used while building this project: Django, Python, Html, CSS and JavaScript.


## UX

#### When researching the UX principles and thinking about the clients needs, the target audience and what needs to be included so that they would benefit from same I considered the following.

#### Bearing in mind that this is a start up and more courses will be added over time as the company and website evolves but the target audience for this site are as follows:
#### -	Companies and Private clients in the health and construction industries 
#### -	Companies interested in providing health and safety training to their employees to ensure compliance with legal requirements and to create a safe and health work environment.  
#### -	Health and Safety courses are essential for promoting workplace safety and prevent accidents and injuries and by undertaking these courses they can benefit both individuals and the company by providing the knowledge and skills necessary to maintain a safe and health work environment.  
#### -	Private clients who are looking to upskill in order to gain a promotion or a change of career or maybe to stay up to date with industry standards.  .  
#### -	Also by offering courses online there is the opportunity to reach a wider audience including people who might not be able to attend in person classes due to time constrains and location 
#### -	Also with an online offering thee is the potential of increased revenue. 


## What the visitors will be looking for:

#### - -	Visitors to the site are looking for a an ecommerce site that provides easy access to a range of courses and training materials that are relevant to their individual needs.  
#### -	An information source which has a bank of courses in relation to health and safety 
#### -	Visitors will require some detail on each course selected.
#### -	Visitors will want to see the cost of each course. 
#### -	Visitors will also want to know whether the course is delivered online or in classroom setting.
#### -	Select a training date for a specific course 
#### -	And be able to carry this selection through to the checkout process 
#### -	Be able to set up an account if they are a frequent visitor to the site so that they can view order history 
#### -	Be able to keep up to date with company announcements by way of newsletter and social media link 
#### -	Be able to easily naviage around the site to view the specific information that a user want to see.


## Agile Development 
#### Github was used to record the project milestone / epics and the kanban board within github was used to record all the user stories for the project. 


### User Stories
#### This project has 5 Milestone and they are as follows: 
#### 1	Project Planning Design and Setup (Admin)
#### 2	Authentication & Access (Admin and User)
#### 3	Functionality (Admin and User)
#### 4	Management of courses and site (Admin)
#### 5	Testing and Deployment (Admin)

#### Each one of the above Milestones/Epics are further divided down into their own user stories: 

### Milestone/Epic : Project Planning Design and Setup (Admin)
#### -	#2 Developer – Document project user requirements, scope and goals – (This was entered twice by mistake under the project milestone above)
#### -	#3 Developer – Create wireframes, mock-ups, layouts and interface, user stories and kanban board. 
#### -	#4 Developer – Setup project workspace on hosting platform 

### Milestone/Epic : Authentication & Access (Admin and User)
#### -	#5 (35) Admin have full access to the site 
#### -	#6 Admin – Manage user accounts
#### -	#7 User – Register for a new account
#### -	#8 User – login to account
#### -	#9 User – Manage Account Information 
#### -	#10 – User – Reset password 


### Milestone/Epic : Authentication & Access (Admin and User)
#### -	#11 User – View full list of courses
#### -	#12 User – View the course in more detail
#### -	#13 User – Search courses by category 
#### -	#14 User – Search courses by location
#### -	#15 User – Add courses to bag 
#### -	#16 (36) User – View courses in bag 
#### -	#17 User – Change qty in bag 
#### -	#18 User – Enter payment details
#### -	#19 User – See order confirmation 
#### -	#20 User – See order history on login 
#### -	#21 User – Make purchase without registration 
#### -	#22 User – Sign up to company newsletter
#### -	#23 User – Submit a contact form 
#### -	#24 User – Access company social media page 
#### -	#25 User – See confirmation of actions completed 
	
### Milestone/Epic : Management of courses and site (Admin)
#### -	#26 Admin – Add new courses
#### -	#27 Admin – Edit a course 
#### -	#28 Admin – Delete a course 
#### -	#29 Admin – Update general content 
#### -	#30 Admin – Manage in-coming orders 
#### -	#31 Admin – Manage all in-coming contact requests

### Milestone/Epic : Testing and Deployment (Admin)
#### -	#32 Developer – Test all parts of the Django site 
#### -	#33 Developer – Deploy successfully
#### -	#34 Developer – Ensure site is responsive 

#### - Please see screenshots below of Kanban board from Github
#### - This is a full list of all user stories on github at the start of the project.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/97b0aabe-06b7-4cb8-a191-30aeb132c35d)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8fa6578d-735e-4261-928f-6005f5d4b184)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/71d9cf8e-91d8-49ec-b48f-3f47af2ab969)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b732b6b8-c426-4889-aecc-4c6879ac9dfb)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/21e0979e-36f8-4d2e-83d8-d74381cfe141)

#### - Presently this is the status of the kanban board in github.
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/31ceca72-5d33-4d63-ab34-59b90c3d9ade)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/38bce8f5-69cc-4627-8334-22e843f3c541)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a74c4049-7ac0-432f-a05b-01a3aed2a13b)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e506e76f-1e45-493e-bdca-108298743275)

### Product Backlog

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3eb6a500-4b6a-4304-890a-b65df0c556d4)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0d998bfa-8ed6-459d-87bd-c1d57af1a1d4)



## Structure 

#### The site is divided into a number of apps so that the user can easily navigate around the site and these are as follows:
#### -  Dashboard - the user can view orders and update shipping information
#### -	Landing – this is the home page for this ecommerce site
#### -	Courses – which contains details about all the courses
#### -	Basket – which will allow user to add their items to the basket and view same 
#### -	Purchase – which is basically the checkout app which collects all the information about the payment for the courses.
#### -	Mailchimpnews - marketing Tool 
#### -	Contact - should a user want to get in contact with kacsafety

## Site map (Diagram showing all pages ************)

## Wireframes
#### All wireframes were created using Balsamiq.  
#### Home Page 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/35b4be24-fdaa-44a4-8c2a-a6ad707a1df9)

#### Sign In Page
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/11cb3cb8-7b8f-4867-a010-a8c3d23d78cc)

#### Sign Up Page
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1238ac32-4adc-4747-bf16-609988db267a)

#### Logout 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9f930e47-7aa6-4376-84b8-41100ebad9f5)


#### All Courses Page 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d9256ef2-225d-4bdc-8be8-cff87c88aa14)

#### Detailed Courses Page - When the superuser is logged in they will be able to 
#### edit and delete courses 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9804d3d7-ea19-4422-835e-e3e01d612ef2)

#### Contact Us 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/fdd053c4-fdee-49e2-aacf-b21fd6185070)

#### Basket
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e754ae74-b5f7-4a5b-bbe2-d84ef0f24f86)

#### Purchase Success
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bb2d6803-a38d-4211-8bda-19fe76f4e311)

#### Newsletter Signup
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ed3c56aa-2a83-4a3b-bb3b-0b5dc555b22d)

#### Add Course Page 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/27e993ad-4125-46bb-b2f7-207d59bdeba2)

#### Edit Course
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4a24b634-4e26-42b9-a280-f5eef5691f76)

#### Dashboard Page 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1217fa51-504f-4146-a9ba-6588e433be8f)



## Database Schema
#### The design for the database were drawn up in draw sql - In total there are 9 tables for this project which are as follows: Courses, Purchase, Purchase_Order, Location, Group_By, UserDashboard, Basket, Mail_Chimp and contact.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8bd0c220-9d12-49f6-a545-4e38689e2a86)

## Business Model 
#### The business model for this ecommerce projects is a Business to Business and Business to Customer (B2B and B2C).  As mentioned above the site is aimed at both companies who are trying to fullfill training and legal requirements and to private clients who want to upskill or career change.  


## Marketing 
### Business Model 
#### The Business Model for this ecommerce project is the provision of an online platform where visitors can view courses in relation to health and safety.

### Purpose of the Ecommerce site 
#### To provide an online presence for the company and also a platform where people can visit and easily browse a range of courses in relation to health and safety, choose the course that matches their requirements and proceed to purchase same.  

### B2B and B2C
#### The ecommerce site focuses on Business to Business and Business to Customer.  It might tend to vere more toward business to business because of the fact many businesses in the health and safety sectors will need to fullfill their training requirements but also legal requirements in relation to health and safety.  There is also a business to customer focus where a visitor might want to update skills, knowledge and possibility of a career change.  

### Core Business Focus
#### -	Provide an online site that is easy to navigate for the visitor
#### -	Providing a bank of courses in relation to health and safety 
#### -	Easy to navigate checkout process



### Marketing Channels
#### -	Each page will provide a link to the companys social media platforms which are Facebook, Twitter, Instagram and Youtube.  These links are located in the footer of each page.  
#### -	By providing a choice of social media platforms it ensure that the company is reaching a wider audience and keeps customers up to date on all company events and updates and allows the company to engage wit their audience.  
#### -	Mail Chimp allows user again to keep up to date with all company updates.  Location 
#### -	Contact Us Form allows the company to engage with their customers and also gives their customers the opportunity to enquire about different course and get extra information.  Location 
#### Below is screenshots of facebook page, contact page and mailchimp signup.
### Facebook 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3b7958e4-b406-47c8-b375-8fed77b3e115)
### Contact Page
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/24100feb-2eea-4b84-993e-4548c476c1f4)
### Mailchimp example
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ce607efd-b517-4607-8f7e-1f56daea84b7)



### SEO – Search Engine Optimisation
#### A sitemap.xml has been included in the root directory of this project.  This will aid search engine crawlers discover and crawl all of the pages on the ecommerce site including those that may be difficult to find through normal navigation or links.  A robots.txt file is also included in the root directory of this project.  This will instruct search engine crawlers which pages or sections of the website should not be crawled or indexed. The following keywords were drawn up for DEV-Tees keyword research - 
 ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a82ab574-4cfc-4d9d-9248-516154a099b8)
 ### These keywords were also put into the meta tag in the base.html page of the project root.  
 ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b02db7dd-dfdd-42dc-abe6-45e70f64f1e6)


## Surface 
### Design Choice 
#### Bootstrap has been used to aid responsiveness of the site 

### Color Schema 
#### The color scheme used on this site is mainly a shade of grey and red.  It allows the content to be shown clearly on the page and in the context of health and safety red is commonly used for warning signs, fire alarms and hazardous material etc to alert people of potential danger and the need for caution.  
#### 
https://mycolor.space/ was used to research these color types.

#### Red Ral Color #CC0000 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a512b104-fe36-4ea1-b312-7baf455aa7cc)

#### Grey Ral Color # CCCCCC
 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a46852c7-5f00-4da3-ae22-a5a3140f0d29)
 
 ### Logo

### Reseached different websites for logo creation and I took inspiration from https://www.canva.com/ - The main colors used in the logo is red / black and white.  The logo sits in the same position on each page in the top left hand corner and will bring the visitor back to the home page when clicked.   

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1f847253-21c5-44fc-9d49-249c5eb4b96e)

 ### Typography 

#### Google fonts was used to research font styles for the project.  The principle font used on the site is *******************************************

## Technologies Used
## Languages
#### -HTML5 - https://en.wikipedia.org/wiki/HTML5
#### - CSS - https://en.wikipedia.org/wiki/CSS
#### - Javascript  - https://en.wikipedia.org/wiki/JavaScript
#### - python - https://en.wikipedia.org/wiki/Python_(programming_language)



## Frameworks, Libraries & Programs Used

#### •	GitHub – project code is stored on GitHub and this is connected to GitPod and Heroku. 
#### •	GitPod – this is the platform where the project is built and then all work that is completed in GitPod is pushed to GitHub in a series of commits which GitPod is also connected to.
#### •	AWS – used to store static files 
#### •	Heroku – is a hosting platform and is again connected to GitHub. 
#### •	Django – the framework which was used to build the project (python web framework)
#### •	Gunicorn – python web server gateway interface (WSGI) HTTP server 
#### •	Allauth – provides authentication and authorisation features for Django 
#### •	Bootstrap – used in design, add styling and focus on making the site responsive across a number of devices.  
#### •	JQuery –  Javascript code 
#### •	Google Font – provide the fonts for the website 
#### •	Font Awesome – used for icons and toolkits
#### •	Balsamiq – used for the production of wireframe
#### •	Draw Sql – used in the production of database design 
#### •	Am I responsive – to check if site is responsive across different screen widths 
#### •	W3C Markup Validator – used to validate HTML 
#### •	W3C CSS Validator – used to validate css 
#### •	Cloudinary – used to store images
#### •	Crispy Forms – used to make it easier to style and manage Django forms.  
#### •	ElephantSQL – cloud-based managed PostgreSQL database service


## Extensions
•	Stripe – payment processing platform 
•	Pillow – python library that provides support for opening and saving many different image file formats



## Testing

## Testing under the following headings 
### Even though there still work to be completed on this project I was able to carry out the folloiwng testing .   
### Validators
#### -	Lighthouse report – Lighthouse was used to evaluate the ecommerce site performance, accessibility, best practices and SEO. The following is a screenshot.
 ![Screenshot of Lighthouse Report](https://github.com/NBJIN/kacsafetya/assets/106515976/47ff3fbf-69a5-4a19-b06b-356f737c4090)

#### -	HTML – code was validated using the W3C HTML Markup Validation 
#### -	CSS – code was validated using the W3C CSS Validation 
#### -	JavaScript – code was validated using JSHint
#### -	PEP8 - At present the PEP8 Sreenshot has all erros with trailing white 
#### - spaces, insertion of lines before functions and classes and removal of extra
#### - line removed. 

### User Stories Testing 
#### Each user story was tested to ensure that it met its intended purpose by ensuring it met its acceptance criteria.  Results of same have been documented. 

### 1 As a developer document project user requirements, scope and goals 
#### Requirements, scope and goals are all recoreded in this readme documents and 
#### discused with user.  

### 2 As a Developer create wireframes and mockups on the layouts and interface and compile list of user stories. 
#### Home Page 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/35b4be24-fdaa-44a4-8c2a-a6ad707a1df9)

#### Sign In Page
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/11cb3cb8-7b8f-4867-a010-a8c3d23d78cc)

#### Sign Up Page
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1238ac32-4adc-4747-bf16-609988db267a)

#### Logout 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9f930e47-7aa6-4376-84b8-41100ebad9f5)


#### All Courses Page 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d9256ef2-225d-4bdc-8be8-cff87c88aa14)

#### Detailed Courses Page - When the superuser is logged in they will be able to 
#### edit and delete courses 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9804d3d7-ea19-4422-835e-e3e01d612ef2)

#### Contact Us 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/fdd053c4-fdee-49e2-aacf-b21fd6185070)

#### Basket
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e754ae74-b5f7-4a5b-bbe2-d84ef0f24f86)

#### Purchase Success
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bb2d6803-a38d-4211-8bda-19fe76f4e311)

#### Newsletter Signup
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ed3c56aa-2a83-4a3b-bb3b-0b5dc555b22d)

#### Add Course Page 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/27e993ad-4125-46bb-b2f7-207d59bdeba2)

#### Edit Course
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4a24b634-4e26-42b9-a280-f5eef5691f76)

#### Dashboard Page 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1217fa51-504f-4146-a9ba-6588e433be8f)

### 3 As a developer I want to be able to setup project workspace on hosting platform using githug and gitpod - installing django, secret key hidden, settings for development and production have been specified in the settings.py 
### Github
-	Login to GitHub and create your new repository 
-	Go to the Repositories tab click on New 
-	Then enter the name of the repository you wish to create 
-	Click on create repository 
-	New repository is now ready to use 

#### Setting Up Django 
This project uses the Django framework 
-	First of all the user needs to install Django so in the terminal enter the command –                        pip3 install django
-	Then to create a new project the user needs to type the following command in the terminal  - django-admin startproject ‘insert your project name here’
-	Then the user needs to add a gitignore file in the command line type the following command – touch .gitignore
-	The user will add the following files to the .gitignore file 
    #### o	*.sqlite3
    #### o	*.pyc
    #### o	__pycache__

-	Then the user needs to run the server to see if base project is running by inputting the following in the terminal – python3 manage.py runserver which will open the 8000 port in which the user will be able to view the base project in the browser when they open this port.
-	The user will then need to run the migrate command by inputting the following command in the terminal – python3 manage.py migrate 
-	The user will then have to create a superuser in order to access the admin panel so that they can view the information for the site and make the necessary changes.  To create a superuser in the terminal the user will input – python3 manage.py createsuperusere. 
-	The user will then be prompted to enter a username, email and a password.
- The secret key needs to be set in the env.py file (this can be generated from a secret key generator for example Djecrety).  In the settings file you will just refrence the secret key which is located in the env.py file.  
- Also add your database url secret from ElephantSQL and add same to the env.py file.  Again reference same in the settings file.  
- The value for the secret key and key for database url will be also set in heroku under config vars.  
-	The user will then make the initial commit to github wit the following commands in the terminal : 
    #### o	git add .
    #### o	git commit -m “initial commit”
    #### o	git push
-	This will push all the setup and changes for this project up to GitHub.

### 4 As an administrator have full access to the site. 
#### The admin user can log by accessing the Dashboard link on the navbar which will then have a dropdown menu where login can be selected.  
 ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c36aa026-1bd3-4be8-b5bc-2286675a6dbf)
#### Once logged in the admin user will have access to Course Administration, My Dashboard and will also be able to logout.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/2d452d72-4296-4e5d-afcd-fbd79c34343c)
#### In the course administration page the admin user will be able to add the details for a new course.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ce28fe95-b688-45c3-944f-187d80aaec13)
### When the user clicks on the add course button the course will be added to the list of courses on the website or the admin user can cancel the page by clicking on the cancel button.  The admin user can also edit a course by clicking on the edit link in the detailed course making the necessary amendments  and updating the details 
##### At the time of testing page was not availabe after deploying to heroku 
##### some of the static files are missing and will need to be looked at.  *************
##### Also the admin user can delete a course by clicking on the delete link on the detailed course above 
#### ******* missing screenshot due to deployment issue 


### 5 As an administrator manage user accounts - As an admin user they have access to the admin panel where they can see all users been reigtered email addresses and orderes placed.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1e21822b-fb68-4e5e-aae5-69c7fb277a28)

### 6 As a user enter my details on a form so that i can register for my own account.  
#### When the user goes to the Dashboard and clicks on Register in the dropdown meanu they will be brought to the Sign Up Page where the user will enter their email, username and password.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7d5c266a-2462-4c2d-9f5b-b09c179491bd)

### 7 As a user I want to be able to login to my account so i can view my details and order history 
#### If the user goes to the Dashboard click on the option to login they will be able to login to their account 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/5f729c74-3caa-4581-b8e7-1b33bb4eb090)
#### Once logged in the user can proceed to My Dashboard in the Dashboard menu and they will be brought to the My Dashboard Page where they can enter shpping details and also see their previous purchases. 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/078ae835-1107-42ba-91fa-d64457f4c313)

### 8 As a user I want to be able to manage my account information so that it is up to date. 
#### In point 7 above the user will be able to enter their details and then click on update information so the information is available on their profile.  When the user makes a purchase it will be recorded in the Purchase records section of the aobve page. 


### 9 As a user I want to be able to reset my password in case i forget same.  
#### When the user goes to sign in they have the option to reset password by clicking on "Forgot Password?" and they can then proceed to reset a new password.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6fe0aa7f-9b29-4bbd-b0ea-7e27c9b34d59)


### 10 As a user i want to be able to view a full list of courses.  
#### To proceed to all courses the user can click on all courses in the navbar at the top of the page.  The learn more button also on the home page will them them to the all courses page.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/30c240cd-638e-4333-bebd-a4db77510e93)
#### the user will then be brought to the all courses page where a list of courses will display but due to deployment issues the courses are not displaying at present.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8b65acff-71ff-4034-9451-a029068acc64)

### 11 As a user i want to be able to view the course in more details so that I can make an informed decision wheather this course is suitable for my needs. #### Once the user navigates to the all_courses page they will see a list of course cards and on each course card there is a link to course details which brings the user to the detailed courses page.  
#### screenshot not available at the minute due to deployment issue 

### 12 As a user search courses by category of healthcare or safety so that i can choose which category is of more interest.  
#### This is located in the all_courses page at the left hand side and there is a Group By search and Location serach.  This feature is not functional at present 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/2d0dbe06-1e9c-4b87-ba74-6dd71bc524b2)

### 13 As a user I want to be able to search by location either online or onsite in the classroom.  
#### From the screenshot in point no 12 this feature is present but not functioning at present.  

### 14 As a user I want to be able to add courses to the basket so that i can clearly see total cose of each course or courses.  
#### When the user navigates to the Basket on the nav bar they can see first of all if they have items in the basket as the amount is displayed under the heading and once they click on the basket link they will be carried to the basket page where they will see items if they have added to the basket. 
 ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ed175545-ae4b-4a16-9453-0d83a4e42a99)
#### if there is not items in the basket they will be brought to the following page.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a3e879c4-379b-41db-9426-8bfb007d1573)

### 15 As a user I want to be able to view all courses in the basket so that i can clearly see the total cose of each course or courses.  
#### When the user clicks on the basket on the nav bar they will be brought to the basket page where they will be able to see the items added to the basket.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3780b411-7ced-41fe-94af-eabedeb3b5dc)

### 16 As a user I want to be able to change the quantity of courses in the bag so that I can accommodate my requirements should they change.  
#### When the user navigates to the basket page they can increase or decrease the amount in the basket with the increment and deincrement option. - see point 15 above for screenshot - The remove link is not currently working on this page.  

### 17 As a user enter my payment details so that I can complete the purchase.  
#### When the user is in the basket page they can proceed to make a purchase and they will be brought to the secure purchase page where they will see their details if they are registered but if they are not registered the user will have to enter their details.    
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a471a384-cd93-4d27-a295-17d80d136ad9)

### 18 See order confriamtion once purchase is complete.  
#### When the user is on the Secure Purchase Page above and they have all their details entered they can then click on Complete Order.  Once this is clicked the spinner will appear on a red background and when successfull will navigate to the purchase success page where the user can see their order. 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a4fdb312-e260-475a-a6c0-d2c4c2ee9ba4)
Purchase Success Page
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a64a65b8-2558-4a0b-a9f8-d98e3cd2d4a5)
#### On this page Total, discount and grand_total and fee do not appear but all other details do appear on the page.  

### 19 User can see an order history once logged in.  
#### Once the user is logged in they will be able to navigate to My Dashboard where they will be able to see a list of purchase records once an order is place.  

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/23a81ef8-da58-455d-a8f7-8538e69d025d)

### 20 As a user I want to be able to make a purchase without having to register 
#### When an unregisterd user accesses the all courses page they can choose a course to go to the detailed view and once on this page they can add the cousre to the basket and proceed to purchase and then purchase success page.  On the screenshot following one can see that the user is not logged in when making the purchase 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d81fd12b-a053-454d-98de-f13846b40674)

### 21 As a user i want to be able to sign up to the company newsletter 
#### On the nav bar at the top of each page there is a link to sign up.  When the user clicks on this link they will navigate to the newslwetter signup page where they will enter their fullname, company and email.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/15e37385-64e8-47a9-b857-e3508fe9af58)
#### Once these details are entered they can then click on the submit button they will be then brought to Newsletter Signup confirmation page.  

### 22 As a user I want to be able to submit a contact form 
#### In the top nav bar there is a link to Contact Us once the user clicks on this link they will be brought to the Contact KACSafety Page where the user can enter their details and their query.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/07a2a497-a7f7-452e-998c-282f33a1d825)
#### Once the useer has entered the details and clicked on submit they will then be brought to the Contact Success Page. 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9fc77033-ef09-4733-840f-79b5bd980327)

### 23 As a user I want to be able to access company social media page 
#### If the user naviages to the bottom footer they will see a list of links for social meida platforms like facebook, instagram, twitter and youtube.  If the user click on the icon of their choice they will be brought to the website page for that social media option. 

Youtube
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f0978a29-e8fb-41a6-a826-e6a445fb1abf)
Facebook
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bce6d3d7-1db6-4242-9e6d-25946f1f4513)
Twitter
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/11b45a84-4445-43c5-9014-2d6407801203)
Instagram
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9c9babe8-8022-46a7-8057-c5eff4182965)

### 24 As a user i want to be able to see confirmation of actions completed.
#### When a user registers, logins etc a message will appear in the top right hand corner.  At present it is only displaying for a second so timing will have to be adjusted. 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b3f03587-2c46-4c0a-b191-3f73365ef54d)

### 25 As an administrator I want to be able to add new courses.  
#### When an administrator logs in they will be able to add courses through the nav link dashboard / course administration.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c548a49b-04ac-4bf9-b89e-1704ff06c642)
#### When the form is completed and the user clicks on the Add Course button 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/29ead29d-d340-46a9-820e-1858ea2cd26e)

#### they will then be brought to the detailed courses page where they will see that course added.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bf2a18c7-1317-4917-b0ff-f24dccf5ba60)

### 26 As an administrator I want to be able to edit a course.  
#### An administrator will be able to edit the courses page from the above link and they will be brought to the edit course page. 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/baad6537-9564-49d9-b9f2-66b918235f31)
#### Here once they have updated the details they can choose update course or cancel.  They will also be able to access the edit course page when the administrator goes to the all courses page then click on course details and the will be brought to the detailed course page where there is an option to edit and delete course.  
#### All courses page which shows the two courses just added (the rest of courses not rendering due to deployment issue at present.)
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e33acaf7-ab16-4384-8852-88948096bfbe)
#### From the above screenshot an administrator can click on course details and then navigate to the detailed courses page where they have the option to edit or delete.  
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/08058f25-89ff-495c-a6c5-123bfc9897e4)

### 27 As an administrator I want to be able to delete a course.
#### Please see user story no 26 above to see the delete option.  

### 28 As an administrator I want to be able to update the general content on all pages 
#### As the administrator the user will be able to access all parts of the site and the admin panel where they will be able to manage users.  

### 29 As an administrator I want to be able to manage all incomming orders.
#### As per point 28 above. 

###  30 As an administrator I want to be able to manage all incomming contact requests. 
#### As per point 28 above 

### 31 As a developer I want to be able to test all parts of the django ecommerce website 
#### In progress not fully completed refer to this readme document.  

### 32 As a developer I want to be able to deploy successfully
#### At present there is an issue with deployement to Heroku due to static file configuration which needs to be resolved.

### 34 As a developer I want to be able to ensure that the site is responsive.  
#### This is a work in progress due to time constraints for this project.  


## Bugs & Items To Be Addressed
#### - There is an issue with deployment and static files and alot of my images and details for my courses are not displaying at present. There are two couses there which i have added durining testing.    
#### - Responsiveness - ran out of time in order to ge this finalised.  
#### - Stripe - When i make a payment It successfully allows me to enter details but when i proceed to the purchase success page it is not bringinig threw my total, discount and grand total.  It is also not bringing threw the course fee for this page.  
#### - On the all courses page the Group By and Location need to be addressed as it is not working. 
#### - I had to leave debug = True in this project in order to get project to display in gitpod. In the Heroku app it is displaying without static and css. Currently trying to resolve an issue with deployment.  


### Features Testing
#### Each feature in the ecommerce site was tested to ensure that it functioned correctly there are some features that still need to be implemented.  

### Responsiveness 
#### The above is a work in progress at the minute which will need to be addressed ran out of time for this project.  


#### Milestone/Epic : Project Planning Design and Setup (Admin)
-	#2 Developer – Document project user requirements, scope and goals – (This was entered twice by mistake under the project milestone above)
-	#3 Developer – Create wireframes, mock-ups, layouts and interface, user stories and kanban board. 
-	#4 Developer – Setup project workspace on hosting platform 

#### Milestone/Epic : Authentication & Access (Admin and User)
-	#5 (35) Admin have full access to the site 
-	#6 Admin – Manage user accounts
-	#7 User – Register for a new account
-	#8 User – login to account
-	#9 User – Manage Account Information 
-	#10 – User – Reset password 

#### Milestone/Epic : Authentication & Access (Admin and User)
-	#11 User – View full list of courses
-	#12 User – View the course in more detail
-	#13 User – Search courses by category 
-	#14 User – Search courses by location
-	#15 User – Add courses to bag 
-	#16 (36) User – View courses in bag 
-	#17 User – Change qty in bag 
-	#18 User – Enter payment details
-	#19 User – See order confirmation 
-	#20 User – See order history on login 
-	#21 User – Make purchase without registration 
-	#22 User – Sign up to company newsletter
-	#23 User – Submit a contact form 
-	#24 User – Access company social media page 
-	#25 User – See confirmation of actions completed 
-	
#### Milestone/Epic : Management of courses and site (Admin)
-	#26 Admin – Add new courses
-	#27 Admin – Edit a course 
-	#28 Admin – Delete a course 
-	#29 Admin – Update general content 
-	#30 Admin – Manage in-coming orders 
-	#31 Admin – Manage all in-coming contact requests

#### Milestone/Epic : Testing and Deployment (Admin)
-	#32 Developer – Test all parts of the Django site 
-	#33 Developer – Deploy successfully
-	#34 Developer – Ensure site is responsive 


## Deployment 
With a fully working django ecommerce project the final steps to hosting the project are as follows:
#### •	First the database is created and this will be completed by using ElephantSQL
1.	Set up an account with ElephantSQL if you don’t have one already else login to your account.  
2.	Access the dashboard on ElephantSQL and click on the button ‘Create New Instance’.
3.	Then set up your plan by giving your plan a ‘Name’ this is usually the name of the project, then select ‘Tiny Turtle (Free) plan’ and then leave the ‘Tags’ field blank.
4.	Next Select “Select Region”
5.	Select a data center near you in this case ‘EU-West-1----’
6.	Then click on ‘Review’
7.	Review your detail again and ensure they are correct then click on ‘Create Instance’
8.	Go to the ElephantSQL dashboard and click on the ‘database instance name’ for the project
9.	Under Details in the section of this page click on copy icon at the right of the url 
10.	Leaving this for a moment we need to create a new database instance 
#### •	Next we will create the Heroku app 
1.	Again if a new user set up and account with Heroku or if you have an account already log in with credentials.
2.	Then click on ‘New’ to create a new app.
3.	Give your app a name and select the region closest to you 
4.	Then click ‘Create app’
5.	Open the ‘settings’ tab in Heroku 
6.	Click on ‘reveal config vars’
7.	Then add the config var ‘DATABASE_URL’ and then paste in the url which would have been copied from ElephantSQL. 
#### •	With the database created in ElephantSQL and app created on Heroku revert back to code specifically to the settings.py file in the project folder in Gitpod (code anywhere if using this IDE) and we need to carry out the steps to connect the db to the local development web server.
1.	In the terminal of the projects Gitpod workspace install dj_database_url and psycopg2 by inserting the following command in the terminal: pip3 install dj_database_url==0.5.0 psycopg2
2.	Update the requirements.txt file with the newly install packages by typing the following command in the terminal – pip freeze > requirements.txt
3.	In settings.py of the project folder import dj_database_url underneath the import os at the top of the page – import dj_database_url
4.	Proceed to the Database section in settings.py – need to comment out the code that is in this section and then enter code that will allow the connection to the new ElephantSQL database. Under the DATABASES commented out code add the following code – 
DATABASES = {
	‘default’: dj_database_url.parse(‘insert the datatbase url here from ElephantSQL’)
}
VERY IMPORTANT – Do not commit this file with your database string in the code this is just a temporary so that a connection can be made to the new database and make migrations.
5.	Back in the terminal run the showmigrations command – this will confirm if connection has been made to the external database.  Type the following command in the terminal – python3 manage.py showmigrations
6.	This will return a list of all migrations – none of these migrations will be checked off 
7.	Migrate the database models to the new database with the following command – python3 manage.py migrate.
8.	Create a superuser for the new database by tying the following command in the terminal – python3 manage.py createsuperuser – it will prompt to enter a username, email and password.  
9.	To prevent exposing the database when a push is done to Github remove the code in the database section in settings.py and set up the original code for sqlite database.  So in setting.py under the database section it should contain the following code:
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }
#### •	Now we need to confirm the database is set up
1.	In ElephantSQL page for your database in the left hand side of the page select ‘BROWSER’.
2.	Click the ‘Table queries’ button select ‘auth_user’
3.	Click ‘Execute’ and you will then see the newly created superuser details displayed which is confirmation that the tables have been created and data can be added.  
#### •	Referring back to the code in the Databases section of settings.py and in particular to counteract the exposing of variable we will add an if statement so that when the app is running on Heroku whet the database URL environment variable will be defined we connect to Postgres and otherwise we connect to SQLite.  
1.	In settings.py and above DATABASES we will add the following code –
 if ‘DATABASE_URL’ in os.environ:
	DATABASES = {
		‘default’: dj_database_url.parse(os.environ.get(‘DATABASE_URL’))
}
else:
	DATABASES = {
		‘default’: {
			‘ENGINE’: ‘django.db.backends.sqlite3’,
			‘NAME’: os.path.join(BASE_DIR, ‘db.sqlite3’),
		}
	}
2.	Next we need to install gunicorn so in the terminal in gitpod type the following code – pip3 install gunicorn
3.	Then freeze the above into requirements file by typing the following in the terminal : pip3 freeze > requirements.txt
4.	Next create the Procfile in the root directory of the project which will tell Heroku to create a web dyno which will run gunicorn and server the django app.  In the Profile file type the following – web: gunicorn ‘name of app’.wsgi:application
5.	Next disable collect static so that Heroku wont start collecting static file when the project is deployed. In the terminal of the project in gitpod type the following command – Heroku config:set DISABLE_COLLECTSTATIC=1 –app ‘app name’.
6.	Add the hostname of the Heroku app to ALLOWED_HOSTS in settings.py in section ALLOWED_HOSTS with the following code – ALLOWED_HOSTS = [‘name’.herokuapp.com’, ‘localhost’]
7.	Next deploy app by typing the following in the terminal -  ‘git add .’ then on the next line ‘git commit -m “name of commit”’ next line ‘git push’ and then finally on the next line  ‘git push Heroku main’
8.	Next type the following line in the termainal – Heroku git:remote -a ‘name of app’
9.	Return and type ‘git push Heroku main’ once you click on return this will print out a log with a link to the deployed app – when you open this link it will contain the deployed app
10.	Next set up automatic deploy in Heroku by clicking on ‘Deploy’ at the top of the screen then click ‘connect to GitHub’ 
11.	Click on ‘search’ to search for the repository once same has been selected click on ‘connect’.
12.	Now scroll down the page and click on ‘enable automatic deploys’ – this ensures that evey times we push to github our code will be deployed to Heroku also.
13.	Generate a secret key for Heroku.  There are many online sources but the source that I have used is ‘https://djecrety.ir/’
14.	Once you have generated the secret key add same to the config vars in Heroku –
SECRET_KEY = ‘paste in generated key from djecrety above’.
15.	Next go back to settings.py and replace the secret key with –
SECRET_KEY = os.environ.get(‘SECRET_KEY’, ‘’)
16.	Next set DEBUG = True only if there is a a development in the environment with the following line of code – DEBUG = ‘DEVELOPMENT’ in os.environ
17.	Then push changes to GitHub.
18.	You can go to Heroku and see the build log of the project and you can view same under ‘more view logs’.
19.	Once this process if finished you will see the link for the app and note saying it was successfully deployed to Heroku.  
#### •	Creating a AWS account – the site needs a place to store the static files and images for the site so we will use a cloud-based storage called Amazon Web Services s3 AWS for short.  
1.	Create a AWS account if you have not an account already else you can login by going to the following page https://aws.amazon.com/console/ and click on my account on the nav menu at the top of the page click on the dropdown and click on ‘AWS Management Console’.
2.	Once logged in you need to search of s3  under the services menu 
3.	When you navigate to the S3 page click on ‘create bucket’  and give it the same name as your Heroku app New we will create a bucket.
4.	Then you need to select a region and select the one that is closest to you.  
5.	Then you need to uncheck ‘Block all public access’
6.	Click on the tick box to acknowledge that the bucket will be public 
7.	Then click on ‘Create Bucket’ and this will bring you to the bucket list page
8.	Locate the bucket that you have just created click on it and  and you will be brought to the settings section
9.	Click on the properties tab and then click on ‘Static website hosting’ (which will give a new endpoint which can be used to access it from the internet) this will open a new dialog box called Static website hosting.  In the input box under Index document type ‘index.html’ and in the input box under Error document type ‘error.html’.  Then click on save.  
10.	Navigate to the permissions tab and then click on ‘CORS configuration’ (this will set up the required access between the Heroku app and this s3 bucket’

***** PUT IN TWO IMAGES 

Then click on Save

12.	Now navigate to the Bucket Policy tab and click on the ‘policy generator’ at the bottom of the screen so that we can create a security policy for this bucket.  
13.	This will bring you to the AWS Policy Generator Page where you will need to input some data.
14.	For step 1 Select Policy Type on this page select ‘S3 Bucket Policy’
15.	Under Step 2  Add Statements we want to allow all principles by adding a ‘*’ to the Principal input box.  For the Actions in this section select ‘Get Object’ from the dropdown menu.  Next you need to revert back to Permissions tab and then to Bucket Policy and  copy the Bucket policy editor ARN:  and paste it it to ‘Amazon Resource Name (ARN)’ input box in Setp 2 of the AWS Policy Generator page. Next click on ‘Add Statement’ .
16.	Unser Step 3 Generate Policy click on the ‘Generate Policy’ button.  A dialog box will open with the Policy JSON document copy the code in this dislog box and then go back to Permissions / Bucket Policy Tab and in the space provided under the heading Bucket policy editor ARN:  paste in the Policy JSON document code.  Add a ‘/*’ onto the end of the resouce key in your code. Finally click on ‘save’ on this page.   
17.	With the configuration for the Bucket Policy and CORS complete it will now allow full access to all resouces in the bucket.
18.	Then navigate to the ‘Acces Control List’ tab and under Public Access select the radio button for ‘Everyone’.  This will then open a diaglog box and click on the checkbox for ‘List object’ and then click on ‘Save’.
19.	Next we need to create a user to acces the bucket 
20.	In AWS got to the services menu open IAM 
21.	Naviage to ‘groups’ in the Dasboard at the left hand side of the screen 
22.	Then click on ‘Create New Group’ and give it a name Group Name : ‘Enter Name Here’ 
23.	Then click ‘Next’ and ‘Next’ again and then click on ‘Create Group’
24.	Next we need to create the policy to acess bucket.  Naviage to Polices on the left of the screen under Dashboard.
25.	Click on ‘create policy’ and naviage to the ‘JSON’ tab 
26.	Click on ‘import managed policy’ at the top of the dialog box 
27.	Then in the search box input ‘s3’ to search for same and then choose ‘AmazonS3FullAccess’ and click on ‘Import’
28.	We just want to allow access to the bucket so Navigate to ‘Services’ on the Nav bar at the top of the AWS page and on the left hand menu choose ‘s3’.  Here you will get the bucket ARN from the bucket policy page in s3
29.	Choose the ‘name of your bucket’ and navigate to ‘Permission’ and ‘Bucket Policy’ and copy the Bucket policy editor ARN: a the top of the large input box.  
30.	Then navigate back to ‘IAM Management Console’ to the ‘JSON’ file and paste the ‘ARN’ after Resoure in square brakets. Its inputted twice in double quotes and the second line has an extra ‘/*’ at the end which adds another rule for all files/folders in the bucket. 
31.	Then click on ‘Review Policy’ on this page 
32.	Give it a ‘Name’ and ‘Description’
33.	Then click on ‘Create Policy’
34.	This will then take the user back to the policy page and you will see a message at the top of the screen that ‘your policy name’ has been created. 
35.	Next attach the policy to the group that was created so navigate to ‘Groups’ under the ‘Dashboard’ then find your group ‘mange-yourgroupname’ and click on ‘attach policy’ then search for the policy that was just created and select it. Click on the tick box next to your policy and then click on ‘Attach Policy’.
36.	Now create a user to put in the group – navigate to ‘users’ on the dashboard and click on ‘add user’.
37.	Then create a ‘user name’ and give the user ‘programmatic access’ and then click on ‘next’. 
38.	Under Add user to group click on the ‘policy for the project’  to attach to the user and then click on ‘next tags’ then ‘next review’ and then click ‘create user’.
39.	This will bring you to the page where there is a success message to say you have successfully created the users shown on this page.
40.	We need to download the csv file on that page as it contain the users access key and secret access key which will be used to authenticate the user from the django app. V.I This file can only be downloaded once and should be completed at this stage.  
#### •	Connect Django to s3
1.	To connect Django to s3  we need to install two packages boto3 and django-storages
2.	Back in our project in Gitpod type the following command in the termianl to install boto3 – pip3 install boto3
3.	And to install django-storages type the following command in the terminal – pip3 install django-storages
4.	Now we need to freeze these requirements so in the teminal type the following command – pip3 freeze > requirements.txt
5.	Then add storages to installed apps in settings.py of your project
6.	We need to add settings to settings.py to connect django to s3 to tell it which bucket it should be communicating with.
7.	Under the media root code we will add an if statement –
If ‘USE_AWS’ in os.environ:
	AWS_STORAGE_BUCKET_NAME = ‘insert bucket name here’
	AWS_s3_REGION_NAME = ‘enter region name’
	AWS_ACCESS_KEY_ID = os.environ.get(‘AWS_ACCESS_KEY_ID’)
	AWS_SECRET_ACCESS_KEY = os.environ.get(‘AWS_SECRET_ACCESS_KEY’)
8.	Now we need to go to Heroku and add aws keys to config variables in the deploy section 

## Github
-	Login to GitHub and create your new repository 
-	Go to the Repositories tab click on New 
-	Then enter the name of the repository you wish to create 
-	Click on create repository 
-	New repository is now ready to use 

## Setting Up Django 
This project uses the Django framework 
-	First of all the user needs to install Django so in the terminal enter the command –                        pip3 install django
-	Then to create a new project the user needs to type the following command in the terminal  - django-admin startproject ‘insert your project name here’
-	Then the user needs to add a gitignore file in the command line type the following command – touch .gitignore
-	The user will add the following files to the .gitignore file 
    #### o	*.sqlite3
    #### o	*.pyc
    #### o	__pycache__

-	Then the user needs to run the server to see if base project is running by inputting the following in the terminal – python3 manage.py runserver which will open the 8000 port in which the user will be able to view the base project in the browser when they open this port.
-	The user will then need to run the migrate command by inputting the following command in the terminal – python3 manage.py migrate 
-	The user will then have to create a superuser in order to access the admin panel so that they can view the information for the site and make the necessary changes.  To create a superuser in the terminal the user will input – python3 manage.py createsuperusere. 
-	The user will then be prompted to enter a username, email and a password.
-	The user will then make the initial commit to github wit the following commands in the terminal : 
    #### o	git add .
    #### o	git commit -m “initial commit”
    #### o	git push
-	This will push all the setup and changes for this project up to GitHub.  

## All Auth 
#### To cover user account for example registration and login the user will use Allauth which automatically handles the user account process.   The steps to installing django allauth are in the attached link: 
https://django-allauth.readthedocs.io/en/latest/installation.html

## Heroku 
#### The user will do the final deployment to Heroku 
#### Login to your account click on the new button and crate new app
#### Choose a name for the app, select the region which is closest to you and click create new app
#### On the resources tab navigate to the Add-ons section and search for Heroku Postgres
#### Select Heroku Postgres then under plan name choose Hoobey Dev free and click submit order form 


#### To use Postgres you will need to install dj_database_url and psycopg2. This should be done in whatever IDE you are using.
#### 1	In your IDE type the command:
pip3 install dj_database_url
#### 2	Then once that is installed type the command:
pip3 install psycopg2-binary
#### 3	Then, to make sure Heroku install all your apps requirements when you deploy it, run the command:
pip3 freeze > requirements.txt
#### 4	Next, navigate to your setting.py file in your main project folder. At the top of the file add the line: import dj_database_url
#### 5	Then scroll down the file till you find your database settings. Comment out the default configuration and underneath insert the code:
#### 6	DATABASES = {
'default': dj_database_url.parse(*Enter Database URL here*)
}
#### 7 The database URL can be found in the settings tab of your app in heroku, under Config Vars. Make sure to have the link in quotation marks
#### 8 If you want to migrate any data from your current database to the Postgres database in Heroku, make sure you run this line before connecting to Postgres:
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
#### 9 Once that's saved, you will now need to run migrations because you have connected to a new database. This is done by running the command: python3 manage.py migrate If you had previously saved your data to import into the postgres database, you can now run the command:
./manage.py loaddata db.json
#### 10	Now that's setup you will now need to create a superuser for the new database. The command is: python3 manage.py createsuperuser Note, once the superuser is created, it's a good idea to sign into the admin panel, locate the user, and check the option that says their email is verified. This is needed otherwise Allauth won't allow the user to sign into the store.
#### 11 Before you commit these changes, you will need to remove the Databases section in the settings.py and uncomment the original database. This is to stop your Postgres database URL from ending up in version control.
#### 12 Now we can create an if statement in our settings.py to run the postgres database when using the app on heroku or sqlite if not. Scroll back to the database section and refactor the code to look like this: 
	if 'DATABASE_URL' in os.environ:
        DATABASES = {
7.	        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
8.	    }
9.	else:
10.	    DATABASES = {
11.	        'default': {
12.	            'ENGINE': 'django.db.backends.sqlite3',
13.	            'NAME': BASE_DIR / 'db.sqlite3',
14.	        }
15.	}



# Credits
## Content
### Content for courses were taken from HSA website.  

## Media
### Most pictures were taken form pexels.com

# Acknowledgements
#### Thanks to our Cohort Facilitator Iris, Class Lead Ivette, to my amazing class mates for their time and knowlege, to the all the patient people in Tutor Assitance and to Student Care.  
#### Also want to say a big thank you to Mentor Sammy and also to Marcel for all their help and support along this journey.  







































