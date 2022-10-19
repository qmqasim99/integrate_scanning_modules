FROM python:3.10-slim

# Install OS-level dependencies
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes --no-install-recommends \
      curl \
      unzip

# Download and unpack the Amass zip file, saving only the binary
RUN cd /usr/local \
 && curl -LO https://github.com/OWASP/Amass/releases/download/v3.20.0/amass_linux_amd64.zip \
 && unzip amass_linux_amd64.zip \
 && mv amass_linux_amd64/amass bin \
 && rm -rf amass_linux_amd64 amass_linux_amd64.zip

# Install your application the same way you have it already
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
