[Link Back to Main Readme Document](README.md)

## NUMBER TO BE INSERTED. Testing
#

## Table of Contents
1. Testing User Stories

2. Code Validation

3. Accessibility

4. Manual and Tools Testing


### 1. Testing User Stories 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| |          |          |          |
|1. Admin User - Set Up Project Workspace  | Installed Django and supporting Libraries, created a new blank Django project and app, set the project to use cloudinary and PostgreSQL and deploy new empty project to Heroku | Pass |          |
|2. Admin User - Complete final project deployment.  | Ensure that final commits are completed, debug changed to false and settings removed under config variables in Heroku. | Pass |          |
|3. Admin User - Be able to set up an account | Create a sign up page where i can enter my username, email and password in order to register and gain access to the blog.   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/3cbf6afb-0941-43eb-be15-47fda8f33b82) |          |
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
|7 As a site user login and see my details.  | Once the user clicks on the dashboard on the nav menu and naviagtes to signin they will enter their details and will then be able to access my dashboard on the menu bar and here they will be able to see their own details.      | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/eff7e7a3-ae52-4538-9625-60935a58c98b)|          |
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
| 14 As a user be able to add a course to the basket. | The user can add an item to the basket in the detailed courses page.  They will then see the amount undere basket on the navbar and a success message will display to say an item has been added to the basket. Here they will also see the total cost of the items they are purchasing. | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/989cc3db-1964-42e0-8774-a181bbb55b98)
if there is no items in the basket they will be able to see this when they see the basket in the nav bar as the amount will read €0.00.  If the user clicks on the Basket they will be brought to the following page.  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/92bcc968-7298-4ae4-a3d2-6a5759f7ad88)|          |
| 15 As a user i want to be able to see courses in the basket.   | When the user clicks on proceed to payment on the success toast they will be brought to the basket contents page.  Here they will be able to see each course they have added to the basket the amount and the discount applied if any to the basket total.  | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/079b6471-4dd8-4b99-b5fc-b53e0ecd411c) |          |
| 16 As a user i want to be able to change the quantity of courses i have in the basket.   | On the basket contents page under the quanity heading there is an option to increase or decrease the quanity of the course by clicking on the minus and plus signs.  Once the sign is clicked on the user can then click on the update button and this will update the total in the basket.  If they decide they no longer want to go ahead with the course they can remove the course from the basket by clicking on the remove button.   | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/01c7bdf5-24e9-4c62-9dc1-f868ed3346e6) |          |
| 17 As a user i want to be able to enter payment details in order to make a purchase.  | When the user is on the Basket Contents page they can click on make a purchase which will bring the user to the Secure Purchase Page.  If the user is not a registered user they will have to enter all their details along with payment details in order to make a successfull purchase.  They will also be given the option to reigister for an account or even login if its a registered user. If the user is a registered user their details will be prefilled and they will just have to enter the name and card details. This page also shows a summary of the order so the user can see exactly what they have purchased and confirmation of the cost.      | Pass Proceed to payment ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7d6666c0-a854-4875-bb04-2dea1ba7d5ef) Secure Purchase Page ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/888f869d-2842-4a84-97ba-13c32da7770d)|          |
| 18 As a user i want to be able to see confirmation of my order when payment is complete.  | When the user is on the Secure Purchase Page and places an order the loading spinner will then display to show that payment is being processed.  Once the transaction is successfull the thank you for your purchase page will then display which is confirmatiion of the order and payment to the user.       | Pass Loading Spinner ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/12cb4196-5105-4436-aa2d-52aa89f7f678) Thank You For Your Purchase Page ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6b619a11-f61c-4d81-803a-5f0a6b02d32d)|          |
| 19 As a user I want to be able to see my order history once logged in.  | Once a user is registered and logged in they will be able to navigate to the dashboard and then my dashboard on the nav bar.  Here on my dashboard they will be able to see a history of purchases.        | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/66cee049-990d-437b-b51c-5b8fcd06e467)|          |
| 20 As a user I want to be able to make a purchase without having to register.  | When an unregisterd user accesses the all courses page they can choose a course to go to the detailed view and once on this page they can add the cousre to the basket and proceed to purchase and then purchase success page.  On the screenshot following one can see that the user is not logged in when making the purchase        | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/50d3978b-9f1b-4732-ab7a-34913cd8f64a)|          |
| 21 As a user I want to be able to sign up to a company newsletter.  | On the navbar at the top of each page there is a link called sign up.  When the user clicks on this link they will navigate to the newsletter signup page where they will enter their details. Once they have they details entered and submit same they will recived confirmation of signup.  | Pass !![image](https://github.com/NBJIN/kacsafetya/assets/106515976/433fa2c2-9e4b-4aa8-be10-2c1f9fb09939)   ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f04eab86-9b4d-43f9-81ca-7eac304766fe)|          |
| 22 As a user I want to be able to submit a contact form.  | In the top nav bar there is a link to Contact Us once the user clicks on this link they will be brought to the Contact KACSafety Page where the user can enter their details and their query.  Once these details are submitted the user will recieve confirmation to say that their message has been received.    | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c0f04159-5ff9-427b-9412-d330165ae6df)    ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a8ccb9ed-e6df-4256-a2fe-8e2936cfc371)|          |
| 23 As a user I want to be able to access the companys social media page.  | If the user navigates to the footer on any page and click on the facebook link they will be brought to the companys social media pages.   | Pass ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c4843732-b3d4-4cc7-8a15-06a4002b69c2)  Youtube ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bde0e16c-6755-4f92-ba95-09b39557d337) Facebook ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/cbc0a2ae-bb80-4827-a838-f961913041c0) Twitter ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/99377b81-ac63-4c8f-a097-8ca61fffae4f) Instagram![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6c3ffbe3-fe61-4310-8afb-750e51d3d11c)    |          |
| 24 As a user I want to be able to see confirmation of actions completed.  | When a user completes an action on the website confirmation of same is displayed back to the user. Attached are some examples  | Pass Successful Signin ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6a87f1bc-3e02-4e03-a699-a6c79a189ed2) Add Couse ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/fc3277d3-81a5-4e26-8767-837cb714f51e) Successful Payment ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6041196d-6045-452b-9275-7565150fc7db) Contact Success ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b26adccd-fda0-4115-acc8-67650f81359f)  newsletter signup ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/34437f01-2d3c-408a-88d3-0941afe036d5)   |          |
| 25 As an administrator I want to be able to add a course.  | When an administrator logs in they will be able to add courses through the nav link dashboard / course administration. When the couse is added the administrator will naviage to the detailed courses page for that course.  | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1e593bd2-c72b-479b-8db0-5308b7b2d746) ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d1c5cd75-493c-47b3-bfd2-e1374dfe960d) |          |
| 26 As an administrator I want to be able to edit a course.  | An administrator will be able to edit a course when they click on edit on the detailed course page. Once edit is clicked they will be brought to the edit course page. Here they will fill in the details and have the choice of editing or cancelling the changes they have completed.  | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/2ab297f0-828f-4707-86d2-89be18437b43) |          |
| 27 As an administrator I want to be able to delete a course.  | An administrator can naviage to the detailed course page there they will see a button to delete a course.  Once they click on the button the course will be deleted and they will navigate back to the all courses page and a message will display to say the course have been deleted.   | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/568a5bc8-85ac-4f96-813a-9d1640f737bb) ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b8f6761c-14b2-497e-9404-60e16537866b)|          |
| 28 As an administrator I want to be able to update the general content on all page.  | The admin user will have full access to the admin panel and also will be able to manage courses from the front end and will be able to update and add content here and through the admin panel.    | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/98f298de-04b5-4475-b921-7a045474c62a) ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0beb5494-f7e2-4297-affb-1471cfd6d630)|          |
| 29 As an administrator I want to be able to manage all incomming orders.  | The admin user will have full access to the admin panel where they can manage orders.      | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/06b2fd64-9325-49e4-85ad-e17cf89e2e29)|          |
| 30 As an administrator I want to be able to manage all incomming contact queries.  | The admin user will have full access to the admin panel where they can manage orders.      | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/06b2fd64-9325-49e4-85ad-e17cf89e2e29)|          |
| 31 As an developer I want to be able to test all parts of the django website.  | Testing of user stories, features, code validation, lighthouse reports have all being carried out and detailed report is contained in this readme file.     | Pass  |          |
| 32 As an developer I want to be able to deploy successfully.  | This project has been deployed to Heroku.     | Pass  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9b499754-f851-4d26-8327-eb39fdff409e)|          |
| 34 As an developer I want to be able to ensure that the site is responsive.   | The project is responsive on mobile and desktop (desktop, labptop, i pad air, samsung galaxy and iphone 6/7/8).     | Pass  |          |
<br>



