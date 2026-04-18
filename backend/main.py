#Receptionist
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai 
from pydantic import BaseModel
import mysql.connector
from dotenv import load_dotenv
import os

#Load variables from .env file
load_dotenv()

app = FastAPI()

#IMPORTANT:This  allows your StackBlitz website to talk to your laptop
app.add_middleware(CORSMiddleware, allow_origins =["*"],allow_methods=["*"],allow_headers=["*"],)

# Setup gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

# setup Railway Cloud datatbase
db = mysql.connector.connect(host = os.getenv("MYSQL_HOST"), user = os.getenv("MYSQL_USER"), password =os.getenv("MYSQL_PASSWORD"), port = int(os.getenv("MYSQL_PORT")), database = os.getenv("MYSQL_DATABASE"))
cursor = db.cursor()

#Data model for incoming syllabus 
class SyllabusRequest(BaseModel):
    text:str

@app.post("/generate-plan")

async def generate_plan(request:SyllabusRequest):
    #A.Get AI response
    prompt =  f"Break this syllabus into small 45-min study task: {request.text}"
    response = model.generate_content(prompt)
    tasks_text = response.tes

    #B.Save to Railway # Using the 'syllabus_input' and 'ai_generated_tasks' columns we created 
    sql = "INSERT INTO study_tasks(syllabus_input,ai_generated_tasks) VALUES(%s,%s)"
    cursor.execute(sql,(request.text, tasks_text))
    db.commit()

    return {"tasks":response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)