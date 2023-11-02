[Link Back to Main Readme Document](README.md)

## NUMBER TO BE INSERTED. Testing
#

## Table of Contents
1. Testing User Stories

2. Code Validation

3. Accessibility

4. Manual and Tools Testing


## 1. Testing User Stories 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| |          |          |          |
|1. Admin User - Set Up Project Workspace  | Installed Django and supporting Libraries, created a new blank Django project and app, set the project to use cloudinary and PostgreSQL and deploy new empty project to Heroku | Pass |          |
|2. Admin User - Complete final project deployment.  | Ensure that final commits are completed, debug changed to false and settings removed under config variables in Heroku. | Pass |          |
|3. Admin User - Be able to set up an account | Create a sign up page where i can enter my username, email and password in order to register and gain access to the blog.   | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/cefa4199-15fc-45b4-89d0-8a56bf948e9d) |          |
|4. As an administrator has full access to the site. | The admin user can log in through the Dashboard link on the menu bar.  This Dashboard link will drop down and give the admin user the option to login once they are logged in they can view, delete, add and edit information on the site.       | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9ea29b15-29b7-4a40-9ec8-2207da0297c6)  |    |
|Once The admin user is logged in will have access to Course Administration, My Dashboard and will be able to logout.   | Once the admin user has logged in all options for eg course administraion, my dashboard and logout becomes available to the admin user.   | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4d25bd09-7572-435b-bb8a-26950dce1e02) |          |
||          |          |          |
|Admin user be able to add details for a course.  | When the admin user is logged in they can choose Course Administration which will bring them to the Course Administration - Add A Course Page   | Pass![image](https://github.com/NBJIN/kacsafetya/assets/106515976/5c6a3753-4358-42ff-aa5c-119823da7183)  |          |
|. Admin user is able to add a course or cancel the add course page. | When the admin user clicks on the add course button the course will be added to the list of all courses on the website or the admin user can also cancel the page by clicking on the cancel button.  | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/779b3155-4d39-4188-9837-41b669d4851d)|          |
|Admin user is able to edit a course by clicked on the edit link in the detailed course page. | On the detailed course page there is an edit button provided for the admin user if they wish to edit a course and once they click on this they are brought to the edit course page.   | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6d09c7dd-5fbc-4b81-a9e7-451082d3ef92)    ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/af3cadab-d948-4177-bdba-b1907519b1ba) |          |
| Admin User is able to delete a course. | On the detailed courses page there is a delete button which the admin user has access to and once this button is selected the course will be delected and the admin user will be brought back to the all courses page with an alert to say that the course has been deleted.       | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f817bdc4-9fc5-49e3-ae59-75ea79191210) |          |
|5. As an administrator be able to manade user accounts. | As an admin user they has access to the admin panel where they can see all user been registered, email addressed and orders placed.     | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9c4a1eaf-cf31-4e24-9d03-184138bf5125)|          |
|6 As a site user be able to register for an account. | When the site user clicks on the Register link in the nav bar under Dashboard the user will be brought to the Sign up page where they enter their email address, username and password.    | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c9ceaedf-73ff-4673-b473-6937e64df75a)
|          | 
|7 As a site user login and see my details.  | Once the user clicks on the dashboard on the nav menu and naviagtes to signin they will enter their details and will then be able to access my dashboard on the menu bar and here they will be able to see their own details.      | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/eff7e7a3-ae52-4538-9625-60935a58c98b)
| Once logged in the user can proceed to My Dashboard where they can enter or update their shipping details and view preious orders.  | Once the user clicks on my dashbaord they will be brought to the my dashboard page.  Here they can enter their details and update them.  Also they will be able to view all their prevous orders that they have made.    | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/42652695-bfd1-4aaf-87ca-0197f87eec99)|          |
| 8 As a user be able to manage account information so that it is up to date. | Once the user reaches the my dashboard page they will be able to update the information and keep their details up to date.  If they want to see how much they have spent on preivous orders all these are saved to the dashboard and the user can view each one. | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9437eed5-8a81-4bf7-bcfc-977145b5cfa6)|          |
| 9 As a user be able to reset password | When the user navigates to the sign in page there is a link for forgot password.  Once the user clicks on this they will be brought to the Password Reset page where they will enter their email address and confirmation will be sent tot the email.   | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/863fe263-7eab-45e0-8f49-33ca8228e521)  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/14ee814e-ff5f-4751-9710-e2acad935724)|          |
| 10 As a user i want to be able to view a full list of courses.         | When the user naviages to the all courses link on the nav bar on the home page or the learn more button on this page they will be brought to the all courses page in which it displays a certain number of courses per page.  Pagination is used to bring the visitor from page to page (of courses).  | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/018f8a15-8840-4d9d-908a-5240d6d0b9c9) ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/04fa3114-6d48-4332-a16c-c1eb57975b74) ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4f7f0113-3828-4996-afc4-876ae1357562)
|          |
| 11 As a user be able to view a course in more detail. | When the user is on the all courses page whether they be logged in or out they can click on a link called Course Details which is displayed on each course summary card.  Once this is clicked the user will be brought to the detailed course page where they can see full details about the course.  | Pass Example of course details link on the course details card ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7b8dfb83-e048-4476-9b8c-51058b3643b7) Example of the detailed course page ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1e38e621-babc-4fa0-8803-3be21be0a5ac)
|          |
| 12 As a user be able to search category of courses. | The user is able to search course by Location and Group By.  Location searched by classroom or online courses and group by searches by health or safety courses.  This search facility is available to users on the all courses page.    | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/cc7f2599-8088-4c80-8c42-5d564902fd94)
|          |
| 13 As a user be able to search by location either online or classroom and group by either health or safety courses. | On the all courses page the the user can click on either online or classroom under the location search and will return the list of preferred courses.  Also there is a search for group by which groups the courses either by health or safety.  This search facility is available on the all courses page. | Pass List of online courses ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/cc7f2599-8088-4c80-8c42-5d564902fd94) List of classroom courses ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9430f98f-87d6-4f03-b5b1-6b796fae4735) list of health courses ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1a95a21e-5e6b-471c-b04a-3b3613386739) list of safety courses ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f9b495fd-d422-4832-8b21-facc20b1e842)
|          |
| 14 As a user be able to add a course to the basket. | The user can add an item to the basket in the detailed courses page.  They will then see the amount undere basket on the navbar and a success message will display to say an item has been added to the basket. Here they will also see the total cost of the items they are purchasing. | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/989cc3db-1964-42e0-8774-a181bbb55b98)|          |
| 15 If there is no items in the basket want to see a balance of 0.00 | if there is no items in the basket they will be able to see this when they see the basket in the nav bar as the amount will read €0.00.  If the user clicks on the Basket they will be brought to the following page. |Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/92bcc968-7298-4ae4-a3d2-6a5759f7ad88)|          |
| 16 As a user i want to be able to see courses in the basket.   | When the user clicks on proceed to payment on the success toast they will be brought to the basket contents page.  Here they will be able to see each course they have added to the basket the amount and the discount applied if any to the basket total.  | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/079b6471-4dd8-4b99-b5fc-b53e0ecd411c) |          |
| 17 As a user i want to be able to change the quantity of courses i have in the basket.   | On the basket contents page under the quanity heading there is an option to increase or decrease the quanity of the course by clicking on the minus and plus signs.  Once the sign is clicked on the user can then click on the update button and this will update the total in the basket.  If they decide they no longer want to go ahead with the course they can remove the course from the basket by clicking on the remove button.   | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/01c7bdf5-24e9-4c62-9dc1-f868ed3346e6) |          |
| 18 As a user i want to be able to enter payment details in order to make a purchase.  | When the user is on the Basket Contents page they can click on make a purchase which will bring the user to the Secure Purchase Page.  If the user is not a registered user they will have to enter all their details along with payment details in order to make a successfull purchase.  They will also be given the option to reigister for an account or even login if its a registered user. If the user is a registered user their details will be prefilled and they will just have to enter the name and card details. This page also shows a summary of the order so the user can see exactly what they have purchased and confirmation of the cost.      | Pass Proceed to payment ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7d6666c0-a854-4875-bb04-2dea1ba7d5ef) Secure Purchase Page ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/888f869d-2842-4a84-97ba-13c32da7770d)|          |
| 19 As a user i want to be able to see confirmation of my order when payment is complete.  | When the user is on the Secure Purchase Page and places an order the loading spinner will then display to show that payment is being processed.  Once the transaction is successfull the thank you for your purchase page will then display which is confirmatiion of the order and payment to the user.       | Pass Loading Spinner ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/12cb4196-5105-4436-aa2d-52aa89f7f678) Thank You For Your Purchase Page ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6b619a11-f61c-4d81-803a-5f0a6b02d32d)|          |
| 20 As a user I want to be able to see my order history once logged in.  | Once a user is registered and logged in they will be able to navigate to the dashboard and then my dashboard on the nav bar.  Here on my dashboard they will be able to see a history of purchases.        | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/66cee049-990d-437b-b51c-5b8fcd06e467)|          |
| 21 As a user I want to be able to make a purchase without having to register.  | When an unregisterd user accesses the all courses page they can choose a course to go to the detailed view and once on this page they can add the cousre to the basket and proceed to purchase and then purchase success page.  On the screenshot following one can see that the user is not logged in when making the purchase        | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/50d3978b-9f1b-4732-ab7a-34913cd8f64a)|          |
| 22 As a user I want to be able to sign up to a company newsletter.  | On the navbar at the top of each page there is a link called sign up.  When the user clicks on this link they will navigate to the newsletter signup page where they will enter their details. Once they have they details entered and submit same they will recived confirmation of signup.  | Pass !![image](https://github.com/NBJIN/kacsafetya/assets/106515976/433fa2c2-9e4b-4aa8-be10-2c1f9fb09939)   ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f04eab86-9b4d-43f9-81ca-7eac304766fe)|          |
| 23 As a user I want to be able to submit a contact form.  | In the top nav bar there is a link to Contact Us once the user clicks on this link they will be brought to the Contact KACSafety Page where the user can enter their details and their query.  Once these details are submitted the user will recieve confirmation to say that their message has been received.    | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c0f04159-5ff9-427b-9412-d330165ae6df)    ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a8ccb9ed-e6df-4256-a2fe-8e2936cfc371)|          |
| 24 As a user I want to be able to access the companys social media page.  | If the user navigates to the footer on any page and click on the facebook link they will be brought to the companys social media pages.   | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c4843732-b3d4-4cc7-8a15-06a4002b69c2)  Youtube ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bde0e16c-6755-4f92-ba95-09b39557d337) Facebook ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/cbc0a2ae-bb80-4827-a838-f961913041c0) Twitter ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/99377b81-ac63-4c8f-a097-8ca61fffae4f) Instagram![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6c3ffbe3-fe61-4310-8afb-750e51d3d11c)    |          |
| 25 As a user I want to be able to see confirmation of actions completed.  | When a user completes an action on the website confirmation of same is displayed back to the user. Attached are some examples  | Pass Successful Signin ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6a87f1bc-3e02-4e03-a699-a6c79a189ed2) Add Couse ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/fc3277d3-81a5-4e26-8767-837cb714f51e) Successful Payment ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6041196d-6045-452b-9275-7565150fc7db) Contact Success ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b26adccd-fda0-4115-acc8-67650f81359f)  newsletter signup ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/34437f01-2d3c-408a-88d3-0941afe036d5)   |          |
| 26 As an administrator I want to be able to add a course.  | When an administrator logs in they will be able to add courses through the nav link dashboard / course administration. When the couse is added the administrator will naviage to the detailed courses page for that course.  | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1e593bd2-c72b-479b-8db0-5308b7b2d746) ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d1c5cd75-493c-47b3-bfd2-e1374dfe960d) |          |
| 27 As an administrator I want to be able to edit a course.  | An administrator will be able to edit a course when they click on edit on the detailed course page. Once edit is clicked they will be brought to the edit course page. Here they will fill in the details and have the choice of editing or cancelling the changes they have completed.  | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/2ab297f0-828f-4707-86d2-89be18437b43) |          |
| 28 As an administrator I want to be able to delete a course.  | An administrator can naviage to the detailed course page there they will see a button to delete a course.  Once they click on the button the course will be deleted and they will navigate back to the all courses page and a message will display to say the course have been deleted.   | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/568a5bc8-85ac-4f96-813a-9d1640f737bb) ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b8f6761c-14b2-497e-9404-60e16537866b)|          |
| 29 As an administrator I want to be able to update the general content on all page.  | The admin user will have full access to the admin panel and also will be able to manage courses from the front end and will be able to update and add content here and through the admin panel.    | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/98f298de-04b5-4475-b921-7a045474c62a) ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0beb5494-f7e2-4297-affb-1471cfd6d630)|          |
| 30 As an administrator I want to be able to manage all incomming orders.  | The admin user will have full access to the admin panel where they can manage orders.      | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/06b2fd64-9325-49e4-85ad-e17cf89e2e29)|          |
| 31 As an administrator I want to be able to manage all incomming contact queries.  | The admin user will have full access to the admin panel where they can manage orders.      | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/06b2fd64-9325-49e4-85ad-e17cf89e2e29)|          |
| 32 As an developer I want to be able to test all parts of the django website.  | Testing of user stories, features, code validation, lighthouse reports have all being carried out and detailed report is contained in this readme file.     | Pass  |          |
| 33 As an developer I want to be able to deploy successfully.  | This project has been deployed to Heroku.     | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9b499754-f851-4d26-8327-eb39fdff409e)|          |
| 34 As an developer I want to be able to ensure that the site is responsive.   | The project is responsive on mobile and desktop (desktop, labptop, i pad air, samsung galaxy and iphone 6/7/8).     | Pass  |          |
<br>



