### Instructions for Students: Fetching, Pulling, and Merging Updates from the Instructor’s Base Repository in GitHub Codespaces

These instructions will guide you through updating your `starleap-intro-python` repository in GitHub Codespaces by fetching and merging changes from the instructor’s base repository (`https://github.com/EmilyNeel/starleap-intro-python`). This ensures you receive new materials, templates, or examples (e.g., new files in `chapters/01_2_lesson`) while keeping your existing work (e.g., `chapters/01_1_lesson/right_justify.py`). Follow each step carefully to avoid conflicts and keep your repository up-to-date.

#### Prerequisites
- You have a GitHub account and access to a Codespace for your `starleap-intro-python` repository, which is a fork or clone of the instructor’s repository (`https://github.com/EmilyNeel/starleap-intro-python`).
- You’re using the Codespace’s terminal or VS Code’s integrated terminal (accessible via `View > Terminal`).
- You’ve committed and pushed your current work to avoid losing changes (see previous instructions for adding, committing, and pushing).

#### Step-by-Step Instructions

1. **Open the Terminal in Codespaces**
   - In your Codespace, open the terminal:
     - Click the `Terminal` tab at the bottom of VS Code (or press `Ctrl + ~` or `Cmd + ~`).
     - Alternatively, go to `View > Terminal` in the menu.
   - Ensure the terminal prompt shows you’re in the repository directory (e.g., `/workspaces/starleap-intro-python`).

2. **Commit Your Current Work**
   - Before pulling updates, ensure your changes (e.g., to `chapters/01_1_lesson/right_justify.py`) are committed to avoid conflicts:
     ```bash
     git status
     ```
     - If you see modified or untracked files (e.g., `chapters/01_1_lesson/right_justify.py`), add and commit them:
       ```bash
       git add .
       git commit -m "Saved my work before pulling instructor updates"
       git push origin main
       ```
     - This ensures your work is saved on GitHub. If `git status` shows no changes, proceed to the next step.

3. **Add the Instructor’s Repository as a Remote**
   - Check if the instructor’s repository is already set as a remote named `upstream`:
     ```bash
     git remote -v
     ```
     - You’ll see remotes like:
       ```
       origin  https://github.com/your-username/starleap-intro-python.git (fetch)
       origin  https://github.com/your-username/starleap-intro-python.git (push)
       ```
     - If you don’t see `upstream`, add it using the instructor’s repository URL:
       ```bash
       git remote add upstream https://github.com/EmilyNeel/starleap-intro-python.git
       ```
     - Verify the remote was added:
       ```bash
       git remote -v
       ```
       - You should now see `upstream` listed:
         ```
         upstream  https://github.com/EmilyNeel/starleap-intro-python.git (fetch)
         upstream  https://github.com/EmilyNeel/starleap-intro-python.git (push)
         ```

4. **Fetch Updates from the Instructor’s Repository**
   - Fetch the latest changes from the instructor’s `main` branch without merging them:
     ```bash
     git fetch upstream main
     ```
     - This downloads updates (e.g., new files in `chapters/01_2_lesson`) to your local repository but doesn’t apply them yet.
     - Example output:
       ```
       remote: Enumerating objects: 5, done.
       remote: Counting objects: 100% (5/5), done.
       remote: Compressing objects: 100% (3/3), done.
       remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
       Unpacking objects: 100% (3/3), done.
       From https://github.com/EmilyNeel/starleap-intro-python
        * branch            main       -> FETCH_HEAD
       ```

5. **Merge the Instructor’s Updates**
   - Merge the fetched changes from `upstream/main` into your `main` branch:
     ```bash
     git merge upstream/main
     ```
   - If there are no conflicts, you’ll see a message like:
     ```
     Updating abc1234..def5678
     Fast-forward
      chapters/01_2_lesson/example.py | 10 ++++++++++
      1 file changed, 10 insertions(+)
      create mode 100644 chapters/01_2_lesson/example.py
     ```
   - This applies the instructor’s updates (e.g., new files or templates) to your repository.

