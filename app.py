import requests
import os
import numpy as np
import pandas as pd
from questiongenerator import QuestionGenerator
import csv
import helper
import pickle
           
qg = QuestionGenerator()

def generate_questions(article,num_que):
    result = ''
    if article.strip():
        if num_que == None or num_que == '':
            num_que = 3
        else:
            num_que = num_que
        generated_questions_list = qg.generate(article, num_questions=int(num_que))
        summarized_data = {
            "generated_questions" : generated_questions_list
        }
        generated_questions = summarized_data.get("generated_questions",'')
        
        list_of_question = []
        for q in generated_questions:
            print(q)
            questions = result + q + '\n'
            list_of_question.append(questions)

        # print("sending result***!!!!!!", questions)
        model = pickle.load(open('model.pkl','rb'))
        non_duplicate_questions = []
        
        for i in range(1, len(list_of_question)):
            query = helper.query_point_creator(list_of_question[0], list_of_question[i])
            result_1 = model.predict(query)[0]
            print(result_1)
            if not result_1:
                non_duplicate_questions.append(list_of_question[i])

        non_duplicate_questions.insert(0, list_of_question[0])

    return non_duplicate_questions





    