## 2. Code Validation - In carrying out code validation the following was utilised. 
 - HTML code tested using W3C Markup Validation Service - https://validator.w3.org/
 - CSS code was tested using CSS Validation Service - https://jigsaw.w3.org/css-validator/
 - Javascript was tested using JS hint - https://jshint.com/
 - python was tested with Code Institute python pep8 - https://pep8ci.herokuapp.com/#

 #### Starting with HTML below is a screenshot of each page which has been passed through W3C Validator.  
 - 1 Landing Page - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4c3d9792-442c-4630-bce7-f9c2a5be6a6f)


 - 2 all_courses page 1 - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d3fcbb66-c99f-45b6-bc14-af58cf722cf4)


 - 3 all_courses page 2 - No Errors or Warnings 

 ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/471aeeed-9a5f-421d-a799-6259388aaa33)


- 4 all_courses page 3 - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/30f171ff-a12b-4a61-90aa-319c6cdcf281)

- 5 courses/courses/detail (detailed courses page) - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e07b06c1-cb03-4b5d-955c-8ebc70b842d3)

- 6 Contact Us - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/171f81c7-502b-4cd6-b447-773d18d8ed0e)

- 7 Sign Up - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/520dae8d-5e7f-4175-9df0-160bd075fa25)

- 8 Sign In - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/912dd4e1-4c47-4914-b5b8-3ffbda9f9922)

