def add_digits(num):
  sum_sq = 0
  for i in str(num):
    sum_sq = sum_sq + int(i)**2
    
  return(sum_sq)


def magic_run(num):
  step = 0
  out = [num]
  while num not in [1, 145]:
    num = add_digits(num)
    step = step + 1
    out.append(num)

  print(f"After {step} step it reaches to {num}")
  print(f"The numbers during this transition is {out}")


magic_run(42)
