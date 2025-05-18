from __future__ import annotations
import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_wth_op_args",
    schedule= "30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    regist_t1 = PythonOperator(
        task_id ='regist_t1',
        python_callable=regist,
        op_args = ['skyoon','male','kr','seoul']
    )

    regist_t1