- 9 Accounts / Confirm Email  - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/13e55d73-86a7-439d-af1f-eb6cd85091e2)

- 10 Sign Out - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/64334304-8376-48a1-b212-7c910a6c56d6)

- 11 Course Administration - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1883f236-b9e7-4cc2-bc21-d278a5d4d5af)



- 12 courses/edit (edit a course) - Error

I have an error in my edit course page re date field that its a bad value.  The way 
its shown on the page is the way that the developer wants it to display.  

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b119a15b-d17c-4163-94ec-a2ca264ab494)



- 13 My Dashboard - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f227a0cc-940f-42f4-a76b-e4d6a6bdb9cc)

- 14 Basket - No Errors or Warnings 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/5d913cbc-485b-4c12-afbd-8331a38728f8)

- 15 Sign Up - No Errors or Warning 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/508e3f31-1a7c-4c48-a93d-d0188bdb63c3)


- 16 Secure Purchase Page - No Errors or Warnings 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/44ec480d-9da1-473a-a817-c119122ec1a7)

- 17 Thank You For your Purchase Page - No Errors or Warnings 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/175df36f-c694-4f50-8558-12d630976e61)


- 18 Contact Success Page - No Errors or Warnings 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0da18639-ec9c-4684-99dc-03a36a97f863)

