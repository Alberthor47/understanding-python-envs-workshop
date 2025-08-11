---
marp: true
theme: default
paginate: true
footer: "Python envs | Major League Hacking"
size: 16:9
title: "GHW Beginners"
---

# Understanding Python Environments Part 2

**Facilitator:** Alberto Camarena
**Presented at:** Global Hack Week 🌐 Beginners
**Date:** 11/08/25 📅

---

## Recap from Part 1

- What is a Python environment
- Tools: `venv`, `conda`
- How Python finds and loads packages

Quick quiz from Part 1:

- Command to check active interpreter?

---

## Hands-on: Creating Envs and Moving Through Them

**Goal:** Learn to create, activate, deactivate, and switch between environments efficiently.

**With `venv`**  
```bash
python -m venv myenv
source myenv/bin/activate   # macOS/Linux
myenv\Scripts\activate      # Windows
deactivate
````

**With `conda`**

```bash
conda create --name data-env python=3.10
conda activate data-env
conda deactivate
```

---

## Switching Between Multiple Environments

* **List available environments**

  * `conda env list`
  * Manually track `venv` folders
* **Quick switching tips**

  * Use aliases/functions in shell
  * Keep environments in a dedicated `~/envs` folder

---

## Best Practices 💡

* Always use a virtual environment for projects
* Keep dependencies minimal
* Use `requirements.txt` or `pyproject.toml`
* Pin exact versions for reproducibility

  ```bash
  pip freeze > requirements.txt
  ```
* Automate environment setup in README

---

## Containerizing Python Environments

**Why use containers?**

* Same env in dev, test, prod
* No “works on my machine” problem

**Minimal Dockerfile**

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

## When to Choose Containers vs. Virtual Envs

* **Virtual Envs**

  * Fast local development
  * Lightweight
  * No extra dependencies

* **Containers**

  * Cross-platform consistency
  * Deployment-ready
  * Isolation from host OS

---

## Final Takeaways

* Understand your environment **before** coding
* Use tools wisely (`venv`, `conda`, containers)
* Reproducibility saves time and headaches
* Keep environments clean and project-specific
* Document setup instructions for your team

---

## Q\&A ❓

Time to ask about:

* Edge cases you’ve faced
* Integration with existing workflows
* Recommendations for your specific stack
