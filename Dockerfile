FROM python:3.8.3-slim

WORKDIR /

COPY ./requirements ./requirements

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r ./requirements/prod.txt
RUN pip3 install --no-cache-dir torch==1.10.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install --no-cache-dir torchvision==0.11.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY ./ ./

EXPOSE 8080

RUN ["chmod", "+x", "run_gunicorn.sh"]

CMD ["sh", "run_gunicorn.sh"]
