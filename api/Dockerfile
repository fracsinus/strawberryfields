FROM python:3.12-alpine

ARG VERSION=0.1.0
ARG WHEEL=strawberryfields_api-${VERSION}-py3-none-any.whl

COPY requirements.txt /opt/
RUN pip install -r /opt/requirements.txt

COPY dist/${WHEEL} /opt/
RUN pip install /opt/${WHEEL}

COPY run.py /opt/

CMD ["fastapi", "run", "/opt/run.py", "--port", "80"]
