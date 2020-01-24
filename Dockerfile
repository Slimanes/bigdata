FROM ubuntu
RUN mkdir ./work
RUN apt update
ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt install sudo -y
RUN apt install python3 -y && apt install python3-pip -y
RUN apt install python3-venv -y
RUN apt install jupyter-notebook -y 
RUN apt install git -y
WORKDIR ./work
RUN python3 -m venv bigdata
CMD ["sh", "-c" , "jupyter notebook --no-browser --port=8000 --ip='0.0.0.0' --allow-root"]
COPY . ./bigdata
EXPOSE 8000

