
 git add <helloWorld.py>
mkdir git_task_project
cd git_task_project
git init
git status
echo "print('Hello World!')" > helloWorld.py
git status
git add helloWorld.py
git status
echo "print('Oit is awesome!')" > helloWorld.py
git status
git add helloWorld.py
git status
git commit -m "Changed message in helloWorld.py"
git status
git log