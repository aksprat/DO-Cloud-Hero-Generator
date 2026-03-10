from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import shutil
import uuid
import os

from backend.inference import generate_avatar
from backend.lead_storage import save_lead

app = FastAPI()

UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/generate-avatar")
async def create_avatar(
    name: str = Form(...),
    email: str = Form(...),
    company: str = Form(...),
    designation: str = Form(...),
    file: UploadFile = None
):

    if file:
        file_id = str(uuid.uuid4())
        file_path = f"{UPLOAD_DIR}/{file_id}.jpg"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    save_lead(name, email, company, designation)

    image_url = generate_avatar(name)

    return {
        "image": image_url
    }


@app.get("/download-leads")
def download_leads():
    return FileResponse("/tmp/leads.csv", filename="cloudconf_leads.csv")


# Serve frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