2. Code Validation - In carrying out code validation the following was utilised. 
 - HTML code tested using W3C Markup Validation Service - https://validator.w3.org/
 - CSS code was tested using CSS Validation Service - https://jigsaw.w3.org/css-validator/
 - Javascript was tested using JS hint - https://jshint.com/
 - python was tested with Code Institute python pep8 - https://pep8ci.herokuapp.com/#

 ## Starting with HTML below is a screenshot of each page which has been passed through W3C Validator.  
 - 1 Landing Page - No Errors or Warnings
 ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/40452372-6a51-4a29-a95b-0aea73e5b23c)
 - 2 all_courses page 1 - No Errors or Warnings
 ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7966de88-a3e1-4942-b4b4-2bd0a5b5fe05)
 - 3 all_courses page 2 - No Errors or Warnings 
  ![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0bd702ab-10db-42e2-9876-8e0241a94e34)
- 4 all_courses page 3 - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9b0f429a-4bbe-4576-8bfc-617a64aa41b2)
- 5 all_courses page 4 - No Errors or Warnings 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/cecb2497-0dbf-4d8a-b9c7-c8d24eac6114)
- 6 coourses/courses/detail (detailed courses page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9f191817-de1f-4697-af50-57b78b6eda45)
- 7 courses/courses/detail/16 (Add course to basket) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/cb3d543a-151e-43a0-8b6f-609265d77f28)
- 8 basket page - No Errors or warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e9800504-92b1-482a-8b50-64060889d9cd)
- 9 Purchase Page (Secure Purchase Page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/2e20a9ac-81b1-45b8-99cd-6b7d306414e7)
-10 purchase/purchase/purchase_success/ (Thank Your For Your Purchase page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/aeb31c79-6230-4165-8eca-5bf938b400ed)
- 11 contact page - (Contact The KAC Safety Team Page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/feb3dc59-e7c6-4343-a00e-3ce04d02864e)
- 12 contact/contact_approved (Contact Success Page ) - No Errors or Warnings

