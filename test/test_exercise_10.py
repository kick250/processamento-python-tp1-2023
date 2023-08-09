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
  pass