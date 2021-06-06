# dcpp
# DevOps Core Practical Project

## Content
1. Background
2. The "Game"
3. Risk Assessment 


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
The appilcation is a simple Cannon Ball / Target game. When the user presses the fire 
button, a simple service select an angle of cannon elevation from defined list, 
another service generates the muzzle velocity of the cannon ball from a defined rane.
The angle and velocity are sent to third service which calculates the distance travlle and how close to a 100 meter target the cannon balls land. This score is then rank from 
a direct hit scoring a BULLS EYE, in 10 meter inetrvals, giving an increaing rude message.
The complete set of data, is persisted to a MySQL database.


## Risk Assessment
An initial Risk Assessment was completed on project commencement:
![Risk Assessment](images/dcpp_Risk_Assessment.PNG)


### Risk Assessment Revision
