# Welcome to our Travel Website

## How to use our Site
- In order to use our Site you must first clone the github link onto intellij. Once cloned, navigate to the main.py file and run the program. It may ask you to configure python, make sure to do that as well. Once running, use the nav bars and titles to navigate to different areas of the website and view all our projects and project resources.

## Features
- Our site provides a home page allowing the user to view all sorts of projects we as a scrum team have worked on during trimester 1 of AP CSP
- Features navbars that allow the user to easily navigate to different areas of the site, whether it be our Hello Series, Home Page, or Flask Project.
- Features resources and links to code on our home page for our Hello Series project and Flask project.
- Features a nice Travel Website that allows the user to explore all the famous areas in San Diego, from beaches to parks to restaurants.


## TODO (From most recent to least recent)
- Marc will work on fixing up the formatting through CSS to ensure that the site runs well on all devices
- Dk, Jason, and Jacob will add final touch ups to descriptions of each place featured in our website
- Marc will work on integrating the Travel Website into the Night of The Museum website
- Allen will work on combining the Web Portfolio along with the Travel Website
- Look over the descriptions of each place, making sure it's easy to read and descriptive and not too redundant
- Jason, Dk, and Jacob will work on the Park page of our website, making sure to embed the links and provide a nice aesthetic to the page
- Marc will apply the layout. Jason, DK, and Jacob designed from the Park page onto the Restaurants page of the site, making changes to images and format when necessary via CSS
- Allen will then apply this layout to the Beaches page, making changes to backgrounds, formats, and images via CSS when necessary.

## Github Files 
- Our main.py file is how we run everything on our site. We use it to create routes to different pages, allowing us to put different information on each page. As you can see, we created routes to all sorts of different places, like our park page, beach page, travel page, and more. If you look at the url, you can see how it changes based on which page you go to. For example, http://ntm.nighthawkcoders.cf/p5_monkeymens/beach/ here you cans ee the /beach/ which sends you to the beach section, and http://ntm.nighthawkcoders.cf/p5_monkeymens/restaurant/ here you can see the /restaurant/ which sends you to the restaurent section, and all of this is done through our main.py file. 
- Our templates folder is how we create and edit each of these pages. In the folder, you can see all the different .html files we have. Because we are combining 2 different websites, we needed 2 bases, which can be seen with base.html and travelbase.html. From there, all the other .html files follow the template of either base.html or travelbase.html. Using Jinja, we can make edits to the template in the other files, allowing us to easily make changes and add new pages to our website. 
- Our data.py folder allowed us to define variables and store them all in a seperate file. This way, when we needed a certain link, name, or anything else, we could first store the information in our dawta.py folder, then import it over to our other files and use the variables there. With easy access to these variables, it makes coding the other files much easier and efficent.
