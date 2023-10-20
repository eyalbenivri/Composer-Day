from unittest import mock
import internal_unit_testing


def test_dag_import():
    with mock.patch.dict('os.environ', AIRFLOW_VAR_GREETING="env-value", AIRFLOW_VAR_GCP_PROJECT="shtut"):
        from dags import first_dag
        internal_unit_testing.assert_has_valid_dag(first_dag)