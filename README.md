# dcpp
# DevOps Core Practical Project

## Content
1. Background
2. The "Game"
3. Techincal Design
4. CI/CD
5. Unit Tests
6. Risk Assessment 
7. Project Management


## Background
The DevOps Core Practical project is supposed to display our skills in the use of DevOps technologies, CI/CD techniques, deploy tools and working strategies. It has been stated that this assessment does not concentrate on the actual program being deployed, rather the methods used to automatically install the application on the target hosts.

To that extent, the project must demonstrate, the use of:
* JENKINS and a CI/CD manager.
* DOCKER as a containerisation tool.
* DOCKER-SWARM as a deploy technology of choice.
* ANSIBLE as a configuration management tool.

The project must also include:
* A sample of the JIRA Board used during the application life cycle.
* A simple ERD.
* A Risk Assessement.


## The "Game"
The appilcation is a simple Cannon Ball / Target game. 

When the user presses the fire button, a simple service select an angle of cannon elevation from defined list, another service generates the muzzle velocity of the cannon ball from a defined rane.


The angle and velocity are sent to third service which calculates the distance travlle and how close to a 100 meter target the cannon balls land. This score is then rank from a direct hit scoring a BULLS EYE, in 10 meter inetrvals, giving an increaing rude message.

The complete set of data (angle, velocity and message), is persisted to a MySQL database, and the last 10 entries displayed under the latest result.

When accessed the screen displays:
![SCREEN0](images/dcpp_SCREEN0.PNG)

Pressing the fire button, fires the cannon ball and generates a score. The last 10 attempts are then displayed.
![SCREEN0](images/dcpp_SCREEN1.PNG)


## Techincal Design
The application is based on four seperate, python based services:
|Service|Description|
|-------|-----------|
|APP1   |Main GUI, reporting and trigger button|
|APP2   |Service that returns a randomly selected elevation angle|
|APP3   |Service that returns a randomly selected muzzle velocity|
|APP4   |Service that accepts the elevation and velocity, calculate the distance travelled and allocates a score and comment.

**APP1** also is responsible for recording the details of the firing to a table within a MYSQL database. The is database is a single table containing:

|Column|Type|Description|
|------|----|-----------|
|id       |Integer, Not Null|Row Identifier and Primary Key|
|velocity |Integer, Not Null|Muzzle Velocity|
|elevation|Integer, Not Null|Elevation Angle|
|result   |String, Not Null|Resultant text (details + ranking) from APP4|


### ERD:
A simple ERD disagram for this table:

![ERD](images/dcpp_ERD.png)

## CI.CD
The appilcation was developed in python, using Microsoft Visual Studio, linked to GITLAB. During the development process, regular updates where posted to the GIT DEV branch.

A Web-hook was attached to the GIT Repo, currently monitoring the DEV branch, (it will alter be moved to Main branch, if and when the application goes into production!!) 

The Repo also contained:
|File|Description|
|----|-----------|
|Jenkinsfile|Containing the pipeline build, upload and deploy the |application
|Dockerfiles|To build each service|
|Requerments.txt|Requerements for each service|



The Web-Hook triggers a Jenkins pipeline, that when trigger:
1. Downloads the application from the GIT Repo.
2. Runs PYTEST against the new code.
3. Runs the DOCKER-COMPOSE to create images for each services.
4. Uploads the new containers to DOCKERHUB.
![DOCKERHUB](images/dccp_Dockerhub.PNG)

## Unit Tests
The following unit test where created:
|Service|Test|Description|
|-------|----|-----------|
|APP1   |Assert200   |Access to access "/"|
|       |AssertIn    |Mock request for APP2, APP3 and APP4, to exercise APP2 request|
|APP2   |Assert200   |Access to elevation service|
|       |AssertIn    |Validate return value|
|APP3   |Assert200   |Access to veloicity service|
|       |AssertIn    |Validate return value|
|APP4   |Assert200   |13 tests for each ranking message (Over/Under shoot, Bulls Eye, 10 Ranings|


Happly able to validate 100% coverage:
![Unit Tests](images/dcpp_PYTEST.PNG)

## Risk Assessment
An initial Risk Assessment was completed on project commencement:
![Risk Assessment](images/dcpp_Risk_Assessment.PNG)

### Risk Assessment Revision
The following revisions where applied to the initial Risk Assessment:

## Project Manager
The JIRA Project Management tool was used to track and manage the application during the development, testing deployment cycle:
![JIRA Board](images/dcpp_JIRA_bord.PNG)

**NOTE:** The above graphic may not be an accurate reflection of the curreny JIRA tickets.

The current JIRA configuration allows:

Management of the "To-Do list" - user stories, summarising "Who Wants", "What they Want" and "What they except"

The "In progress" - containing items currently being worked on, or blocked items.

The "Done List" - Items that have been completed and tested, or approved.