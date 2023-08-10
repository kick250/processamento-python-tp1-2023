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
  consecutive_spents_index = -1
  consecutive_spents = []

  for metric in consecutive_metrics:
    if metric.has_day_before:
      consecutive_spents[consecutive_spents_index].append(metric.value * -1)
    else:
      consecutive_spents_index += 1
      consecutive_spents.append([metric.value])

  spents = [sum(spents_consecutive) for spents_consecutive in consecutive_spents]

  return sum(spents) * -1

def count_valid_days(consecutive_metrics):
  quantity = 0

  for metric in consecutive_metrics:
    if metric.has_day_before: quantity += 1

  return quantity

def main():
  input_quantity = int(input("Diga o nº de medições: "))
  metrics = []
  for i in range(input_quantity):
    data = input(f"Diga a medição {i} (dd/mm/aaaa valor): ")
    metrics.append(
      build_metric(data)
    )

  consecutive_metrics = get_consecutive_metrics(metrics)
  spent = calculate_spent(consecutive_metrics)
  valid_days = count_valid_days(consecutive_metrics)

  print(f"{valid_days} dia(s)\n{spent} KWh")


if __name__ == "__main__":
  main()