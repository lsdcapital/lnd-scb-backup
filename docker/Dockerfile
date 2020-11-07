FROM python:3.8-slim-buster

LABEL maintainer="LSDopen - Stefan Lesicnik (stefan@lsdopen.io)"

ENV LND_SCB_BACKUP_VERSION "v0.3-alpha"

ENV LND_SCB_BACKUP_ARCHIVE "${LND_SCB_BACKUP_VERSION}.tar.gz"
ENV LND_SCB_BACKUP_URL "https://github.com/lsdopen/lnd-scb-backup/archive/${LND_SCB_BACKUP_ARCHIVE}"

WORKDIR /app

RUN apt-get update && \
  apt-get install -y --no-install-recommends wget

# Download / Check / Install
RUN cd /tmp \
    # Get LND-SCB-BACKUP
    && wget -qO ${LND_SCB_BACKUP_ARCHIVE} "${LND_SCB_BACKUP_URL}" \
    # Install
    && tar -xzvf ${LND_SCB_BACKUP_ARCHIVE} -C /app --strip-components=1 \
    # Cleanup downloaded archive
    && rm -rf /tmp/${LND_SCB_BACKUP_ARCHIVE}

RUN pip install pipenv && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pipenv install --deploy --system && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

RUN apt-get install -y --no-install-recommends git curl && \
  /app/compile_proto.sh && \
  apt-get remove -y git && \
  apt-get autoremove -y

CMD ["python", "lnd-scb-backup.py"]
