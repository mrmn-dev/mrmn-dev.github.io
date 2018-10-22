Title: Pelican Tips
Category: Postcards
Date: 2018-10-2
# Pelican and github hosted site notes

---
* **Pelican** is a static website genaration tool. **Github** is a version control web repository that allows you to host a website. See the links below to get set up. Below are just notes to myself for my wash, rinse and repeat process.  
* Place yourself in the github content directory. Start your editor.
* There are two directories within the content directory, **blog** and **pages**. We will mainly use **blog**.
* Copy template.md to your new file.
* Edit and add the content you want.
* Back up a directory and type ***make html***.
* Type ***make serve***, start a browser and link to host:8000.
* Once you are happy, *** `ghp-import -b master output` ***.
- Finally push to github, *** git push origin master ***. You will need your github id (email) and password.

---
## Links
- [Creating github static website](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html "Link")
- [ghp-import and tips](https://www.entilzha.io/blog/2015/09/15/github-website-with-pelican/ "Link")
- [Tutorials](https://github.com/getpelican/pelican/wiki/Tutorials "Link")
- [Workflow githooks](http://anotherdatum.com/pelican-and-github-pages-workflow.html "Link")