- 19 Newsletter Sign up success - No Errors or warnings 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3b04039d-371e-462e-a435-039277782be7)


### CSS was validated through the W3

- 1 dashboard.css - No Errors Found

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c77e1a14-bd24-4469-9884-9db52a890b32)

- 2 purchase.css - No Errors Found

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1cb74281-4574-41e7-b7b9-fc94470514ca)

- 3 base.css - No Errors Found

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/be8bcaf2-b429-4652-923b-29a765c58e15)

### Python was validated with the Code Institute Python Linter 
No Errors have been found in the validation of python see screenshots 
below.

1 basket / bag_tools.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/db612725-d77b-4cda-8f99-2bc2c19bfcb9)

2 basket / admin.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/24e73b7e-5016-4a68-8957-15047a64ca67)

3 basket / apps.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c61fe361-20ad-4bfe-a7d2-11e1a35c4322)

4 basket / contexts.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/db044656-e0b9-4a6e-afae-c2b2ca6f1081)


![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4b4d7565-255d-440b-b87d-8ba2a38538d3)


5 basket / models.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f15f0fba-32cd-46d3-984f-76c44816c46a)

6 basket / urls.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/01d1f44e-8a4c-4e54-9cdf-3b48427f188f)

7 basket / views.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8f6fc301-ac38-4e64-98ef-00e10ad22646)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c23e4883-640c-427e-84fd-9b9ff189590c)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e5bae9ab-9f0d-4be1-9198-c00ab8ca4147)


8 contact / admin.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/2430e50f-b90e-4fba-853f-e054ecf805e6)


9 contact / apps.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ad748eea-949d-4efd-bf6b-88ada0f629bf)

10 contact / forms.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/55c57853-e11f-46f7-b036-4c1f621e6fc0)

11 contact / models.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f553e1c6-0e78-4273-919a-c1940e421732)

12 contact / urls.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ab530ffc-3e3c-4e23-9235-86a88094704f)

13 contact / views.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d55214dd-b815-4f56-a510-296e0bc31c01)

14 courses / admin.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a0856e81-c2f1-406f-be25-6aa46480114c)

15 courses / apps.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c7849309-f201-4a40-bbb4-3765dfc5c8df)

16 courses / forms.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c797ebe4-12a6-4d0b-9462-9ebdddb86f87)

17 courses / models.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7d0dc948-0206-4eff-ba56-60cca904b9c4)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f1ec24f4-245a-4246-bc39-9322fb994458)

18 courses / urls.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3f5f58db-1f24-4968-88c6-76bfa854a64d)

19 courses / views.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/428dfa88-e350-4361-82cb-ab1170b2f54d)


![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ab54dcfe-7625-44f9-bb70-82ac4d90764e)


