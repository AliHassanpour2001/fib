def fib(n) :
  l = [1,1]
  if n==1 or n==2 :
    return n
  else :
    for i in range(n-2) :
      l.append(l[-1]+l[-2])
    return l[-1]
    
def main() :
  n = int(input("what you want fibonaci's number? "))
  print(fib(n))


if __name__ == "__main__" :
  main()
