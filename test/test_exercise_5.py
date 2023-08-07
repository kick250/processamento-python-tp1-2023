from exercise_5 import city_and_country


def test_city_and_country():
  result = city_and_country("Moscou", "Russia")
  assert result == "Moscou, Russia"