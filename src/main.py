import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Class Profile API",
    description="Reads student profile JSON files from the profiles directory",
    version="1.0.0",
)

PROFILES_DIR = Path("profiles")


class Profile(BaseModel):
    name: str
    title: str
    bio: str
    skills: list[str]


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Class Profile API!",
        "endpoints": ["/profiles", "/profiles/{student_name}"],
    }


@app.get("/profiles")
def list_profiles():
    """List all student profile names available."""
    if not PROFILES_DIR.exists():
        return {"profiles": []}

    files = [f.stem for f in PROFILES_DIR.glob("*.json")]
    return {"profiles": files}


@app.get("/profiles/{student_name}", response_model=Profile)
def get_profile(student_name: str):
    """Read a specific student's JSON profile and validate it with Pydantic."""
    file_path = PROFILES_DIR / f"{student_name.lower()}.json"

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Profile for '{student_name}' not found.",
        )

    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error parsing profile JSON: {str(e)}",
        )


@app.get("/health")
def health_check():
    return {"status": "healthy"}
