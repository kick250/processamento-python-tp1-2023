from datetime import timedelta


class Metric:
  def __init__(self, date, value):
    self.__date = date
    self.__value = value
    self.has_day_before = False

  @property
  def day(self):
    return self.__date.day

  @property
  def month(self):
    return self.__date.month

  @property
  def year(self):
    return self.__date.year

  @property
  def date(self):
    return self.__date

  @property
  def value(self):
    return self.__value

  def is_next_day(self, date):
    tomorrow = self.__date + timedelta(days=1)

    if tomorrow.day != date.day: return False
    if tomorrow.month != date.month: return False
    if tomorrow.year != date.year: return False
    return True