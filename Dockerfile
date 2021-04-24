FROM python:3.8
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt -f  https://download.pytorch.org/whl/torch_stable.html
RUN python3 download.py
CMD python3 main.py
