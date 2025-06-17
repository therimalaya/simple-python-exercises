def prime(a):
  is_prime = 1
  num_upto_a = range(1, a + 1)
  
  for i in num_upto_a:
    if i != 1 and i != a:
      if a % i == 0:
        is_prime = 0
        break;
  
  if is_prime == 1:
    print(a, "is prime :)")
  else:
    print(a, "is not prime :(")

  
prime(123456789012345678912345678)
