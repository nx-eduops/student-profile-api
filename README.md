# Student Profile API

A simple FastAPI application designed for teaching and learning Git & GitHub collaboration workflows.

Students can add their own profile JSON files, practice branching, merging, handling pull requests, and resolving merge conflicts.

---

## Project Structure

```text
my-profile/
├── profiles/          # Where student JSON profiles live
│   └── john_doe.json  # Example profile
├── src/
│   ├── __init__.py    # Python package marker
│   └── main.py        # FastAPI application code
├── requirements.txt   # Project dependencies
└── .gitignore         # Ignored files (virtual envs, cache, etc.)
```

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone git@github.com:nx-eduops/student-profile-api.git
cd my-profile
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the development server with live-reloading using Uvicorn:

```bash
uvicorn src.main:app --reload
```

Once running, open your browser and explore:

- **API Root:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive API Docs (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **List all student profiles:** [http://127.0.0.1:8000/profiles](http://127.0.0.1:8000/profiles)
- **View a specific profile:** [http://127.0.0.1:8000/profiles/john_doe](http://127.0.0.1:8000/profiles/john_doe)

---

## Git Assignment for Students

1. **Create your branch:**
   ```bash
   git checkout -b feature/profile-<your-name>
   ```
2. **Add your profile:**
   Create a new JSON file inside the `profiles/` directory named after yourself (e.g., `profiles/alice.json`). Use this format:
   ```json
   {
     "name": "Your Name",
     "title": "Your Role",
     "bio": "A short sentence about yourself.",
     "skills": ["Python", "FastAPI", "Git"]
   }
   ```
3. **Commit & Push:**
   ```bash
   git add profiles/<your-name>.json
   git commit -m "feat: add profile for <your-name>"
   git push origin feature/profile-<your-name>
   ```
4. **Open a Pull Request** on GitHub to merge your profile into `main`!
