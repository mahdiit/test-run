FROM debian:bookworm-slim

COPY install.sh /app/install.sh
COPY start-xray.sh /usr/local/bin/start-xray.sh
COPY start-admin.sh /usr/local/bin/start-admin.sh
COPY admin-server.py /usr/local/bin/admin-server.py

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash git curl wget unzip tzdata openssl ca-certificates python3 \
    && rm -rf /var/lib/apt/lists/*

RUN chmod +x /app/install.sh && /app/install.sh
RUN chmod +x /usr/local/bin/start-xray.sh /usr/local/bin/start-admin.sh /usr/local/bin/admin-server.py
COPY config.json /etc/config.json
COPY admin /opt/mrh-admin

CMD ["/bin/sh", "-lc", "/usr/local/bin/start-xray.sh && tail -f /tmp/xray.log"]