![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bca1511a-0b1c-4336-a880-168359b95949)

- 13 courses/add (Course Administration Page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4ad8a816-35f0-49c2-b237-133343e7ab65)

- 14 dashboard (My Dashboard Page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7571f7c7-f21f-4bd3-8cee-a040cc4aef6e)

- 15 accounts/logout/ (Sign Out Page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/123b835a-d62e-4264-b48c-f09f576d0c12)

- 16 basket/ (Basket Contents Page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d5989a7d-00e8-426c-a55b-575e728d929b)

- 17 mailchimpnews/subscribe (Newsletter Signup Page) - No Errors or Warnings 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8db08f2e-abf8-477c-b53a-ae209e344a9d)

- 18 mailchimpnews/subscribe/success (Newsletter Signup )
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/5a2049e8-e66f-47ef-91e6-37346cd04c44)

- 19 accounts/signup/ (Sign UP Page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/846dcaba-c7c1-4ed9-a689-01ecf0c25085)

- 20 accounts/login/ (Sign In Page) - No Errors or Warnings
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/5be30326-ccdd-4434-bf32-4c9af486a13b)

## CSS was validated through the W3
- 1 dashboard.css - No Errors Found
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c77e1a14-bd24-4469-9884-9db52a890b32)
- 2 purchase.css - No Errors Found
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1cb74281-4574-41e7-b7b9-fc94470514ca)
- 3 base.css - No Errors Found
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/be8bcaf2-b429-4652-923b-29a765c58e15)