![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f3e3288a-f942-4a28-9f8c-9e2d4fd539e4)


![image](https://github.com/NBJIN/kacsafetya/assets/106515976/21085fc8-b93d-47b0-b9dc-408d482b5580)


![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f3568eb1-eb48-4ba0-ba15-73f397c36ad3)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3a150e45-79d3-4dc7-838d-e7ce0f68cfb4)

20 courses / widgets.py

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b2846664-83fb-43f0-9653-fff2b67107af)

21 Dashboard / apps.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0b8509ed-289a-4181-a789-05df0284b30d)

22 Dashboard / forms.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c88d9fbe-55ef-468e-8410-20b9d0d90893)

23 dashboard / models.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/106c0b5c-8616-4355-be70-7d1dca93e989)

24 dashboard / urls.py

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6aaec7a7-cfa9-446a-b154-b94c7edb620e)

25 dashboard / views.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/196ca9ad-9128-4761-8d17-62d2c144e01f)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ecb7eaf8-831f-49f3-8559-d00b94c6db58)

26 Kac_safety urls 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/50524877-74cf-4d3e-b327-729d1d69f788)

27 Kac_safety views.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/59546c63-2860-451b-a3f5-7e590f93c02f)

28 kac_safety wsgi.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f3aef4f2-2546-4ed1-84c1-f71ea8f0e7ab)

29 landing apps.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8f7904b7-9ff8-40b8-8316-df86228e9c83)

30 landing urls.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/44a6fea8-4d7b-4014-b530-acfd4244c3fc)

31 landing views.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/91464aae-8f08-4cb9-bef2-ed58c2cd064e)

32 mailchimpnews admin.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a19e9130-9603-42d5-969e-77b068b1aa3c)

33 mailchimpnews apps.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8f2b89b7-6664-448d-a346-149d65d3b9d1)

34 mailchimpnews forms.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3638799f-4aef-4ae6-844b-7b0f10c2e54c)

35 mailchimpnews models.py 


![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bd0cc841-cab4-43f1-98c5-a5e87bb9d65a)

36 mailchimpnews urls.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9cf4888d-bf08-40b2-a84e-6a8d3f169840)

37 mailchimpnews views.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/91266040-bd74-4e83-8881-be0d1913ba20)

38 purchase init.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a2f86666-5ad8-482e-8526-919826bdccd3)

39 purchase admin.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ff0bac09-d703-4f90-ac66-f0b94220ef6d)

40 purchase apps.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/31968952-cf75-48db-8c07-d12c84eedd7f)

41 purchase / forms.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6fcb09ce-fc11-4771-a8b8-d5e0497b3db5)


![image](https://github.com/NBJIN/kacsafetya/assets/106515976/007e0b19-62dd-4952-b411-7016b2eb7989)

42 purchase / models .py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4d874c40-3fd6-4ffc-89ca-8ffa083e0785)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ac4e7679-a025-41a8-b9a6-e8f813daf0c4)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/dd32f23c-3734-401f-a0e5-1704af3537fb)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6586d48f-336b-4ff5-beb8-9d9405a156a1)

43 purchase / signals.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bb96f4bb-d131-434f-9ba9-8c1cc12d05c0)



44 purchase / urls.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6c6b7cdd-c141-4a63-a214-b93cace09931)

45 purchase / views.py 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f9ab83ff-4faa-4785-94e0-661a74e38aeb)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/57fe844a-7c9c-41e2-9ce3-188cd7c92f43)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/5b7e7101-d0c0-436b-ab8d-a94614cb14be)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ab598048-5062-48cb-a9af-d38db91d57fd)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f067b2f1-fe87-4a2d-bead-42fc17411abb)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/47f0e097-979e-4699-a1a5-eca5a189fab3)

46 purchase / wh handler 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1a912e84-e1f9-4cbe-9a27-1399f33f1c72)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/96ad75d4-5b9f-4e90-b64d-7a5c5a9a8b5d)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e8b45c95-a536-4d4e-8d6b-32c7a1c74037)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7a671a18-c277-431e-8f70-20de785488ec)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/af2809af-096e-41d5-8c17-dbbb8c4cd093)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c2340d98-fe68-4c03-8d86-e38f77156b58)


47 purchase / webhooks.py

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d516aa18-a91d-467e-9a1a-27a2df62885c)

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e6d852e3-3d33-4616-a686-26a771db0cdf)

48 custom storages 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/39e26216-21fe-4a54-959b-36639de98fdc)



### JS HINT was used to validate javascript in the project the following 
### are the findings. 

- 1 basket.html 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c96ba2ef-3c8e-4d19-8719-e2e4eff3a0d9)

- 2 quantity-input-script.html 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ab12b185-389d-4399-838a-3a9d3cc138e4)

- 3 add_courses.html 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b82b6d7f-5427-4216-8641-b076f039ce10)

