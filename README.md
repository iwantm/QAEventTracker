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
This will be updated once a CI pipeline is in place


## Tracking
[Jira](https://iwanmoreton.atlassian.net/secure/RapidBoard.jspa?projectKey=ET&rapidView=1&view=planning.nodetail&atlOrigin=eyJpIjoiYTI3YjZmOWI3MGVhNGQxM2JiMDYyZDY1MTI3MzYzYzciLCJwIjoiaiJ9) was used to track the progress of the project.
![Imgur](https://i.imgur.com/xsUwKVu.png)
I used Jira to create 2 epics, one for the user account system and one for the events, these were then split into user stories created as issues. This allowed me to create different sprints for the project consisting of various issues. Each issue was set a priority for the application and given story points dependant on how much time I believed it would take to complete. The Jira board allowed me to check the backlog to see which feature needed compeleting and then to add similar features to a sprint, which then allowed me for each issue of the sprint to track whether the issue was 'in progress' or done. This would also allow me to create reports for bigger projects.

## Risk Assessment
The full risk assessment can be found [here](https://docs.google.com/spreadsheets/d/1Q3bw1Kq9GwS-QO11yzzbHXt3JxtC32gwJgP5J90frmQ/edit?usp=sharing).

![Imgur](https://i.imgur.com/1nbF4hl.png)

## Testing
### Unit Testing
Pytest is used for unit testing the application. These tests are designed to check that the outputs from the application are correct. These are then used to produce a report allowing me to check the coverage of the tests.
![Imgur](https://i.imgur.com/UxBaUiv.png)
Pytest also allows you to produce a coverage report in HTML to show how far the app has been tested.
![Imgur](https://i.imgur.com/cFEM6td.png)
### Integration Testing
Selenium is used for integration testing. These tests are designed to make sure that the front end of the application is working as expected and that it produces the correct outcome.

## Front-End
The front-end of the application is built using HTML and the Bootstrap framework. It's functional and allows the user to achieve every thing set out.
### Home Page

### Registration

### Logging In

### Viewing Account

### Editing Account

### Adding Event

### Viewing Event

### Editing Event