## Python was validated with the Code Institute Python Linter
1 bag_tools.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/db612725-d77b-4cda-8f99-2bc2c19bfcb9)
2 basket / admin.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/24e73b7e-5016-4a68-8957-15047a64ca67)
3 basket / apps.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c61fe361-20ad-4bfe-a7d2-11e1a35c4322)
4 basket / contexts.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/476d3715-6edd-42a8-b398-0e0cb3c48a13)
5 basket / models.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7941369d-628a-49d1-9d42-b52932f78b0d)
6 basket / urls.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a5c575e1-70e8-4d23-a3e3-e699dffe0366)
7 basket / views.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d715c814-58ee-45ef-b997-ca5139d72c98)
8 contact / admin.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/bb2dc953-31c5-410a-a942-09fd6411ddce)
9 contact / apps.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ad748eea-949d-4efd-bf6b-88ada0f629bf)
10 contact / forms.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/21759d4b-de81-4d80-8208-a78296f7d698)
11 contact / models.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/5e470e79-bbab-4807-b8a8-9880e60e87d6)
12 contact / urls.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7b23f57d-76c8-4d54-950b-4c84988dbcbd)
13 contact / views.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f0c52e00-26ff-4ad8-a441-a26f52b8545d)
14 courses / admin.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/88eb38f7-8483-45ba-a572-719b8799f986)
15 courses / apps.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c7849309-f201-4a40-bbb4-3765dfc5c8df)
16 courses / forms.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e764ecab-464a-4814-8261-2fa436a94a91)
17 courses / models.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7d0dc948-0206-4eff-ba56-60cca904b9c4)
18 courses / urls.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3f5f58db-1f24-4968-88c6-76bfa854a64d)
19 courses / views.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/30e0ce52-a04d-41f6-8fd7-5832379aeebd)
20 courses / widgets.py
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/b2846664-83fb-43f0-9653-fff2b67107af)
21 Dashboard / apps.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0b8509ed-289a-4181-a789-05df0284b30d)
22 Dashboard / forms.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/8be758fe-9568-4771-b678-a91d8ab30645)
23 dashboard / models.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/56c8fe3d-07e5-416c-9853-ee10ddb168e5)
24 dashboard / urls.py
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9ce0638d-c79b-4977-8253-791846aeea11)
25 dashboard / views.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c271e9ab-a02c-498e-991c-2d6576b5fd93)
26 Kacsafety urls 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/a175222f-7e99-4ec8-af04-5f7bb9be4d12)
27 Kacsafety views.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/51c187ed-1aa5-4195-a997-b7850d065244)
28 kac_safety wsgi.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/97b9b0d1-25a0-4fb4-9eec-50cf3cadba7a)
29 landing apps.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/f44796ad-16ff-4b2c-b8fb-043b1fbef6f4)
30 landing urls.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/441036c4-68a5-4d5a-81d1-22490b5b1af1)
31 landing views.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e1841580-9b7e-4beb-8c99-4cac600a704d)
32 mailchimpnews admin.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/00b784de-bf26-458d-8c5e-7d7cd7c2c571)
33 mailchimpnews apps.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/ec75e645-8511-4b99-af6d-77630606f756)
34 mailchimpnews forms.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/4713c6c6-1949-4181-84f3-1b11948c43c8)
35 mailchimpnews models.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/9e7ec3c8-cd5d-418b-bb49-dc52c1e6c4b4)
36 mailchimpnews urls.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/0f6d836d-8004-4b9d-938c-0612049c167e)
37 mailchimpnews views.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d591ae4b-101e-4642-aba8-59813c7dbed6)
38 purchase init.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3cfc2a14-7a5c-4fe8-a401-f1fa8bf1015e)
39 purchase admin.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/6c53acb9-31b7-4729-997d-bc8a13e82fe7)
40 purchase apps.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/3928f2b6-33b5-40b2-8eda-012ad2881161)
41 purchase / forms.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/2e4c43ce-eea5-4888-b231-184fed2d6d1f)
42 purchase / models .py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/7fda020e-abc9-4ce3-bd49-8b538a4712dd)
43 purchase / signals.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/c2a3864e-843f-458d-9087-67bd1f28439b)
44 purchase / urls.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/d97e3a0c-46ae-4ab4-8837-c2d571e96805)
45 purchase / views.py 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/aa005b6f-0776-4d8b-a439-213ad0bbf411)
46 purchase / wh handler 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/1a912e84-e1f9-4cbe-9a27-1399f33f1c72)
47 purchase / webhooks.py
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/15cce422-5820-4540-9e19-47496abebd76)
48 custom storages 
![image](https://github.com/NBJIN/kacsafetya/assets/106515976/e62c2949-24bb-454b-b3d1-55dc6e179bfb)





3. Accessibility
A lighthouse test report was carried out and the results are as follows 

![image](https://github.com/NBJIN/constructionblog/assets/106515976/aa9401b1-2cf0-4077-93ea-bb8c94a74ddf)



4. Features Testing

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Home Page - Signed In User |          |          |          |
|1. Logo | When the user clicks on the logo on top of each page it will always bring the user back to the home page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/5b3425d9-0328-47c3-b965-1658607db66a) |          |
|2. Welcome Message | When the user logs in it will display the welcome message with their username letting the user know that they are logged in. | Pass |          |
|3. Navigational Link - Home | This is displayed at the top of every page when the user is logged in so when the user clicks on the home link it will bring them back to the home page | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/cc78a6b3-2827-4c45-86f5-8a2f2b45a226)|          |
|4. Navigational Link - Logout  | This is displayed at the top of every page when the user is logged in so they can logout at any time.    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/cc78a6b3-2827-4c45-86f5-8a2f2b45a226)|    |
|5. Navigational Link - Create Post | This is displayed at the top of every page when the user is logged in so that the user can create a post at any stage while visiting the site  | PassPass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/cc78a6b3-2827-4c45-86f5-8a2f2b45a226)  |          |
|6. Header - List of Blogs Post  | This header advises the user that they are visiting the list of blog post page.  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/e627afd6-ccb9-43f1-af2d-dc57e85e36ab)  |          |
|7. Read More Link On Card   | When the read more link is clicked it brings the user to the detailed post page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/94f4e2b4-fa7f-4cf1-925e-fe752d9fe0ef)  |          |
|8. Fontawesome Thumbs Up and Like Counter On Card  | When the thumbs up or the number of likes is clicked it will bring the user to the postdetail page where they can click the like button at the bottom of the page to like the post.  The number of likes on the lists of blog posts page provides the total number of likes for that post and clicking on the thumbs up as mentioned will bring the user to the postdetail where they will read the post in full and then if they wish to like the post they can click the button at the bottom of the postdetail page which automattically updates the counter on the list of blog posts page.    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/94f4e2b4-fa7f-4cf1-925e-fe752d9fe0ef)  |          |
|9. Pagination Next Button   | When the user clicks on the next button under the cards on the list of posts page it will bring them to the next page which has additional posts.     | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/94f4e2b4-fa7f-4cf1-925e-fe752d9fe0ef)  |          |
|10. Footer Social Media Link - Facebook   | When the user clicks on the fontawesome icon for facebook in the footer they will be brought to the facebook login page.      | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/eaa80b05-a88b-4f08-9ea4-892273e4ac18)  |          |
|11. Footer Social Media Link - Twitter   | When the user clicks on the fontawesome icon for Twitter in the footer they will be brought to the Twitter login page.      | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/eaa80b05-a88b-4f08-9ea4-892273e4ac18)  |          |
|12. Footer Social Media Link - Instagram   | When the user clicks on the fontawesome icon for Instagram in the footer they will be brought to the Instagram login page.      | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/eaa80b05-a88b-4f08-9ea4-892273e4ac18)  |          |

