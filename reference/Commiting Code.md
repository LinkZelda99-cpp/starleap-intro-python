# Committing Code

### Instructions for Students: Adding, Committing, and Pushing Changes in GitHub Codespaces

These instructions will guide you through saving your work and submitting it for grading by adding, committing, and pushing your changes to your `starleap-intro-python` repository in GitHub Codespaces. Follow each step carefully to ensure your work is saved and available for grading.

#### Prerequisites
- You have a GitHub account and access to a Codespace for your `starleap-intro-python` repository.
- You’ve edited or created files (e.g., `chapters/01_1_lesson/right_justify.py`) in the Codespace.
- You’re using the Codespace’s terminal or VS Code’s integrated terminal (accessible via `View > Terminal`).

#### Step-by-Step Instructions

1. **Open the Terminal in Codespaces**
   - In your Codespace, open the terminal:
     - Click the `Terminal` tab at the bottom of VS Code (or press `Ctrl + ~` or `Cmd + ~`).
     - Alternatively, go to `View > Terminal` in the menu.
   - Ensure the terminal prompt shows you’re in the repository directory (e.g., `/workspaces/starleap-intro-python`).

2. **Check Your Changes**
   - Before committing, see which files you’ve modified or created:
     ```bash
     git status
     ```
   - This will list files under:
     - `Changes not staged for commit` (modified files not yet added).
     - `Untracked files` (new files not yet tracked by Git).
   - Example output:
     ```
     On branch main
     Changes not staged for commit:
       (use "git add <file>..." to update what will be committed)
         modified:   chapters/01_1_lesson/hello_world.py
     Untracked files:
       (use "git add <file>..." to include in what will be committed)
         chapters/01_1_lesson/right_justify.py
     ```

3. **Add Your Changes**
   - Add specific files you want to commit (e.g., your assignment file):
     ```bash
     git add chapters/01_1_lesson/right_justify.py
     ```
   - To add all modified and new files in the `chapters/01_1_lesson` directory:
     ```bash
     git add chapters/01_1_lesson
     ```
   - To add all changes in the repository:
     ```bash
     git add .
     ```
   - Verify files are staged:
     ```bash
     git status
     ```
     - Staged files appear under `Changes to be committed`.

4. **Commit Your Changes**
   - Commit your staged files with a descriptive message:
     ```bash
     git commit -m "Completed right_justify.py for lesson 01_1"
     ```
   - The message should briefly describe your changes (e.g., “Added right_justify function” or “Updated hello_world.py”).
   - Example output:
     ```
     [main abc1234] Completed right_justify.py for lesson 01_1
      1 file changed, 10 insertions(+)
      create mode 100644 chapters/01_1_lesson/right_justify.py
     ```

5. **Push Your Changes to GitHub**
   - Push your commit to the `main` branch of your repository on GitHub:
     ```bash
     git push origin main
     ```
   - If your repository uses a different branch name (e.g., `master`), replace `main` with the correct branch name (check with `git branch`).
   - Example output:
     ```
     To https://github.com/your-username/starleap-intro-python.git
        abc1234..def5678  main -> main
     ```
   - This sends your changes to GitHub, where they can be pulled for grading.

6. **Verify Your Submission**
   - Visit your repository on GitHub (e.g., `https://github.com/your-username/starleap-intro-python`).
   - Navigate to `chapters/01_1_lesson` and confirm your file (e.g., `right_justify.py`) is present with your latest changes.
   - Check the commit history to ensure your commit is listed:
     - Click the `Commits` tab on GitHub to see your commit message (e.g., “Completed right_justify.py for lesson 01_1”).

7. **Save Your Work**
   - Codespaces automatically saves your files as you edit.
   - Committing and pushing ensures your work is backed up on GitHub and available for grading.
   - If you stop your Codespace, your changes are preserved, but always push to GitHub to ensure they’re submitted.

#### Troubleshooting
- **“Nothing to commit”**:
  - Run `git status` to ensure you’ve modified or added files.
  - If files are untracked, add them with `git add <file>`.
- **Authentication Error on Push**:
  - If prompted for a username/password, ensure you’re logged into GitHub in Codespaces.
  - Codespaces typically uses a GitHub token, so this is rare. If it occurs, run:
    ```bash
    git remote -v
    ```
    Ensure the remote URL is `https://github.com/your-username/starleap-intro-python.git`.
- **Wrong Branch**:
  - Check your branch with `git branch`. If not on `main`, switch with:
    ```bash
    git checkout main
    ```
  - Then push again.
- **File Not Found**:
  - Ensure you’re adding the correct file path (e.g., `chapters/01_1_lesson/right_justify.py`).
  - Verify the file exists:
    ```bash
    ls chapters/01_1_lesson
    ```

#### Tips
- **Commit Often**: Save your progress by committing after completing each part of an assignment.
- **Clear Commit Messages**: Use messages like “Added right_justify function” or “Fixed hello_world.py output” to help instructors understand your changes.
- **Test Your Code**: Before committing, test your code in the Codespace terminal:
  ```bash
  python3 chapters/01_1_lesson/right_justify.py
  ```
  Or use VS Code’s “Run Python File” button (top-right).

#### Example Workflow
Suppose you’ve edited `chapters/01_1_lesson/right_justify.py`:
1. Open the terminal in Codespaces.
2. Check changes:
   ```bash
   git status
   ```
3. Add the file:
   ```bash
   git add chapters/01_1_lesson/right_justify.py
   ```
4. Commit:
   ```bash
   git commit -m "Added right_justify function for lesson 01_1"
   ```
5. Push:
   ```bash
   git push origin main
   ```
6. Verify on GitHub: Check `https://github.com/your-username/starleap-intro-python`.

### Notes for Students
- **Do Not Modify Repository Structure**: Only edit files in `chapters/01_1_lesson` (e.g., `right_justify.py`, `hello_world.py`) unless instructed otherwise.
- **Ask for Help**: If you encounter Git errors, contact your instructor with the error message and output of `git status`.
