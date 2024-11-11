@echo off
echo Starting FastAPI application...

REM Активируем виртуальное окружение, если оно есть
REM Если вы используете виртуальное окружение, замените путь ниже на соответствующий путь
call ..\env_for_Yangi_Bank_Test_Task_FastAPI_Based\Scripts\activate

echo Virtual environment activated...

REM Запускаем uvicorn с нужными параметрами
uvicorn server:app --reload

pause

REM Деактивируем виртуальное окружение после завершения
REM Эта строка нужна только если вы активировали виртуальное окружение выше
deactivate