1. Fork this repository.
2. Clone the forked repository.
```
  git clone   https://github.com/CrewMates-Open-Source/EduHelp
```
3. Navigate to the project directory.
```
cd  EduHelp
```
4. Create a new branch.
```
git checkout -b <your_branch_name>
```
5. Setting up venv-environment

```
python3 -m venv env               (Create a separate Environment)

source env/bin/activate           (Activate the environment)

pip3 install -r requirements.txt  (Install's the dependencies)
```
6. Running flask server

````
export FLASK_ENV=development    (To set flask server in development mode)
````

 flask run to start the server.
(Blog part needs MySQL setup and hence we were not able to resolve it for a windows.)

7. Make changes in source code.

8. To Commit your changes. (use git)
```
git commit -m "Message"
```
9. Push your local branch to the remote repository.
```
git push -u origin <your_branch_name>
```
10. Create a Pull Request!

Finally, go to your repository in browser and click on compare and pull requests.
Then add a title and description to your pull request that explains your precious effort.

click on Compare and Pull Request


Congratulations! boom Sit and relax, you've made your contribution to Crewmates project.


