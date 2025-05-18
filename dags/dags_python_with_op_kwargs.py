from __future__ import annotations
import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_wth_op_kwargs",
    schedule= "30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    regist_t2 = PythonOperator(
        task_id ='regist_t2',
        python_callable= regist2,
        op_args = ['skyoon','male','kr','seoul'],
        op_kwargs={'email':'skyoon7899@gmail.com','phone' :'010'}
    )

    regist_t2