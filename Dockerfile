FROM python:3.11

WORKDIR /CarBrandClass1

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# COPY folder หรือ file งาน
COPY ./requirements.txt /CarBrandClass1/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /CarBrandClass1/requirements.txt

COPY ./app /CarBrandClass1/app

ENV PYTHONPATH "${PYTHONPATH}:/carbrandclass1"

# ต้องการใช้ poth 80 สำหรับให้ Containers สื่อสารกันเองใน Docker
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]