- 4 all_courses.html 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/29fbd2fd-48f4-4ce5-b9ca-9d176b5647dc)

- 5 edit_courses.html

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/508bab99-0c4f-4013-911d-b2adc174ba45)

- 6 stripe elements js file

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b7472e5f-1a3f-4a28-bed9-000eb2c6ba23)

- 7 email.html file 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ed3e8a6d-6237-4814-918a-b51152df4751)

- 8 base.html 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6e6441d1-3619-4c35-b1a8-79789ae4d518)


### Flake 8 Report 

While running the flake8 report there was a number of items raised in relation to files that the django project generated itself and not coded by the developer.  These files were:
- ./.vscode/arctictern.py 
- ./.vscode/make_url.py
- ./basket/migrations/
- ./contact/migrations
- ./courses/migrations
- ./dashboard/migrations
- ./mailchimpnews/migrations
- ./purchase/migrations


Files which were coded by the developer and are showing up on the flake8
report are below.  


- ./courses/views.py - Had to leave this in as it was affecting the operation of code.  
- ./env.py - tried making these lines of code shorter but it 
was presented errors in the terminal.  
- ./kac_safety/settings.py -  have to leave env in as when i took this out it was presenting an error with the secret key.   
- /kac_safety/settings.py - Again when i went to shorten these
lines of code it presented errors in the terminal.
- ./purchase/apps - had to leave the purchase signals in as without it was causing issues in code.  



## 3. Accessibility

A lighthouse test report was carried out and the results are as follows 
Desktop Accessibility Testing for each page
#### Desktop 
Home Page Desktop

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bea67bf4-c66c-4a46-b965-9a57ab5e9369)

All Courses Page 1 Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1d956193-5743-4c8d-9bf5-0895d11d5170)

All Courses Page 2 Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8666a643-2be7-4a87-a912-6e66f72ecde6)

All Courses Page 3 Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c80018d5-099f-42fc-a397-ef0145dbe77d)

Course Details Page Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4b016a2a-790f-4edf-abdc-e9317b59b99d)

Course Administration Page Destop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/308a1cce-1c52-4eac-9985-bd65696e9507)

My Dashboard Page Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/fc83d13a-b23a-4fa3-845f-bfc1646767f5)


Contact Us Page Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/58805d6f-c1b5-4f7f-831d-46c66016249e)

Sign In Page Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/80799f1f-9ba6-4d98-8666-c461d13c9aeb)

Sign Out Page Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a3f47033-a7dd-4d1b-b8ae-db6138f25c62)

Basket Contents Page Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/67fc43ae-46ec-42e2-ab2d-5620690fe5e9)

Newsletter Sign Up Page Desktop 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/2c53cb50-da31-49fe-9733-1a97f1bae89a)

### Mobile 

Home Page Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7e87b133-1204-4818-acc2-d4a667287dd9)

All Courses Page 1 Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/24f349ba-78e8-4a1c-8a2a-2e9826cdc7bc)

All Courses Page 2 Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d9e500a5-ff43-475c-bdcb-d8306c167ca2)

All Courses Page 3 Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f3d32cf7-a52f-403b-b06e-ede577fad19b)

Contact Us Page Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/81fb3491-419b-4e9c-9eaf-156fdd9a57ec)


Course Administration Page Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/38352ced-c19e-45e5-ad28-f7d2324db526)

My Dashboard Page Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/35fb14b8-d191-444d-b8b2-62e71b9a1247)

Sign Out Page Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/05e27e63-f61a-42d3-b3a0-5e233d3d8e0c)

Basket Contents Page Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3f67cad8-19a4-402a-af29-1bb196b1b9af)

Newsletter Sign Up Page Mobile 

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/aaf229e5-ab9e-47ab-b013-546904f69c04)