| Goals | Acceptance | Pass | Fail |
|:----------|:----------|:----------|:----------|
| Detailed Post Page Signed In User  |          |          |          |
|1 Detailed Post Page  | Contains all the header and footer items above for a logged in user and all features are working.  | Pass |          |
|2. Detailed Post Header | The header advises the user what page they are currently visiting.  |Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/f12e2f42-1da3-4d03-aa43-27da09d922ff) |          |
|3. Card Update Post | When the user clicks on the update post link at the bottom of the card it will bring the user to the update post page | Pass - Screen shot below |          |
|4. Card Delete Post | When the delete post link is clicked it will bring the user to the delete post page. | Pass - Screen shot below |          |
|5. Card Create Post | When the user clicks on create post it will navigate to the create post page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/d835e1ff-d553-4899-af99-b279a1f7673a) |          |
|6. Confirmation of Comments | If there is no comments it will advise the user of same and ask if they would like to add a comment  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/cbc87569-bc4d-48ff-a1d0-a6ee671261a0) |          | 
|7. Add comment button | If the user clicks on the add comment button they will be brought to the add comment page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/378beb04-0ba6-4525-bdbd-a27f4a75e294) |          | 
|8. Delete comment button | A button had been added for Delete Comment but at present it is not functioning  | Fail ![image](https://github.com/NBJIN/constructionblog/assets/106515976/9e672d9c-d429-40d5-a00b-a94a82c2d360) |          | 
|9. Like button | The like button when clicked will increase the counter which inturn increments the no of likes on the list of posts page.  If the user likes the post by mistake they can press the button again and it will remove the like. | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/ec438296-b63b-4978-bf31-54a2b9a09e58) |          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Add Comment Page - Signed In User |          |          |          |
|1. Form and Submit Button | On the form the user will fill in the details of their comment on the form and when the submit button is clicked it will bring the user back to the postdetail page where they can see the comment displayed. | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/529f9253-bc4f-4e23-8514-e6be94f34e9a)

