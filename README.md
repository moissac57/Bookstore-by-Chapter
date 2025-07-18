# Bookstore-by-Chapter

## VERY IMPORTANT:

1. **Django for Professionals is outdated.**  
   I strongly advise you to download the Word Sheet included inside each chapter. This will help you avoid problems and save precious study time.

2. **Chapters 1, 2, and 3 set up the foundation** for the project, which actually starts in Chapter 4: Bookstore Project.

3. **Two ways to study this book:**

   **A.** Follow all chapters sequentially inside one folder on your code editor (I use VS Code, recommended by the author).

   **B.** Create a main folder (e.g., `Django for Professionals`), then inside it create **separate subfolders for each chapter**, like this:

Django for Professionals/
├── Chapter 01. Initial Set Up <-- setup for project
├── Chapter 02. Docker Hello, World! <-- setup for project
├── Chapter 03. PostgreSQL <-- setup for project
└── Chapter 04. Bookstore Project <-- project starts here

*Note:* I prefer option **B** because it makes reviewing chapters easier—your editor shows only code for the chapter you're studying. In real projects, you’ll usually work with just one folder.

4. The author recommends creating a **GitHub account**.  
You can push chapters to GitHub **chapter-by-chapter (not recommended)** or after finishing the entire book (recommended).  
Word Sheets are provided for each chapter.  
At the end, I show how to push chapters 1 to 9 if you want to use option A.

5. **Fix for Chapter 9 ("Environment Variables") outdated package issue:**

- In your `requirements.txt`, add this just after `environs==9.5.0`:

  ```
  django-allauth==0.50.0
  environs[django]==9.5.0   # existing
  marshmallow==3.20.1      # new, updated version
  ```

- Install both packages:

  ```bash
  pip install "environs[django]==9.5.0"
  pip install "marshmallow==3.20.1"
  ```

- Then run Docker commands:

  ```bash
  docker-compose down
  docker-compose up -d --build
  ```

- Fix VS Code Python interpreter for red squiggly under `environs`:

  1. Press `Ctrl + Shift + P`
  2. Type: `Python: Select Interpreter` → Enter
  3. Choose `Enter interpreter path`
  4. Click `Find...`
  5. Navigate to:
     ```
     C:\Users\your_name\Django for Professionals\Chapter 04. Bookstore Project\.venv\Scripts
     ```
  6. Select `python.exe`
  7. Click `Select Interpreter`
  8. When VS Code asks to reload terminal, click **Reload**  
  (If squiggly persists, repeat the process)

6. **How to push your chapters to GitHub:**

- Make sure your **local main folder name matches your GitHub repository name**.
- When creating a new repo on GitHub, choose the option to copy the first snippet of commands for pushing an existing repo.
- In your terminal, navigate to the folder you want to push.
- Run:

  ```bash
  git add "Chapter X. Title of the chapter"
  git commit -m "Add Chapter X. Title of the chapter"
  git push origin main
  ```

- Repeat for each chapter folder.

---

I hope this helps you save time and enjoy your study!  
Take your time to understand each chapter well.

— Jean-Marc

---

