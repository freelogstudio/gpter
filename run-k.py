import sys
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY");
answer = openai.Answer()


def read_file(p):
    with open(p) as f:
        return f.read()
import json

k = json.loads(read_file('./k.json'))['text'];
kex = read_file('./k-ex.txt');



def create_question(q):
    return q;


def ask(question, temperature=0.99):
  response = answer.create(  
    search_model='davinci',
    model='davinci',
    question=create_question(question),
    temperature=float(temperature),
    documents=[k],
    examples_context=kex,
    examples=[["What are some things kylie tried to make flex believe?", "She tried to make him believe that she was the person flex was trying to contact when he messaged her, and that she was kyle"], ["What is the age of kylie", "25, but she acts significantly younger."], ["What are some issues that kylie deals with?", "Depression, chronic boredom, and immaturity."]],
    max_tokens=500,
    max_rerank=20,
    stop=["<|endoftext|>"],
    n=5
  )
  return response.answers;

if __name__ == '__main__':
  answers = ask(sys.argv[1], sys.argv[2]);
  for x in answers:
      print(x)
