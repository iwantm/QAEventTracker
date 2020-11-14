# Event Tracker
### Useful Links
- [Jira Board](https://iwanmoreton.atlassian.net/secure/RapidBoard.jspa?projectKey=ET&rapidView=1&view=planning.nodetail&atlOrigin=eyJpIjoiYTI3YjZmOWI3MGVhNGQxM2JiMDYyZDY1MTI3MzYzYzciLCJwIjoiaiJ9) 
- [Website](QA.iwantm.me)
## Contents
- [Brief](#brief)
    - [Requirements](#requirements)
    - [My Approach](#my-approach)
- [Architecture](#architecture)
    - [Database](#database)
    - [CI Pipeline](#ci-pipeline)
- [Tracking](#tracking)
- [Risk Assessment](#risk-assessment)
- [Testing](#testing)
    - [Unit Testing](#unit-testing)
    - [Integration Testing](#integration-testing)
- [Front-End](#front-end)
    - [Home Page](#home-page)
    - [Registration](#registration)
    - [Logging In](#logging-in)
    - [Viewing Account](#viewing-account)
    - [Editing Account](#editing-account)
    - [Adding Event](#adding-event)
    - [Viewing Event](#viewing-event)
    - [Editing Event](#editing-event)
- [Improvements](#improvements)

## Brief

### Requirements

The requirements the project had to meet were:
- A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.
- A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
- Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
- A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board
- Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
- A functioning front-end website and integrated API's, using Flask.
- Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

### My Approach
To meet these requirements I have decided to create an event tracking application that will allow the user to:
- Create an account that stores:
    - **Username**
    - **Email**
    - **Password**
- Create events that store:
    - **Title** of the event
    - **Description** of the event
    - **Date** of the event
- View and update account information
- View and update events
- Delete accounts and events
#### Stretch Goal
- Invite other users to events
- See events in a calendar format
- Reoccuring events

## Architecture

### Database
The database structure has changed during development with the changes shown in the below ERD diagrams.

![Imgur](https://i.imgur.com/ErfdXLT.png)

This diagram is how I thought the database would be initially, before I decided that the relationship between users and events should be many-to-many with a sub table.

![Imgur](https://i.imgur.com/vR6iOTW.png?1)

This diagram is the final database structure with the description added to the event to allow for more information, the name removed from the user as it wasn't necessary, and the sub-table group added to allow many users to have many events.

### CI Pipeline
For the CI Pipeline I used Jenkins, I used two build steps with the first one being pytest tests with an XML output, and the second one uses Gunicorn to serve the application on port 5000. This gives me a graph on the jenkins home page which shows the tests passed and failed for each build.
! [Imgur](https://i.imgur.com/w47dFYx.png)

## Tracking
[Jira](https://iwanmoreton.atlassian.net/secure/RapidBoard.jspa?projectKey=ET&rapidView=1&view=planning.nodetail&atlOrigin=eyJpIjoiYTI3YjZmOWI3MGVhNGQxM2JiMDYyZDY1MTI3MzYzYzciLCJwIjoiaiJ9) was used to track the progress of the project.
![Imgur](https://i.imgur.com/xsUwKVu.png)
I used Jira to create 2 epics, one for the user account system and one for the events, these were then split into user stories created as issues. This allowed me to create different sprints for the project consisting of various issues. Each issue was set a priority for the application and given story points dependant on how much time I believed it would take to complete. The Jira board allowed me to check the backlog to see which feature needed compeleting and then to add similar features to a sprint, which then allowed me for each issue of the sprint to track whether the issue was 'in progress' or done. This would also allow me to create reports for bigger projects.

## Risk Assessment
The full risk assessment can be found [here](https://docs.google.com/spreadsheets/d/1Q3bw1Kq9GwS-QO11yzzbHXt3JxtC32gwJgP5J90frmQ/edit?usp=sharing).

![Imgur](https://i.imgur.com/1nbF4hl.png)

## Testing
### Unit Testing
Pytest is used for unit testing the application. These tests are designed to check that the outputs from the endpoints of the application are correct. These are then used to produce a report allowing me to check the coverage of the tests. This allows me to check which endpoints of the application still need testing. This was used to check that the correct data is being sent to the front end and that the correct data is being created in the database when routes are used. The problem with unit testing this application was that I had to turn validation off on the forms to allow for post requests to work. This meant that the finished application and the unit tested application were slightly different. There's a seperate **unit-testing** branch that has the changes made to the application to allow for unit testing to work.
![Imgur](https://i.imgur.com/UxBaUiv.png)
Pytest also allows you to produce a coverage report in HTML to show how far the app has been tested. Which is included in the files of the repository as a zip file.
![Imgur](https://i.imgur.com/IWLnB3b.png)
This is the HTML coverage report with the changes made to the application. This wasn't the final coverage as it meant that forms weren't validated. Because of the problems I faced with form validation in unit testing, forms.py isnt tested fully by the unit tests either.
![Imgur](https://i.imgur.com/6xXyfZN.png)
This is the coverage report with the tests removed as the post request didn't work correctly with form validation on. Although it's not shown in the report, the views that aren't covered are tested using integration testing.
### Integration Testing
Selenium is used for integration testing. As unit testing doesn't allow for the front-end to be tested as the user would see it, this is used to check if the routes work as expected when controlled how a user would interact with the website. This is done using the chromedriver and chromium to interact with the various front-end elements. In this project integration testing is used to test every form within the project, with the correct validation.

## Front-End
The front-end of the application is built using HTML and the Bootstrap framework. It's functional and allows the user to achieve every thing set out.
### Home Page
![Imgur](https://i.imgur.com/zlp0j7a.png?1)
### Registration
![Imgur](https://i.imgur.com/vDfTRvF.png?2)
### Logging In
![Imgur](https://i.imgur.com/vNNirGg.png?1)
### Viewing Account
![Imgur](https://i.imgur.com/75NUlq6.png?1)
### Editing Account
![Imgur](https://i.imgur.com/AZOHUpP.png?1)
### Adding Event
![Imgur](https://i.imgur.com/fpPha2e.png?1)
### Viewing Event
![Imgur](https://i.imgur.com/i1Xc042.png?1)
### Editing Event
![Imgur](https://i.imgur.com/lAXD2ZD.png?1)
### Adding User to Event
![Imgur](https://i.imgur.com/0V5rnKL.png?1)
## Improvements
There are a number of improvements that could be made to the application to make for a better user experience:
- Implementation of groups (properly) to allow for a user to select a group and then invite all members of that group.
- User acceptable invites, rather than the user being added directly.
- Automatic deletion of events that have passed.
- A user account system that allows for friends, profile pictures and more information about the user.
- A UI using JS and more CSS to make it more interactable and appealing.
- Turn the Jenkins server into an auto polling CI/CD pipeline. 

## Author
Iwan Moreton






