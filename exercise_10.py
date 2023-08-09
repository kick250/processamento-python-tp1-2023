from datetime import datetime
from metric import Metric


def remove_empty_strings(sentences):
  def not_empty(sentence):
    return len(sentence.strip()) != 0
  return tuple(filter(not_empty, sentences))

def build_metric(string_data):
  data = string_data.split(" ")
  data = remove_empty_strings(data)

  date = datetime.strptime(data[0], "%d/%m/%Y")
  value = int(data[1])
  return Metric(date, value)

def get_consecutive_metrics(metrics):
  consecutive_metrics = []
  for index, metric in enumerate(metrics):
    try:
      next_metric = metrics[index + 1]
    except IndexError:
      next_metric = None

    if next_metric != None and metric.is_next_day(next_metric.date):
      next_metric.has_day_before = True
      consecutive_metrics.append(metric)
    elif metric.has_day_before:
      consecutive_metrics.append(metric)

  return consecutive_metrics


def calculate_spent(consecutive_metrics):
  pass

def main():
  input_quantity = int(input("Diga o nº de medições: "))
  metrics = []
  for i in range(input_quantity):
    data = input(f"Diga a medição {i} (dd/mm/aaaa valor): ")
    metrics.append(
      build_metric(data)
    )

  consecutive_metrics = get_consecutive_metrics(metrics)
  spent_values = calculate_spent(consecutive_metrics)

  print(f"{len(spent_values)} dia(s)\n{sum(spent_values)} KWh")


if __name__ == "__main__":
  main()