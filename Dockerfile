FROM python:3.12-rc-alpine3.17




WORKDIR . /Ai_software_stability_backend_code/Ai_software_stability_backend_code




COPY . .




COPY requirements.txt .




RUN pip install -r requirements.txt




CMD ["python","api.py","Models_test.py","Models.py","BertApi.py","Resample_test.py","run","--host=0.0.0.0",]