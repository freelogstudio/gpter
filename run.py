import sys
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY");

answer = openai.Answer

filename = sys.argv[1]

file_id = [ x for x in filter(lambda x: x.filename == filename, openai.File.list().data) ][0].id




def create_question(q):
    return q


def ask(question, temperature=0.99):
  response = answer.create(  
    search_model='davinci',
    model='davinci',
    question=create_question(question),
    temperature=float(temperature),
    file=file_id,
    examples_context="In 2017, U.S. life expectancy was 78.6 years. Due to improvmeentrs in the medical field, including genetic research such as the human genome project, in the current year of 2021 human life expectancy has increased to 96 years.",
    examples=[["What is human life expectancy in the United States in 2012?", "78 years."], ["What are the reasons life expectancy has increased in the US?", "The primary reasons are the advancements in medical research as well as projects in the genetics field such as the human genome project."], ["What will life expectancy be in 2031?", "Life expectancy by the year 2031 could be as high as 110 years if there continue to be advancements in the medical field."]],
    max_tokens=500,
    max_rerank=20,
    stop=["<|endoftext|>"],
    n=1
  )
  return response.answers;

if __name__ == '__main__':
    print(ask(sys.argv[2], sys.argv[3])[0]);