4. Features Testing

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Home Page  |          |          |          |
|1. Nav Item Logo | The logo is situated at the top left of each page and when the user clicks on it the logo will always bring the user back to the home page  | Pass  |          |
|2. Nav Item All Courses  | The all course link is situated at the top of each page in the nav bar and when the user clicks on this link it will bring the user to the all courses page.  | Pass |          |
|3. Nav Item Contact Us  | The contact us link is situate at the top of each page in the nav bar and when the user clicks on this link it will bring the user to the contact us page| Pass |          |
|4. Nav Item Dashboard  | This link is situated in the nav bar at the top of each page when the user clicks on this link it expands to give the user the option to login or register if they are not a registered user and to logout view my dashboard in case teh use is a registered logged in user.  In the case of an admin account it will also show course administration link    | Pass  |    |
|5. Nav Item Basket | This link is situated at the top of the page in the nav bar and when clicked will bring the user to the basket page. if the user has an item in the basket it will show the value undeer the basket link in the nav bar otherwise it will display 0.00 if there are no items in the basket   | Pass  |          |
|6. Nav Item Sign Up   | This link is located in the nav bar and when clicked will bring the user to the newsletter sign up page.   | Pass   |          |
|7. Nav item search  | This is located at the top of each page in the nav bar and will allow the user to search for courses. As mentioned already all of these items in the nav bar are a constant at the top of each page.  | Pass   |          |
|8. Banner  | The banner is a reminder to the user that if an order is placed about €200 they will receive a 10% discount as an added bonus.     | Pass   |          |
|9. Learn More Button    | When the user clicks on the learn more button this will bring them to the all courses page    | Pass   |          |
|10. Footer Social Media Link - Facebook   | When the user clicks on the fontawesome icon for facebook in the footer they will be brought to the comapanys facebook page.      | Pass   |          |
|11. Footer Social Media Link - Twitter   | When the user clicks on the fontawesome icon for Twitter in the footer they will be brought to the Twitter login page.      | Pass   |          |
|12. Footer Social Media Link - Instagram   | When the user clicks on the fontawesome icon for Instagram in the footer they will be brought to the Instagram login page.      | Pass   |          |
|13. Footer Social Media Link - Youtube   | When the user clicks on the fontawesome icon for Youtube in the footer they will be brought to the Youtube login page.      | Pass   |          |
|14. Footer KAC Safety Privacy Policy    | When the user clicks on the privacy policy it will open the policy in pdf format      | Pass   |          |
|15. Footer KAC Safety Contact Details    | The footer contains the contacts details of the company and again all these footer items are a constant on all pages    | Pass   - Home Page ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b797ed08-3556-43c9-b435-7fd3ee1b264a)|          |

| Goals | Acceptance | Pass | Fail |
|:----------|:----------|:----------|:----------|
| All Courses Page  |          |          |          |
|1 Contains the Nav items and footer details as described above   | All links are functional  | Pass |          |
|2. Group By search facility | The user can search for courses by health or safety in the group section  |Pass  |          |
|3. Location search facility | The user can search by location weather a course is delivered online or in the classroom.  | Pass  |          |
|4. Button - Reset To All Courses | Once the user completes a search they can reset the page to all courses | Pass  |          |
|5. Course Cards | Each course card contains information about each course and each card contains a link to course details that brings the user to the detailed courses page when clicked.  | Pass  |          |
|6. Pagination Button Next & Previous | The pagination buttons will allow the user to go the the next page of courses should they exist when clicked and the previous button will allow the user to revert to the previous page of courses when clicked.   | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f1681528-dbf0-4480-99a3-ea9476930c31)|          | 

