# Mentora – The Mentor Agent  

Mentora helps you master any subject in a fun and interactive way.  
Simply choose a topic, and Mentora will generate:  

1. A structured course summary.  
2. Detailed lessons for each chapter and unit.  
3. Engaging games after each lesson, such as quizzes, fill-in-the-blanks, and more.  

## **Installation**  

First, create the `.env` file at the root of the project, and fill the vars
```dotenv
AZURE_API_KEY=
AZURE_ENDPOINT=
AZURE_API_VERSION=
AZURE_MODEL_ID=
```

Run the following commands to build and start the application

```shell
docker-compose up --build
```
Then, open a shell inside the web container:
```shell
docker-compose attach partoo-repo-mini-env-web-1
```