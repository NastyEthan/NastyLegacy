{% include navigation.html %}


# Project Requirements

## Week 1

### First meeting with Mr. Mortensen

- [Initial Requirements/Ideas are on the linked wiki](https://github.com/NastyLegacy/NastyLegacy/wiki/New-Project-Plans-Ideas-Wires)
* First, we will build an SQL Database
* Establish columns that contain categories like period, group, name, contact
* Page for new students to add in their information. Old students should be able to delete and update their information (and only their own).
* Page for the teacher to view all the data
* Search function so that the teacher can easily find information for a particular student.
* Way to backup the database
* For the future: experimentation with other database types like mongo

## Week 2

### Second meeting with Mr. Mortensen

* Another encryption system/class code type thing so only students actually in the class can update
* For hosting: host personally on AWS for developing for now, but later on Mr. Mortensen's personally pi or AWS will host it
* Have security key to access the API as it has personal information of del norte students

## Week 8

### Third Meeting with Mr. Mortensen

* We spoke prior about having data for everything I need to interact with students and projects.  You seem to have started on student side, now I have added requirements on project side.  This is to have a database to help build this pages...
https://nighthawkcodingsociety.com/projectsearch/dash
* The idea is to build the CRUD frontend and rendering so that students could point to their projects.  
* This model is now using most of the relationship patterns in the documentation shown here:  https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
* Essentially, we need to work on a frontend that easily displays the many to many association between projects and users.

## Week 9

### Fourth Meeting with Mr. Mortensen

* Mr. Mortensen talked to us more about many to many associations. 
* The function to automate associations is good progress. Continue to work on front end, which is the hard part. 
* Next steps: Display projects from the site and have more intuitive UI.


# Progress

[ScrumBoard to show progress](https://github.com/NastyLegacy/NastyLegacy/projects/1)
[ScrumBoard 2](https://github.com/NastyLegacy/NastyLegacy/projects/2)
