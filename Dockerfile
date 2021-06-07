FROM tensorflow/tensorflow:2.5.0-gpu-jupyter

COPY . /app

EXPOSE 8888

CMD ["jupyter", "notebook", "--notebook-dir=/app", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]