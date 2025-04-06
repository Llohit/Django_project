from openai import OpenAI
import openai
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a one-sentence story about a human nature which should contain human word exactly 4 times."
)
def func(content_to_train,question):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "developer", "content": f"{content_to_train}"},
            {"role": "developer", "content": f"If you don't have any answer to question, just say...Sorry information not available"},
            {
                "role": "user",
                "content": f"{question}"
            }
        ]
    )
    return str(response.output_text)
#
# para = "My name is Raju, I am 23 years old, I stay in Mumbai, currently I am a software developer at XXY firm and I work with Django framework. I am currently working with a total of 8 months of full-time and 6 months of internship experience."
questions = ['How many years of full-time work experience does Raju have?',"What is the age of Raju?","What is raju's parent name?"]
# ans=[]
# for question in questions:
#     ans.append(func(content_to_train=para,question=question))
# print(ans)
# file_content=client.files.retrieve("file-CSP76CDjLJKfqNmX6XfznY")
# print(file_content.id)

resp=client.files.create(
  file=open("/home/epooloh/Downloads/llm_file.pdf", "rb"),
  purpose="assistants"
)
print(resp)
content = client.files.content(resp.id)
print(content)

'''

{
                "role": "user",
                "content": f"{question}"
            }
'''