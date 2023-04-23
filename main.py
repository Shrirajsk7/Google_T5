from fastapi import FastAPI, Response,status,FastAPI, File, Form, UploadFile
from pydantic import BaseModel
# import streamlit as st
import helper
import pickle
from app import generate_questions


class FAQ(BaseModel):

    topic: str

app = FastAPI()

        

@app.post("/api/topic_data",status_code=200)
async def upload_topic(topic: str = Form(), number_of_questions: str = Form()):

    generated_question = generate_questions(str(topic),int(number_of_questions))

    non_duplicated_question_list = [s.strip() for s in generated_question]

    question_list = [element for element in non_duplicated_question_list if element != ""]

    return question_list

