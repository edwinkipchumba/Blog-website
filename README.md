# Blog Website

## Author

 Kolem Edwin

## Description

This is a personal blogging website where you can create and share your opinions and other users can read and comment on them.

## Screenshot images

<img src="./app/static/ima">



## Live page
https://github.com/edwinkipchumba/Blog-website


## User stories

As a user I would like to:

1. View the blog posts recent on the site.
2. comment on blog posts.
3. email alert when a new post is made by joining subscription.
4. see random quotes on the site.
5. sign in to the blog.
6. create a blog from the application.
7. delete comments that I find insulting/degrading
8. update/delete blogs I have created
   
## Behaviuor Driven Development (BDD)

| Behaviour | Input |Output |
| :----------------| :-------------------:| :------------------|
| Blogger Authentication| On demand | Access Admin dashboard |
| Display blogs by most recent | On home page | Clickable links to open all blogs |
| Display profile | Click profile page | Redirected to a page with your profile |
| Display single blogs | On link click | Blog is displayed with with comment ready function and comments already stored |
| To add a blog | Through Admin dashboard | Redirected to the blog form collection form |
| To edit a blog | Through Admin dashboard | Redirected to the blog form collection form and editing happens |
| To delete a blog/comments | Through Admin dashboard and on display | Bad comments and posts can be deleted | 
| To subscribe | On button click | Users can subscribe on click | 

## Installation/Setup instruction

#### The application requires the following installations to operate
* python3.8
* flask
* virtualenv
* pip
 
 #### Cloning

* Open Terminal {Ctrl+Alt+T}

```
$git clone https://github.com/edwinkipchumba/Blog-website
```
```
$cd blog
```
* open based on the text editor you have.
  
* Creating virtual environment
```
$ python3.8 -m venv --without-pip virtual
```
  
```
$ source virtual/bin/activate
```
```
$ curl https://bootstrap.pypa.io/get-pip.py | python
```

* Installing Flask and other Modules:
```
(virtual)$ pip install -r requirements.txt 
```
* To run the application, in your terminal:

```
$ chmod +x start.sh
```
```
$ ./start.sh
```

## Technology used

* flask
* HTML5
* Bootsrap
* python3.8

## Known Bugs

If you find a bug, kindly feel free to comment an issue here and inlcude their corresponding results.

## Contact  Information

 Feel free to contact me incase of any issue or questions, ideas and concern towards the same.
 * Contact Number:+254728357619
 * E-Mail: edwinkolem5@gmail.com.

## License
https://github.com/edwinkipchumba/Blog-website/blob/master/LICENSE