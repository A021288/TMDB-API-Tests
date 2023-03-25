FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD . /
CMD [ "pytest", "tests", "--junit-xml='test_report.xml'", "-v" ]
