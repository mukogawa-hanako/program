import random

def roll_dice():
  """サイコロを振って出た目を返す関数"""
  num = random.randint(1, 6)
  return num

def main():
  """サイコロを振るアプリのメイン関数"""
  print("サイコロを振ります...")
  result = roll_dice()
  print("出た目は", result, "です。")

if __name__ == "__main__":
  main()
