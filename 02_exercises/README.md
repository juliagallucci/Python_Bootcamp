
This folder contains daily Python exercises for participants to practice and reinforce key programming concepts.

## Exercise Submission Workflow

For each assignment, you will use a simple **branch → commit → pull request (PR)** workflow.

We will use GitHub to practice real-world version control.

---

### 1. Create a new branch

Before starting your exercise, create a new branch from `main`:

```bash id="b1k8qp"
git checkout -b day-1-exercise
```

Use a descriptive name (e.g., `day-1-exercise`, `day-2-exercise`, etc.).

---

### 2. Complete your work

Do your coding in this branch (using **Google Colab**).

> Note: Even if you work in Colab, make sure your final notebook is saved and included in your GitHub repository before committing.

---

### 3. Stage and commit your changes

```bash id="m4x9ld"
git add .
git commit -m "Completed Day 1 Exercises"
```

---

### 4. Push your branch to GitHub

```bash id="t8v3nc"
git push origin day-1-exercise
```

---

### 5. Create a Pull Request (PR)

* Go to your GitHub repository
* Click **“Compare & pull request”**
* Set:

  * **base:** `main`
  * **compare:** `day-1-exercise`
* Submit the PR

---

### 6. Do not merge your own PR

Leave the pull request open for review/submission.

---

## Important Notes

* Always branch off `main` before starting an exercise
* Never work directly on `main`
* Each exercise should have its own branch
* Keep commits clear and meaningful
* Make sure your Colab notebook is saved and pushed to GitHub before submitting
