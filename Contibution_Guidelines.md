# Contributing to [EduHelp](https://github.com/CrewMates-Open-Source/EduHelp):

## Lets Start:

- Look at the existing Issues or create your own issue.
- Before starting, wait for the issue to be assigned to you.
- Fork the [repo](https://github.com/CrewMates-Open-Source/EduHelp) and create a branch with a appropriate name.
- Create a PR and add suggestions to the changes made.
- Add images to help us know what this PR is all about.

## Let's get on work:

**1.** Fork [this](https://github.com/CrewMates-Open-Source/EduHelp) repository. Now you will get a local copy of the repo on your GitHub Profile.

**2.** Clone the forked repository.

```bash
git clone https://github.com/<your-github-username>/EduHelp
```


**3.** Navigate to the project directory.

```bash
cd EduHelp
```

**4.** Add a reference to the original repository, to keep this reference to the original project in the `upstream`.

```
git remote add upstream https://github.com/CrewMates-Open-Source/EduHelp 
```

**5.** Check the remotes for this repo.

```
git remote -v
```

**6.** Always take a pull from the upstream repository to your master branch to keep it at par with the main project.

```
git pull upstream master
```

**7.** Create a new branch.

```
git checkout -b <your_branch_name>
```

**8.** Make changes in the code as required.

**9.** Add changes to the branch you've just created by:

```bash
# To add all new files to branch Branch_Name 
git add . 

# To add only a few files to Branch_Name
git add <files>
```

**10.** Commit your changes .

```bash
git commit -m <message>
```

**11.** Push the committed changes in your feature branch to your remote repo.

```bash
git push -u origin <your_branch_name>
```

**12.** Create a [PR](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) !

**13.** **Congrats!** Sit back and relax, you've made your contribution to [EduHelp](https://github.com/CrewMates-Open-Source/EduHelp) project. Give us some time so that we can review it and reply back to you.🤗

## Note:

- Set up a local env_setup refer [this](https://github.com/CrewMates-Open-Source/EduHelp/blob/GSSoC21/Starter.md), if you are looking to work on Python Scripts and NLTK.

- If you are willing to work on any of the utils files, i.e., the functionalities part you can refer to our codebase in the [main](https://github.com/CrewMates-Open-Source/EduHelp/tree/main) branch.

- It is important to understand the Issue before asking for getting assigned, and while commenting you have to comment on your approach you think could work, it should not be strictly correct or a complete implementation but a starting point for the same. This ensures that you have done some research on the project. 

- Even presenting and sharing your ideas will be a great Issue and we will accept your PR with that idea and assign tags as per the improvements. You can hence ask for multiple PR’s if you wish to add the code as well, an example of Idea will be: replacing some algorithm from the functionality that boosts performance and accuracy. Shifting to a different module that gives a stable result is also a great issue.

- At any point if you feel stuck, contact any of the mentors on Discord, and be patient.

- It takes time to get used to development and we all go through the same stage while we get started, hence it is alright to ask silly doubts.

## License
By contributing, you agree that your contributions will be licensed under the [GNU General Public License v3.0](https://github.com/CrewMates-Open-Source/EduHelp/blob/GSSoC21/LICENSE).