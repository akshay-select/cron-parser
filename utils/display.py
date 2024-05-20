

def print_table(key_value_pairs):
  max_key_length = max(len(key) for key in key_value_pairs.keys())

  print("-" * (max_key_length + 2 + sum(len(val) for val in key_value_pairs.values()) + len(key_value_pairs.keys()) - 1))

  for key, values in key_value_pairs.items():
    # print(values)
    print(f"{key:<{max_key_length}} | {' '.join(str(val) for val in values)}")

  print("-" * (max_key_length + 2 + sum(len(val) for val in key_value_pairs.values()) + len(key_value_pairs.keys()) - 1))