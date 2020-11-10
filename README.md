# Event Tracker
### Useful Links
- [Jira Board](https://iwanmoreton.atlassian.net/secure/RapidBoard.jspa?projectKey=ET&rapidView=1&view=planning.nodetail&atlOrigin=eyJpIjoiYTI3YjZmOWI3MGVhNGQxM2JiMDYyZDY1MTI3MzYzYzciLCJwIjoiaiJ9) 
- [Website](QA.iwantm.me)
## Contents
- [Brief](#brief)
    - [Requirements](#requirements)
    - [My Approach](#my-approach)
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

## Architecture

### Database
The database structure has changed during development with the changes shown in the below ERD diagrams.

![Imgur](https://i.imgur.com/wG0J7qh.png)

This diagram is how I thought the database would be initially, before I decided that the relationship between users and events should be many-to-many

![Imgur](https://i.imgur.com/vR6iOTW.png?1)