6. **Handle Merge Conflicts (If Any)**
   - If you modified files that the instructor also updated, you may encounter a merge conflict:
     ```
     Auto-merging chapters/01_1_lesson/right_justify.py
     CONFLICT (content): Merge conflict in chapters/01_1_lesson/right_justify.py
     Automatic merge failed; fix conflicts and then commit the result.
     ```
   - To resolve:
     - Open the conflicting file (e.g., `chapters/01_1_lesson/right_justify.py`) in VS Code.
     - Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and edit to keep your changes, the instructor’s changes, or a combination.
     - Example:
       ```
       <<<<<<< HEAD
       def right_justify(s):
           print(s.rjust(70))
       =======
       def right_justify(s):
           print(s.rjust(80))  # Instructor updated width to 80
       >>>>>>> upstream/main
       ```
     - Decide which version to keep (e.g., your code, the instructor’s, or a mix), then remove the markers.
     - Save the file, then mark it as resolved:
       ```bash
       git add chapters/01_1_lesson/right_justify.py
       ```
     - Complete the merge:
       ```bash
       git commit
       ```
       - VS Code may open a commit message editor; save and close it to finish.

7. **Push Your Updated Repository**
   - After merging (and resolving any conflicts), push your updated repository to GitHub:
     ```bash
     git push origin main
     ```
   - Example output:
     ```
     To https://github.com/your-username/starleap-intro-python.git
        abc1234..def5678  main -> main
     ```
   - This ensures your repository includes both the instructor’s updates and your work.

8. **Verify the Updates**
   - Visit your repository on GitHub (e.g., `https://github.com/your-username/starleap-intro-python`).
   - Navigate to `chapters/01_2_lesson` and confirm new files (e.g., `example.py`) are present.
   - Check the commit history to see the instructor’s updates:
     - Click the `Commits` tab on GitHub to verify new commits from `upstream/main`.

#### Troubleshooting
- **“Nothing to merge”**:
  - If `git merge upstream/main` does nothing, ensure you fetched updates:
    ```bash
    git fetch upstream main
    ```
  - Check for new commits:
    ```bash
    git log upstream/main --oneline
    ```
- **Authentication Error on Fetch**:
  - Verify the `upstream` URL:
    ```bash
    git remote -v
    ```
    - Ensure it’s `https://github.com/EmilyNeel/starleap-intro-python.git`.
  - If prompted for a username/password, ensure you’re logged into GitHub in Codespaces.
- **Merge Conflicts**:
  - If conflicts persist, ask your instructor for help, providing the conflicting file and error message.
  - To abort a merge and start over:
    ```bash
    git merge --abort
    ```
- **Wrong Branch**:
  - Check your branch:
    ```bash
    git branch
    ```
  - If not on `main`, switch:
    ```bash
    git checkout main
    ```

#### Tips
- **Commit Before Merging**: Always commit your changes before fetching/merging to avoid losing work.
- **Check for Updates Regularly**: Run these steps whenever the instructor announces new materials (e.g., new lessons or templates).
- **Test After Merging**: After merging, test your code to ensure it still works:
  ```bash
  python3 chapters/01_1_lesson/right_justify.py
  ```
  Or use VS Code’s “Run Python File” button (top-right).
- **Contact the Instructor**: If you’re unsure about conflicts or updates, email your instructor with details (e.g., error messages, `git status` output).

#### Example Workflow
Suppose you need to pull a new example file (`chapters/01_2_lesson/example.py`) from the instructor’s repository:
1. Open the terminal in Codespaces.
2. Commit your changes:
   ```bash
   git add .
   git commit -m "Saved my work before pulling updates"
   git push origin main
   ```
3. Add the instructor’s remote (if not already added):
   ```bash
   git remote add upstream https://github.com/EmilyNeel/starleap-intro-python.git
   ```
4. Fetch and merge:
   ```bash
   git fetch upstream main
   git merge upstream/main
   ```
5. Push updates:
   ```bash
   git push origin main
   ```
6. Verify on GitHub: Check `https://github.com/your-username/starleap-intro-python` for new files.

### Notes for Students
- **Backup Your Work**: Commit and push your changes before merging to ensure your work is safe.
- **Ask for Help**: If you encounter Git errors, contact your instructor with the error message and output of `git status` or `git log --oneline`.
