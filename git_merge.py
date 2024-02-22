# Change directory to the project folder
cd git_task_project

# Create a new branch called issue-1
git branch issue-1

# Switch to the issue-1 branch
git checkout issue-1

# Modify the helloWorld.py file to accept input from the user and print it out
nano helloWorld.py

# Replace the existing code with the following:
```python
def main():
    user_input = input("Enter a word: ")
    print(f"You entered: {user_input}")

if __name__ == "__main__":
    main()