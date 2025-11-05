@echo off
title AI Smart City Platform
echo ===========================================
echo 🚀 Starting AI Smart City Platform...
echo ===========================================

REM --- PY1: Data Ingestion & ETL Service ---
if exist py1_data_ingestion_etl (
    start cmd /k "cd py1_data_ingestion_etl && uvicorn main:app --port 8001 --reload"
) else (
    echo ❌ Folder py1_data_ingestion_etl not found
)

REM --- PY2: Feature Engineering Service ---
if exist py2_feature_engineering (
    start cmd /k "cd py2_feature_engineering && uvicorn main:app --port 8002 --reload"
) else (
    echo ❌ Folder py2_feature_engineering not found
)

REM --- PY3: Model Serving Service ---
if exist py3_model_serving (
    start cmd /k "cd py3_model_serving && uvicorn main:app --port 8003 --reload"
) else (
    echo ❌ Folder py3_model_serving not found
)

REM --- PY4: Automation & Data Ops ---
if exist py4_automation_ops (
    start cmd /k "cd py4_automation_ops && python scheduler.py"
) else (
    echo ❌ Folder py4_automation_ops not found
)

echo ===========================================
echo ✅ All services launched successfully!
echo ===========================================
pause