| Goals | Acceptance | Pass | Fail |
|:----------|:----------|:----------|:----------|
| Detailed Courses Page  |          |          |          |
|1. Contains the Nav items and footer details as described above  | All links are functional  | Pass  |          | 
|2. Increment (+ sign) and decrement (- sign) | The increment button allows the user to increase the quantity of courses in the basket and the decrement button will decreate the number of courses in the basket  | Pass|          | 
|3. Keep Shopping Button  | When the user clicks on the Keep Shopping Button it will bring the user back to the all courses page where they can continue to shop the courses.  | Pass  |          | 
|4. Add Item To Basket  | When the user clicks on this button it will add the item to the basket and a toast will display to confirm item has been added to basked and they can click on procced to payment   | Pass  |          |
|5. Edit Button | When this button is clicked it will bring the user to to the edit courses page   | Pass  |          |
|5. Delete Button | When this button is clicked it will delete the course   | Pass  |          |
|5. Home Button | This will bring the user to the home page once it is clicked   | Pass   ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8be4d150-fe5d-4c44-a627-733c3808f157)|          |

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Basket Contents Page |          |          |          |
|1. Contains the Nav items and footer details as described above | All links are functional|Pass   |          | 
|2. Increment and Decrement buttons | Under the quantity column the user can click on an increment button to increase the quanity in the bag and will only go as far as 99 and the decrement button will decrease the quantity in the bag and will not pass byond the number 1 |Pass   |          | 
|3. Update and Remove buttons | The update link when clicked will update the number of courses in the basket if a change has been applied to the quanity and the remove link will remove the course from the basket. |Pass   |          | 
|4. Total Section | The totals section informs the user how much is due and the discount is clearly shown if the purchase goes above €200. |Pass   |          | 
|5. Continue Browsing Button | This button when clicked will bring the user back to the all courses page to continue browsing. |Pass   |          |
|6. Make A Purchase Button | This button when clicked when bring the user to the secure purchase page to complete the purchase. |Pass   ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/711fa031-ae87-4efc-87f8-8aeee6bdc9fb)|          |  

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|Secure Purchase Page  |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Contact Form| If the user is not registered they will have to fill out the contact form in full but if the user is registered they just need to enter their name and card details.  | Pass  |          | 
|3. Incorrect Payment Details | Should the user input incorrect payment details it will not allow the purcahse to be completed and a message will be displayed to the user under the card payment input box.    | Pass  |          | 
|3. Save Details | When the user enters their details on the form it will give the user the opportunity to save the details to their account should they be any changes in contact details.    | Pass  |          |
|4. Payment Summary | The payment summary displays to the user the picutre, name, quantity, subtotal, order total, discount if applicable and grand total for each order.    | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/59cc4e31-4a53-45b0-b3c6-dc023d81ca0a)|          |  

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Thanks You For Your Purchase Page |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Confirmation of Purchase | The thank you for your purchase page confirm that the purchase has been sucessfully processed and that an order number has been generated for the order.  The user is also given a summary of the costings for the purchase.    | Pass ! |          | 
|3. Return to all courses button | When this button is clicked is will bring the user back tot he all courses page   | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d1b3526e-82a1-4ba6-8c10-13f49b44595a)|          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Contact The KAC Safety Team Page |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Contact Form | This page contains the contact form in which the user enters their details should they wish to make contact with the company.  The form will not be submitted unless fullname, company, telephone, email and course title is filled out.   | Pass  |          | 
|3. Submit Button | When the user clicks on the submit button it will submit the details and bring the user to the contact success page.    | Pass |          | 
|4. Sign Up Error Messages  | If the user fails to input the correct information it notifys the user    | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/25ec1d12-f4f9-44e3-bbfb-5852487c4977)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Contact Succuss|  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Contact Success | The contact success page displays confirmation back to the user that their message has been recieved and a memeber of the team will reach out within 24 hours.  | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/fd445eeb-703f-43d5-ac81-c8228fd37edd) |          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|Sign Up  |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2 Sign Up Form  | The sign up form will request the user to enter their email address, username and password in order to sign up. If the password is too short a notification will be displayed back to the user.  | Pass |          | 
|3 Sign Up | When the user clicks on this button the user details will be submitted  | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c22993d6-5d2a-4019-b921-387ff54a6fe7)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|Login   |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2 Sign In Form  | The sign in form will request the user to enter their email address or username, and password in order to Login. .  | Pass |          | 
|3 Home Button | The home button will bring the user back to the home page when clicked  | Pass | |
|4 Sign In Button | This will sign the user into their account when the button is clicked.  | Pass | |
|5 Forgot Password | This will allow the user to set a new password .  | Pass | |
|6 Sign Up | This will allow the user to sign up for a new account  | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/77981fbd-a964-4685-bef8-01dccdc16028)| |

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Add Course Page  |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Add Course Form  | Here the adminstrator will enter the title, location, details, group by, fee, date of course and image url.  If the user does not have an image the place holder image will be assigned to the course. The course will not be submitted unless the Title and details of the course are filled out.   | Pass |          | 
|3. Cancel Button  | Should the administrator not want to add the course they can click on the cancel button and this will cancel the form.   | Pass  |          | 
|4. Add Course Button  | When the user clicks on the add course button this will submit the form and a message will be displayed back to the user to say course has been added and will return the user to the detailed course page.  | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/787fa92d-20f2-4de6-9ae1-e7954689111a)|          | 



| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| My Dashboard Page  |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Dashboard Form  | The dashboard form is where the user can enter their details and save same | Pass          | 
|3. Update Information  | When the user has updated their details they will click on the update information button and this will update the details that are stored for that user.   | Pass |          | 
|4. Purchase Record  | This section displays a list of previous purchases that the user has made and they can click into each purchase and view in detail.  | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1dd0aed2-2be0-487e-9cbb-1201aba54587)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Sign Out Page |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Message and Sign out button   | The sign out page displays a message to the user asking them if they are sure they want to sign out.  The user can then click on the sign out button which will sign them out of their account. | Pass -	![image](https://github.com/NBJIN/kacsafetya/assets/106515976/19d5ba71-484d-42a4-87a3-361036c1499c) |          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Basket Contents Page|  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2.Message and Continue Browing Button  | The basket contents page displays a message to the user to say their bag is empty and if they wish they can click on the continue browsing button which will bring them back to the all courses page. | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3eb15d38-0a2b-4d63-b881-0b77535f33de)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|Newsletter Sign Up  |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Newletter Signup  Form   | In order for the user to sign up for the companys newsletter they must fill out fullname, company and email.  The form will not submit unless fullname and company are filled out.  | Pass |          | 
|3. Submit Button  | When the user clicks on the submit button it will submit their details and  the user will be carried to the newsletter signup success page  | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0dfd5d95-ed0d-411c-aa02-ad8fccad1bd1) |          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|Newsletter Sign Up Success |  |   |          | 
|1.Contains the Nav items and footer details as described above | All links are functinal | Pass |          | 
|2. Sign up success message and home button  | The Newsletter sign up success page displays a message back to the user to say they have successfully signed up and the home button when clicked will bring the user back to the home page.  |  Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4eb858b0-68ba-4f35-8ba4-7efd303f0dc2) |          | 

<br>