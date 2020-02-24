From python:3.7
COPY ./python_task.py ./
RUN pip install datetime
CMD [ "python", "./python_task.py" ]
