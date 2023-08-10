import exercise_10


def test_build_metric():
  data = "12/10/2023 300"
  metric = exercise_10.build_metric(data)

  assert metric.day == 12
  assert metric.month == 10
  assert metric.year == 2023
  assert metric.value == 300

def test_get_consecutive_metrics():
  metric1 = exercise_10.build_metric("09/09/1979 440")
  metric2 = exercise_10.build_metric("29/10/1979 458")
  metric3 = exercise_10.build_metric("30/10/1979 470")
  metric4 = exercise_10.build_metric("01/11/1979 480")
  metric5 = exercise_10.build_metric("02/11/1979 483")
  metrics = [
    metric1,
    metric2,
    metric3,
    metric4,
    metric5
  ]

  consecutive_metrics = exercise_10.get_consecutive_metrics(metrics)
  assert len(consecutive_metrics) == 4
  assert consecutive_metrics == [
    metric2,
    metric3,
    metric4,
    metric5
  ]


def test_calculate_spent():
  metric1 = exercise_10.build_metric("09/09/1979 440")
  metric2 = exercise_10.build_metric("29/10/1979 458")
  metric3 = exercise_10.build_metric("30/10/1979 470")
  metric4 = exercise_10.build_metric("01/11/1979 480")
  metric5 = exercise_10.build_metric("02/11/1979 483")
  metrics = [
    metric1,
    metric2,
    metric3,
    metric4,
    metric5
  ]

  consecutive_metrics = exercise_10.get_consecutive_metrics(metrics)

  spent = exercise_10.calculate_spent(consecutive_metrics)
  assert spent == 15

def test_calculate_spent_with_3_days():
  metric1 = exercise_10.build_metric("07/10/2003 500")
  metric2 = exercise_10.build_metric("08/10/2003 510")
  metric3 = exercise_10.build_metric("09/10/2003 520")
  metric4 = exercise_10.build_metric("10/10/2003 530")
  metrics = [
    metric1,
    metric2,
    metric3,
    metric4
  ]

  consecutive_metrics = exercise_10.get_consecutive_metrics(metrics)

  spent = exercise_10.calculate_spent(consecutive_metrics)
  assert spent == 30

def test_count_valid_days():
  metric1 = exercise_10.build_metric("09/09/1979 440")
  metric2 = exercise_10.build_metric("29/10/1979 458")
  metric3 = exercise_10.build_metric("30/10/1979 470")
  metric4 = exercise_10.build_metric("01/11/1979 480")
  metric5 = exercise_10.build_metric("02/11/1979 483")
  metrics = [
    metric1,
    metric2,
    metric3,
    metric4,
    metric5
  ]

  consecutive_metrics = exercise_10.get_consecutive_metrics(metrics)
  valid_days = exercise_10.count_valid_days(consecutive_metrics)
  assert valid_days == 2

def test_count_valid_days_with_3_days():
  metric1 = exercise_10.build_metric("07/10/2003 440")
  metric2 = exercise_10.build_metric("08/10/2003 458")
  metric3 = exercise_10.build_metric("09/10/2003 470")
  metric4 = exercise_10.build_metric("10/10/2003 480")
  metrics = [
    metric1,
    metric2,
    metric3,
    metric4
  ]

  consecutive_metrics = exercise_10.get_consecutive_metrics(metrics)
  valid_days = exercise_10.count_valid_days(consecutive_metrics)
  assert valid_days == 3