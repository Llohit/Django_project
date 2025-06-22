# Project Title: Financial Profile Analyzer

This Django-based project allows users to register and manage multiple financial accounts securely. A key feature is the ability to upload PDF reports containing structured financial data. The system processes the data, analyzes it using OpenAI's LLM APIs, and provides smart insights such as:

- Estimated CIBIL score
- Maximum additional loan eligibility
- Debt-to-Income (DTI) ratio
- Financial health score
- Budget optimization tips

Features

1. **User Authentication**
   - Register/login with email & password
   - JWT-based token authentication

2. **Account Management**
   - Each user can manage multiple accounts (CRUD operations)
   - Access restricted to authorized users only

3. **Financial PDF Upload**
   - Users upload a 1-page structured financial report in PDF format
   - The file includes data like loan amounts, income, EMI, credit history, etc.

4. **LLM-Driven Analysis**
   - The PDF content is parsed and converted into a structured dictionary
   - This data is passed to an OpenAI model with custom prompts
   - The model responds with human-readable insights, calculations, and remarks

5. **Secure & Scalable Architecture**
   - Django backend with modular app structure
   - Uses `pypdf` and `json` for document processing
   - LLM integration via OpenAI.
