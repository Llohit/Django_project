from rest_framework.views import APIView
from pypdf import PdfReader
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
import json
client = OpenAI()

class FileUploadView(APIView):
    def ask_ai(self,content_to_train, question):
        # print(question, content_to_train)
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "developer", "content": f"{content_to_train}"},
                {"role": "developer",
                 "content": f"If you don't have any answer to question, just say...Information not available"},
                {"role": "developer",
                 "content": f"Instruction: The content which is shared is one persons information referred as candidate."},
                {
                    "role": "user",
                    "content": f"{question}"
                }
            ]
        )
        return str(response.output_text)
    def post(self,request):
        pdf_file = request.data.get('file')
        pdf_reader = PdfReader(pdf_file)
        questions = request.data.get('text')
        questions = json.loads(questions)
        st = ""
        for page in pdf_reader.pages:
            st += str(page.extract_text())
        ans=[]
        for question in questions:
            ans.append(self.ask_ai(content_to_train=st,question=question))
        return_ans = {}
        for question in questions:
            return_ans[question] = ans.pop(0)
        return Response(return_ans, status=status.HTTP_201_CREATED)
