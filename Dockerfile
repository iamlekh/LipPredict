FROM python:3.8
RUN mkdir /project
WORKDIR /project
COPY . /project
VOLUME /project
RUN pip install -r requirements.txt
EXPOSE 8888
#CMD ["bash"]
# RUN pip install jupyter
# EXPOSE 8888
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
