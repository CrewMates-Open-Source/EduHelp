
﻿<h1 align="center">EduHelp</h1>
<p align="center">
	<img src="https://user-images.githubusercontent.com/68437435/111764796-a00de000-88c9-11eb-88ba-56369207aabd.gif" width=300 height=300 alt="Banner">
</p>

[![Number of Contributors](https://img.shields.io/github/contributors/CrewMates-Open-Source/EduHelp)](https://github.com/CrewMates-Open-Source/EduHelp/graphs/contributors)
  [![Issues opened](https://img.shields.io/github/issues/CrewMates-Open-Source/EduHelp)](https://github.com/CrewMates-Open-Source/EduHelp)
  [![Issues closed](https://img.shields.io/github/issues-closed/CrewMates-Open-Source/EduHelp)](https://github.com/CrewMates-Open-Source/EduHelp/issues)
  [![PRs open](https://img.shields.io/github/issues-pr/CrewMates-Open-Source/EduHelp)](https://github.com/CrewMates-Open-Source/EduHelp/pulls)
  [![PRs closed](https://img.shields.io/github/issues-pr-closed/CrewMates-Open-Source/EduHelp)](https://github.com/CrewMates-Open-Source/EduHelp/pulls)
  ![Repo size](https://img.shields.io/github/repo-size/CrewMates-Open-Source/EduHelp)
  [![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
 
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

## What does it do? :thinking:
**EduHelp** simply means to make it easier for you to *record any online session*, be it an online lecture, meetings, youtube tutorials, etc. But we are not simply making a web extension or desktop app that records your screen or gives you an audio file in the end. We mean to *save the slide show* or screen presentation going on during those meets as well as the *text file of the entire conversation* that took place. This Project will not only help normal people but also *differently-abled people* because the audio is converted to text and a file containing its summary is saved in a .txt file as well as *braille script file*. The braille file can be given as an input to refreshable braille display (rbd) machines. The audio files can also be used by a blind person for taking note of what happened during class. The screenshots are stored in a .docx file and can be used by a deaf person for revisiting concepts they might miss during classes.
<h2 align="center">AMAZING!!😮:star_struck:RIGHT?</h2>

## Demo
Want to know more about EduHelp. Just look below :point_down:
<p align="center">
  <img src="Assets/crewmates.gif"></img>
</p>

[Youtube Link](https://youtu.be/qgMU8F1QX5g)

## What do we think of implementation?
 - There are a lot of features that need to be implemented for this project. To know what are those please click :point_right:[here](https://docs.google.com/document/d/1NgP7kcJPSz0XaIq51hJkgtHk4Pm7J58N76-_0py2DTc/edit?usp=sharing).
 - We would love to add other features to this project. It will be greatly appreciated if you contribute to this project and we ensure, it will be given a higher rating, i.e. level1, level2, level3 based on the usefulness and how inspirational your idea is, hereby idea I mean just the idea and the flow of Idea in a `.md` file. If you can write your code for the idea you suggested, we will deal with it in separate PR’s and with different level tags.

## Tech-Stacks 💻
- For website: `HTML`, `CSS`
- For core functionalities: `Python`
- For summarizer part: `NLP`
- For different Speech audio being clustered: `ML`
- `Electron.js` or `Tkinter` or any other desktop app development stack.
- For making all the functionalities available as an API: `Flask Backend`

## How to get started?
<h3 align="center">A beginner and don't know how and where to start???</h3>
<p align="center">
   <img src="https://user-images.githubusercontent.com/68437435/111859661-70fa7b80-8968-11eb-809d-a8e9a7266917.gif" width=300 height=200>
</p>
Don't worry, you can refer to the following articles and also contact the project maintainers, in case you are stuck:

## GIT AND GITHUB

Before continuing we want to clarify the difference between Git and Github. Git is a version control system(VCS) which is a tool to manage the history of our Source Code. GitHub is a hosting service for Git projects.

We assume you have created an account on Github and installed Git on your System.

Now tell Git your name and Email (used on Github) address.

     $ git config --global user.name "YOUR NAME"
     $ git config --global user.email "YOUR EMAIL ADDRESS"
     

This is an important step to mark your commits to your name and email.

### FORK A PROJECT -

You can use github explore - https://github.com/explore to find a project that interests you and match your skills. Once you find your cool project to work on, you can make a copy of the project to your account. This process is called forking a project to your Github account. On Upper right side of project page on Github, you can see -

<p align="center">  <img  src="https://i.imgur.com/P0n6f97.png">  </p>

Click on fork to create a copy of the project to your account. This creates a separate copy for you to work on.

### FINDING A FEATURE OR BUG TO WORK ON - 

Open Source projects always have something to work on and improve with each new release. You can see the issues section to find something you can solve or report a bug. The project managers always welcome new contributors and can guide you to solve the problem. You can find issues in the right section of the project page.

<p align="center">  <img  src="https://i.imgur.com/czVjpS7.png">  </p>

### CLONE THE FORKED PROJECT -

You have forked the project you want to contribute to your github account. To get this project on your development machine we use the clone command of git.

```$ git clone https://github.com/<your-account-username>/<your-forked-project>.git```  
Now you have the project on your local machine.

### ADD A REMOTE (UPSTREAM) TO ORIGINAL PROJECT REPOSITORY 

Remote means the remote location of a project on Github. By cloning, we have a remote called origin which points to your forked repository. Now we will add a remote to the original repository from where we had forked.

    $ cd <your-forked-project-folder>
    $ git remote add upstream https://github.com/<author-account-username>/<project>.git
    
You will see the benefits of adding a remote later.

### SYNCHRONIZING YOUR FORK -

Open Source projects have a number of contributors who can push code anytime. So it is necessary to make your forked copy equal with the original repository. The remote added above called Upstream helps in this.


    $ git checkout master
    $ git fetch upstream
    $ git merge upstream/master
    $ git push origin master
  

The last command pushes the latest code to your forked repository on Github. The origin is the remote pointing to your forked repository on github.

### CREATE A NEW BRANCH FOR A FEATURE OR BUGFIX -

Normally, all repositories have a master branch which is considered to remain stable and all new features should be made in a separate branch and after completion merged into master branch. So we should create a new branch for our feature or bugfix and start working on the issue.

```$ git checkout -b <feature-branch>```
This will create a new branch out of the master branch. Now start working on the problem and commit your changes.

    $ git add --all
    $ git commit -m "<commit message>"
    

The first command adds all the files or you can add specific files by removing -a and adding the file names. The second command gives a message to your changes so you can know in future what changes this commit makes. If you are solving an issue on original repository, you should add the issue number like #35 to your commit message. This will show the reference to commits in the issue.

### REBASE YOUR FEATURE BRANCH WITH UPSTREAM-

It can happen that your feature takes time to complete and other contributors are constantly pushing code. After completing the feature your feature branch should be rebased on latest changes to upstream master branch.

    $ git checkout <feature-branch>
    $ git pull --rebase upstream master

Now you get the latest commits from other contributors and check that your commits are compatible with the new commits. If there are any conflicts, solve them.

### SQUASHING YOUR COMMITS-

You have completed the feature, but you have made a number of commits which make less sense. You should squash your commits to make good commits.

```$ git rebase -i HEAD~5```    
This will open an editor which will allow you to squash the commits.

### PUSH CODE AND CREATE A PULL REQUEST -

Till this point you have a new branch with the feature or bug fix you want in the project you had forked. Now push your new branch to your remote fork on github.

```$ git push origin <feature-branch>```
    
Now you are ready to help the project by opening a pull request means you now tell the project managers to add the feature or bugfix to the original repository. You can open a pull request by clicking on green icon -

<p align="center">  <img  src="https://i.imgur.com/aGaqAD5.png">  </p>

Remember your upstream base branch should be master and source should be your feature branch. Click on create pull request and add a name to your pull request. You can also describe your feature.

Awesome! You have made your first contribution. If you have any doubts please let me know in the comments.

#### BE OPEN!

## How to contribute?
- Read this [contribution guide](Contibution_Guidelines.md), it will give you a detailed explanation of how, what and where to contribute. 
- Now take a look at the existing [issues](https://github.com/CrewMates-Open-Source/EduHelp/issues) or create your issues!
- Wait for the issue to be assigned to you after which you can start working on it.
- Fork the repo and create a branch for any issue that you are working upon.
- Create a pull request which will be promptly reviewed and suggestions would be added to improve it.
- If applicable, add screenshots to show the changes you made.
- Last but not least don't forget to have fun while contributing.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## ❤️ Project Admin

|                                     <a href="#"><img src="https://avatars.githubusercontent.com/u/58778597?" width=100px height=100px />                                     |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                      **[Shankhanil Borthakur](https://github.com/shankhanil007)**                                                                                       |
| <a href="https://www.linkedin.com/in/shankhanil-borthakur-00069019a/"><img src="https://mpng.subpng.com/20180324/vhe/kisspng-linkedin-computer-icons-logo-social-networking-ser-facebook-5ab6ebfe5f5397.2333748215219374063905.jpg" width="32px" height="32px"></a> |

## 👨‍💻 Mentors

<table>
<tr>
    <td align="center" thead="Mentor"><a href="https://github.com/Apurva-tech"><img src="https://avatars.githubusercontent.com/u/59837325?" width="100px;" alt="Mentor"/><br /><sub><b>Apurva</b></sub></a></td>
    <td align="center" thead="Mentor"><a href="https://github.com/GrayFlash"><img src="https://avatars.githubusercontent.com/u/57063469?" width="100px;" alt="Mentor"/><br /><sub><b>Gaurav Kumar</b></sub></a></td>
    <td align="center" thead="Mentor"><a href="https://github.com/D3ADSH0T25"><img src="https://avatars.githubusercontent.com/u/57529264?" width="100px;" alt="Mentor"/><br /><sub><b>Anshoo Rajput</b></sub></a></td>
  </tr>
  </table>

## Open source program(s)
- GirlScript summer of code (2021)
<p align="center">
  <a href="https://gssoc.girlscript.tech/"><img src="https://user-images.githubusercontent.com/68437435/110908762-493a6080-8335-11eb-8dd8-a0f184767fd3.png"></img></a>
</p>

## License
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This project is licensed under GPL v3. To know more about it you can refer [LICENSE](LICENSE).

## Contributors 

### Credits goes to these people:✨

<table>
<tr>
	<td>
	  	<a href="https://github.com/CrewMates-Open-Source/EduHelp/graphs/contributors">
  			<img src="https://contrib.rocks/image?repo=CrewMates-Open-Source/EduHelp" />
		</a>
	</td>
</tr>
</table>


