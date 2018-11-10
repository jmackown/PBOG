# our base image
FROM python:3-onbuild

ADD requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:outrage_display/

# run the application
CMD ["python", "app.py"]
