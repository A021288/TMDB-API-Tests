# FROM public.ecr.aws/lambda/python:3.10

# RUN yum -y install tzdata
# # Install dependencies first so they cache and we can update app code without a full rebuild
# COPY requirements.txt requirements.txt
# RUN python3.10 -m pip install -U pip
# RUN python3.10 -m pip install -r requirements.txt

# COPY . .
FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD main.py /
CMD [ "python", "./main.py" ]