![image](https://github.com/NBJIN/constructionblog/assets/106515976/17b0b75d-b38c-4370-bdca-090e7d80b6f7)  |          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|1. Sign Out Page |  |   |          | 
|1. Sign Out Heading | Heading to advise the user what page they are currently visiting | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/ca3a7a4c-61fb-4544-bba4-050715a75f89) |          | 
|2. Sign Out Button | When the user clicks on the signout button it will bring them to the home page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/bef13f93-cd22-42e8-829a-9a748b689323) |          | 
|3. Sign Out Message | When the user is brought to the home page once they have clicked on the sign out button a message displays at the top of the homepage letting the user know they have successfully logged out.   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/052fc651-1f0f-48ea-9d26-2b78ca87abb1) |          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Sign In Page |  |   |          | 
|1. Sign In Heading | Heading to advise the user what page they are currently visiting | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/019174f7-13a7-4dad-9e03-4b1edcd6cf93) |          | 
|2. Sign Up Link | If the user does not have an account they can choose the sign up link which will bring them to the sign up page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/6a9728ff-75c1-42e0-9331-b60c93089d7f) |          | 
|3. Sign In Form  | The form allows the user to enter their username and password    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/f241a70f-8cf9-4f58-a938-c2d740b8a598) |          | 
|4. Sign In Error Message  | If the user inputs incorrect information it notifys the user    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/3193e4ed-28f4-45d6-ad73-7a0e7462fefb) |          | 
|5. Sign In Button  | The sign in button when clicked will bring the user to the home page    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/8394ba66-637f-4420-bdd5-ea7bb66a5b61) |          | 
|5. Sign In Success Message | When the user signs in successfully a message will be displayed to the user in the home page under the logo of successfull sign in    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/04c7d453-d611-4204-99bd-f388f25f08cf) |          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Sign Up Page |  |   |          | 
|1. Sign Up Heading | Heading to advise the user what page they are currently visiting | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/3ba07683-c364-4e5e-aee3-9e4cfa4efea1) |          | 
|2. Sign In Link | If the user already has an account they can choose the sign in link which will bring them to the sign in page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/626c1cff-c03d-4f46-8280-7f5eb4e87d62) |          | 
|3. Sign Up Form  | The form allows the user to enter their username, email and password in order to register as a user.     |![image](https://github.com/NBJIN/constructionblog/assets/106515976/90fb2793-3f22-4a78-8ef8-a344767fae4a)|          | 
|4. Sign Up Error Messages  | If the user fails to input the correct information it notifys the user    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/5f4f59c2-bee3-414d-bfc8-4975460f5acf) ![image](https://github.com/NBJIN/constructionblog/assets/106515976/8cb361de-9d12-45b1-bd50-e64e7ad890b2)|          | 
|5. Sign Up Button  | The sign up button when clicked will bring the user to the home page    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/565112f6-ed50-48d0-b18b-7134f766399a) |          | 
|5. Sign Up Success Message | When the user signs up successfully a message will be displayed to the user in the home page under the logo of successfull sign up   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/e15291e6-f708-401a-8151-dfd34b107100)|          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Home Page Not Logged In  |  |   |          | 
|1. Navigational Link Sign In | In the nav menu of home page where a user is not logged in they can chooose the sign in link which will bring them to the sign in page  | Pass - Screen Shot Below  |          | 
|2. Navigational Link Sign Up | When the user is not logged in and clicks on the sign up link on the nav bar it will bring them to the sign up page  | Pass - Screen Shot below |          | 
|3. Navigational Link Home  | When the user is not logged in and clicks on the home link it will bring them back to the home page    | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/af3afe93-cc26-4d80-9c87-1c009f8e95f3)|          | 
|4. Card Message To Sign Up  | When the user is not signed in a message displays on the card to advise the user to sign in to like or comment on a post    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/065aac9c-dcfe-40df-b8ad-b82953502e36)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
|Detailed Post Page Not Logged In  |  |   |          | 
|1. Detailed Post Message To User Re Comment and Likes  | When the user is not logged in a message is displayed to the user to advise them to log in if they want to like or comment on a post.    | Pass - ![image](https://github.com/NBJIN/constructionblog/assets/106515976/fefafff0-83f6-4d02-8e81-8fe15fc764e5)  |          | 



| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Detailed Post Page Logged In User |  |   |          | 
|1. Detailed Post Header  | The Header advised the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Link To Update Post  | When the user clicks on the update post link they will be brought to the update post page  | Pass - Screen Shot below |          | 
|3. Link To Delete Post  | When the user clicks on the Delete Post they will be brought to the Delete Post Page    | Pass - Screen Shot Below |          | 
|4. Link to Create A Post   | When the user clicks on create post they will be brought to the create post page    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/0d2fb4ea-b409-4ad7-bdd0-44fb65466c2a)|          | 



| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Update Post Page Logged In User |  |   |          | 
|1. Update Post Header  | The Header advises the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Update Post Form   | The form allows the user to enter details to update the post  | Pass - Screen Shot below |          | 
|3. Submit Button  | When the user clicks on the submit button on the update post page they will be brought back to the list of post page   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/5579625a-8cc5-4c32-91c9-a68087e7cd85) |          | 
|4. Error Message displayed back to user   | If the user submits the form without a date an error will display to the user   | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/df9d0ef0-6e32-4204-b420-ce6e93f0192e)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Delete Post Page Logged In User |  |   |          | 
|1. Delete Post Header  | The Header advises the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Submit Button   | When the user clicks on the submit button the post will be deleted and the user will be brought back to the list of blog post page  | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/d3e07c35-2b64-4781-893e-b4eba0b6c798) |          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Create Post Page Logged In User |  |   |          | 
|1. Create Post Header  | The Header advises the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Create Post Form   | The form allows the user to enter details to create the post  | Pass - Screen Shot below |          | 
|3. Submit Button  | When the user clicks on the submit button on the update post page they will be brought back to the list of post page   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/a8135ffb-75c5-47e5-9d07-171b743268ca) |          | 
|4. Error Message displayed back to user   | If the user does not enter a date or a name the post will not submit and a message is displayed back to the user    | Pass  ![image](https://github.com/NBJIN/constructionblog/assets/106515976/9c1d694c-f3d6-4847-a798-785b4b309dc8)|          | 

| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Add Comment Page Logged In User |  |   |          | 
|1. Add Comment Header  | The Header advises the user of what page they are on  | Pass - Screen Shot Below  |          | 
|2. Create Post Form   | The form allows the user to enter details to add the comment  | Pass - Screen Shot below |          | 
|3. Submit Button  | When the user clicks on the submit button on the update post page they will be brought back to the detailed post page   | Pass ![image](https://github.com/NBJIN/constructionblog/assets/106515976/706a5bd2-861f-4ab1-8424-a961ca1c9d3d) |          | 


| Goals | Acceptance | Pass | Fail
|:----------|:----------|:----------|:----------|
| Delete Comment Page Logged In User | This page is currently not displaying  | Fail   |          | 


<br>