def create_shirt(size = "G", message = "I ♡ Python"):
  print(f"Camisa tamanha {size}\nMensagem: {message}")


if __name__ == "__main__":
  create_shirt(message = "Good Morning")
  create_shirt(size = "M")
  create_shirt(size = "P", message = "Hello World")