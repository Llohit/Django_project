import json

from ..models import Account, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pypdf import PdfReader
import re

class FinancialInfoView(APIView):
    allowed_headers = {'Personal Info':{'Account ID','User Name','Age','Gender'},
                       'Income Info': {'Gross Monthly Income','Other Income'},
                       'Loan Info': {'Personal Loan', 'Education Loan', 'Home Loan', 'Vehicle Loan', 'Other Loans'},
                       'EMI Percentage (On Annual Basis)': {'Personal loan', 'Education Loan', 'Home Loan', 'Vehicle Loan', 'Other Loan'},
                       'Expenditure (Monthly)': {'EMI', 'Average Credit Card Spend (last 3 months)','Other Monthly Average spendings'},
                       'Bank Credit Information': {'Maximum Single Credit Amount', 'Maximum Single Debit Amount'}}

    def clean_value(self,value):
        """Clean ₹ symbols, commas, and whitespace."""
        return re.sub(r'[₹,]', '', value).strip()

    def text_to_map(self,text):
        result = {}
        current_header = None

        for line in text.splitlines():
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Detect section headers like "Loan Info:"
            if line.endswith(":") and not ":" in line[:-1]:
                current_header = line[:-1].strip()
                if current_header not in self.allowed_headers:
                    raise ValueError(f"{current_header} is not a valid header, allowed headers are {self.allowed_headers.keys()}")
                result[current_header] = {}
                continue

            # Detect key-value lines like "Education Loan: ₹7,50,000"
            if ":" in line and current_header:
                key, value = line.split(":", 1)
                cleaned_key = key.strip()
                cleaned_value = self.clean_value(value)
                if cleaned_key not in self.allowed_headers[current_header]:
                    raise ValueError(f"{cleaned_key} is not a valid information for {current_header}, the info can be amongst {self.allowed_headers.get(current_header)}")
                result[current_header][cleaned_key] = cleaned_value
                continue
        return result

    def post(self,request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response("User id not passed as query parameters!", status=status.HTTP_403_FORBIDDEN)
        user_id = int(user_id)
        user_financial_info_pdf = request.FILES.get('file')
        pdf_reader = PdfReader(user_financial_info_pdf)
        user_questions = request.data.get('text')
        full_text = ""

        #Read all the contents of pdf in string
        for page in pdf_reader.pages:
            full_text += str(page.extract_text())

        #Convert the text into the dictionary mapping, so that data is structured and not random
        user_financial_info = self.text_to_map(full_text)

        #Some validation to ensure only authorized user is giving the account details
        compulsory_personal_info = self.allowed_headers['Personal Info'].copy()
        compulsory_personal_info.pop('Age')
        compulsory_personal_info.pop('Gender')
        if 'Personal Info' not in user_financial_info:
            return Response(f"Personal Info is required in the file with information {compulsory_personal_info}", status=status.HTTP_403_FORBIDDEN)
        user_personal_info = user_financial_info.pop('Personal Info')
        if not user_personal_info.get('Account ID'):
            return Response("Account ID is required in personal information section of the file", status=status.HTTP_403_FORBIDDEN)
        if not user_personal_info.get('User Name'):
            return Response("User Name is required in personal information section of the file", status=status.HTTP_403_FORBIDDEN)

        account_id_in_file = int(user_personal_info.get('Account ID'))
        try:
            account_details = Account.objects.get(account = account_id_in_file)
        except Account.DoesNotExist:
            return Response("Incorrect Account Id passed in the file", status=status.HTTP_403_FORBIDDEN)
        if account_details.user!=user_id:
            return Response("Incorrect Account Id passed in the file", status=status.HTTP_403_FORBIDDEN)
        user_details = User.objects.get(user = user_id)
        if user_details.email!=user_personal_info['User Name']:
            return Response("Incorrect User Name passed in the file", status=status.HTTP_403_FORBIDDEN)

        print(user_financial_info)

        #Convert dictionary mapping to json format, as AI will understand json format
        user_financial_info_json = json.dumps(user_financial_info,indent=2)
        return
