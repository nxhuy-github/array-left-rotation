FROM pypy:3
WORKDIR /usr/src/app
COPY . .
ENTRYPOINT ["python", "-m", "main"]
CMD ["abcde", "3"]

