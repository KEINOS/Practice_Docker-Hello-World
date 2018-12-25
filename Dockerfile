FROM python:3.6.5

COPY src/hello-world.py /usr/local/sbin/hello-world

ENTRYPOINT ["/usr/local/sbin/hello-world"]

CMD ["--help"]
