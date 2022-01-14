
Versions Used

django = "==3.2.4"
psycopg2-binary = "==2.9.1"
python version = "3.9"
docker-compose version 3.7
django-crispy-forms = "==1.12.0"
crispy-bootstrap5 = "*"
django-autoslug = "==1.9.8"
pillow = "==8.2.0"
python-dateutil = "*"


crispy-bootstrap5
	https://github.com/django-crispy-forms/crispy-bootstrap5

https://legionscript.medium.com/


			**DONE** 
1. Configured postgresql with docker and django in docker-compose.yml and 

2. Made a Custom User model with no modification
3. Made UserAdd and UserEdit forms with in a new app **Users**
4. Made the profile model. Added it to the admin panel
5. Converted age to positiveinteger field
6. Added Pages app, for static pages  and implemented some tests
7. Added Templates
8. Added Common Login, Logout and Signup functionality 
9. Added Static asset directories and configured the settings (collectstatic -> staticfiles on production) 
10. Altered the profile model user field, removed **null=True**
11. Added the navigation bar in _base.html
12. Added AllAuth, enables username or email in login 
13. congiured AllAuth, degrading the templates/registration under templates/account
14. Email is configured to terminal  
15. all necessory models are made
16. updated timezone 
17. added media folder 


			**TODO**

1. Everything in the Profile model is created when the user model is created so every field in profile model is set to **null=True**. Rectify that in future
2. Recheck the names for profile table rows 
3. Configure bootstrap5 with crispy-template-pack
4. Add styling to the user forms 
5. Configure mail from a webserver. 
6. Add SocialAccout logins
7. Alter the emails
8. Configure django-tinymce 3.3.0
9. Alter email confirmation messages in **templates/account/email**
10. Create home.html and set login_redirect_url to home :: by callous
11. necesory models in feed app require alterations, make the offensive posts noy appear 
12. make views for feed app 
13. comfigure the django-tinymce 
14. Contact Canva.

//Front END

1. Stage.html configured for non users : stage.css :no file for js
2. Every template will inherit from base.html except stage.html


//TO -Do

1. Logo may be changed
2. Footer allignment
3. stage.html for users : user profile information on page 
