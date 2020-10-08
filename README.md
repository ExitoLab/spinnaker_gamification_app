# Spinnaker Gamification App

## Mission & Vision

Vision: gamify and provide extrinsic motivation for Spinnaker and CDF contributions
Mission: by building an application that tracks indivudal contributions with a leaderboard and some other select aggregate data, and correlates those contributions to configurable professional profiles

We find a lot of use in this app: https://github.com/cncf/devstats and https://spinnaker.devstats.cd.foundation/ but are looking for individualized data


## Team

- Ige Adetokunbo
- Nikema Prophet
- Rosalind Benoit 
- Kuti
- Vishal

## 
The following technologies will be used 

1. Django rest framework 
2. React Js 
3. CI/ CD (Spinnaker, Jenkins, Github Actions)
4. Postgres MySQL


The various features of the application:

1. Integrate www.linkedin.com api 
2. Integrate https://github.com api 
3. If user supplies linkedin and github information. it will be displayed on the website and if nothing is supplied it will display basic information from github and a link to the registration page for user to register and add data to their contribution profile. 
4. A cron job (Golang) will run periodically and get information from github and insert into database. This will be a microservice  
5. The cron job will be able to trigger from the admin UI. Supply date and it will get information from linkedln

## Feature & APIs

Views:
1. Home Page - The idea for this page is to provide a few generalized project stats, and two period-configurable "leaderboards" that show the top (20?) contributors in the period (week/month/year). One list should show all contributors, and the other should filter out "Community Contributors" (all contributors minus those from Netflix, Google, and maybe Armory?) Below these lists, we hope to also add areas to browse recent human (non-bot) Pull Requests and Issues, with links to the relevant GitHub pages and to contributor profiles internally. Should link to devstats. Could have a "featured content" area sourced from user-provided links, automated display highly preferable for an OSS-maintained project.
1. Contribution Profile Page - Each GitHub username with project contributions in the Spinnaker organization should be associated with a profile page, perhaps generated by an array. Profile pages display links to contributions by that user and contribution stats - number of PRs/issues/comments, length of time since becoming a contributor, role in the Spinnaker project (can be none or from [list here](https://github.com/spinnaker/governance/blob/master/governance.md#roles)), list of CDF projects contributed to, and more (?). For users with a "claimed" account, this page will also optionally display a user-added photo, user-entered strings (Full name, about me, Spinnaker Slack handle, links to Spinnaker content) as well as LinkedIn account link, job title and company name data from LinkedIn, Medium account link, YouTube account link. 
1. Contributor Profile Claim & Edit Page
1. Admin Page or View

Features to test:
- Count individual user's submitted PRs - https://developer.github.com/v3/pulls/#list-pull-requests
- Count individual user's merged PRs - https://developer.github.com/v3/pulls/#list-pull-requests
- Count individual user's Issues - https://developer.github.com/v3/issues/#list-repository-issues
- Count individual user's Issue & PR Comments - https://developer.github.com/v3/issues/comments/#list-issue-comments
- Check role in the Spinnaker projects - scrape membership file at https://github.com/spinnaker/governance/blob/master/membership.yml

_Testing notes_: we are testing these APIs using curl, with guidance from [this article](https://www.softwaretestinghelp.com/github-rest-api-tutorial/). One issue we have run into is differentiating between usage of "organization" "owner" and "username" as used in these APIs. This query worked to reveal pull requests to the repo in question (clouddriver), but it is still unclear to us how we can filter this for a specific actor/user:

```
curl -X GET -u <username>:<token> https://api.github.com/repos/spinnaker/clouddriver/pulls?state="all" | grep state
```

```
curl -X GET -u <username>:<token> https://api.github.com/repos/ExitoLab/spinnaker_gamification_app/issues
```

```
>curl -X GET -u <username>:<token> https://api.github.com/repos/ExitoLab/spinnaker_gamification_app/issues/1/comments
```

```
curl -X GET -u <username>:<token> https://api.github.com/repos/ExitoLab/spinnaker_gamification_app/stats/contributors
```


Additional APIs that might be helpful:
- Get total number of commits in a repository authored by an individual contributor - https://developer.github.com/v3/repos/statistics/#get-all-contributor-commit-activity
- List contributors to a specified repo in order of number of contributions (detail for top 500 results) - https://developer.github.com/v3/repos/#list-repository-contributors
- Check if a user is a repo collaborator - https://developer.github.com/v3/repos/collaborators/#check-if-a-user-is-a-repository-collaborator

Features with no found API match:
- List of CDF projects contributed to. Some detail here: https://stackoverflow.com/questions/20714593/github-api-repositories-contributed-to
- Length of time since becoming a contributor. This is being monitored in some way here - https://spinnaker.devstats.cd.foundation/d/52/new-contributors-table?orgId=1 so we should dissect how they are doing this using [GHArchive](https://www.gharchive.org/)

Events to start with: 
- [PullRequestEvent](https://developer.github.com/v3/activity/event_types/#pullrequestevent) action=opened
- [IssueCommentEvent](https://developer.github.com/v3/activity/event_types/#issuesevent) action=opened
- [PullRequestReviewCommentEvent](https://developer.github.com/v3/activity/event_types/#pullrequestreviewcommentevent) action=created 
- [IssueCommentEvent](https://developer.github.com/v3/activity/event_types/#issuecommentevent) action=created 

Question:
1. What exact information of users should be displayed on the home page
1. We will need a wireframe of the homepage.. Just an idea, we can come up with the rest of the information.
1. Are we paying attention to the GitHub API limitations listed here https://github.com/cncf/devstats/blob/master/ARCHITECTURE.md#github-archives ?
1. What is the best data to display to show users that the project is popular and "hot"?

## User Journey

I am a new user who has contributed to Spinnaker
- I want to share my Spinnaker contributions that aren't on GitHub and show other users the complete picture of my engagement in OSS
- I want to find out my rank on the leaderboard
- I want to find out what is going on with the project this week/month/quarter
- I want to find new issues/projects that I can contribute to, where others are engaged or help is needed
- I want to find out how popular the project is
- I want to find links to all my contributions in one place
- I want to check and demonstrate how many Spinnaker repositories I have contributed to
- I want to check out my profile
- I want to drive traffic to my OSS content
- I want to feel validated that my contributions can have value

I am a new user who has not contributed to Spinnaker yet
- I want to feel welcomed and that I am joining a friendly community that will appreciate me
- I want to find out how popular the project is
- I want to browse Spinnaker content and contributions
- I want to decide whether or not to invest time in the Spinnaker project
- I want to see where the project needs are, and seek a match for my skillset
- I want to see an example of a successful pull request or other contribution
- I want to feel validated that my contributions can have value

I am a returning user
- I want to drive traffic to my OSS content
- I want to share my Spinnaker contributions that aren't on GitHub and show other users the complete picture of my engagement in OSS
- I want to find out my rank on the leaderboard
- I want to find out what is going on with the project this week/month/quarter
- I want to find new issues/projects that I can contribute to, where others are engaged or help is needed
- I want to find out how popular the project is
- I want to find links to all my contributions in one place
- I want to check and demonstrate how many Spinnaker repositories I have contributed to
- I want to feel validated that my contributions can have value

Next Steps:
1. Create a sketch of the views to use as a basline for wireframing
1. Find a designer to help with better wireframes
1. Gather API specs for all the data we want to display
1. Create a user journey
1. Ige & Rosalind do a short meeting to discuss backend next steps
1. Test consuming API calls on the events in the events list, and compare results to what we see in DevStats, and determine whether the results will meet our needs
1. Based on API output/testing, Ige will begin creating the database schema
1. Vishal will be working on React JS, pairing with Nikema, so he can begin once the API spec is done
1. Kuti & Nikema create HTML/CSS wireframe
1. Rosalind will check for CDF brand guide and give Kuti guidance on branding
1. Ige will re-add collaborators to calendar invite
1. Kuti will create a basic brand guide if needed
1. All will connect to collaborate async on Slack in [our Slack channel](https://spinnakerteam.slack.com/archives/C019EV8HA7Q)
1. Test API behavior in cases where users make commits that are components of Pull Requests submitted by other users. Can we reliably count commits and present an all-time total of merged and/or submitted commits?

Notes:
What APIs can we start consuming? Once you have the token set up it's pretty easy. Ige is going to check out DevStats and see what we can borrow. At this point, the plan is to use APIs where possible and githubarchive where not possible.

2 options:


Here is the usage information from Lukaz on how he pulls and processes the data for DevStats https://github.com/cncf/devstats/blob/master/USAGE.md

## Backlog

- Figure out how to handle redirect from GitHub - is redirect possible or do we need an instructions + link workaround?
- "Connect to my LinkedIn profile" dialog on User Profile (logged-in user) and User Profile Edit pages
- User search feature

