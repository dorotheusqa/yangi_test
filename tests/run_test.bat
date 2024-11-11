echo off
call call ..\env_for_Yangi_Bank_Test_Task_FastAPI_Based\Scripts\activate
pytest & allure serve allure-results --port 9090
pause