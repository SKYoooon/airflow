from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *", # 분 시 일 월 요일
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # 시작일자 
    catchup=False, # Fals = 누락된부분 안돌림 , True= 누락된 부분이 한번에 돌게됨(과부하 가능)
    # dagrun_timeout=datetime.timedelta(minutes=60), # 60분 이상 돌면 취소
    tags=["example", "example2"], # 태그끼리 모아볼수있음
    params={"example_key": "example_value"},
) as dag:

    bash_t1 = BashOperator( # task = t1
        task_id="bash_t1",
        bash_command="echo whoami", # echo = print
    )


    bash_t2 = BashOperator( 
        task_id="bash_t2",
        bash_command="echo $HOSTNAME", 
    )


    bash_t1 >> bash_t2