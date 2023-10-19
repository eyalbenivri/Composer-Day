import internal_unit_testing


def test_dag_import():
    from dags import first_dag

    internal_unit_testing.assert_has_valid_dag(first_dag)