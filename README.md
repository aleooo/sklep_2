# sklep_2



## Add your files

- [ ] [Create](https://gitlab.com/-/experiment/new_project_readme_content:05e951127536f7e298cbf31dec4e3058?https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://gitlab.com/-/experiment/new_project_readme_content:05e951127536f7e298cbf31dec4e3058?https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://gitlab.com/-/experiment/new_project_readme_content:05e951127536f7e298cbf31dec4e3058?https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/Aleooo/sklep_2.git
git branch -M main
git push -uf origin main
```

## Description
The sklep_2 project is a template modeled on Allegro. The application is adapted to mobile devices Project is created in Django.Contains:
- live-search(dynamic search made with AJAX)
- authorization system
- dynamic paging and filtering of the list of objects
- shopping cart for products based on a Django session
- create pdf to order which is send on email
- The recommendation engine on redis
- dynamic personal data form in javascript


## Visual
https://www.sklep2.waw.pl


## Installation
1. create database postgres
2. create virtual environment
3. add .env with settings:
    SECRET_KEY=
    DEBUG=True
    ADDRESS_IP=127.0.0.1
    DOMAIN=
    WWWDOMAIN=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    SOCIAL_AUTH_FACEBOOK_KEY=
    SOCIAL_AUTH_FACEBOOK_SECRET=
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=

4. install libpangocairo-1.0-0 in system
5. install package from requirements.txt

## Project status
The project is being developed

