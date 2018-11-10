# our base image
FROM python:3-onbuild

ADD requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

ENV PYTHONPATH=$PYTHONPATH:outrage_scraper/

# run the application
CMD ["python", "app.py"]
