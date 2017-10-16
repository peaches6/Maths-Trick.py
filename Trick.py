ready = input("This is a math trick. Are you ready? Y/N ")
if ready == "Y":
  print("Ok. You will now begin the trick. Once you have each step worked out, type Ok.")
  a = input("Think of a number between 1 and 10. ").lower()

else:
  print("Well, go away then.")
  
if a == "Ok":
  print("Next step")
  b = input("Multiply that number by 2. ").lower()
  
if b == "ok":
  step1 = a * 2
  print("Next step")
  c = input("Now, times that new number by 5. ").lower()
  
if c == "ok":
  step2 = step1 * 5
  print("Next step")
  d = input("Divide that new number by your original number. ").lower()
  
if d == "ok":
  step3 = step2 / a
  print("Final step")
  e = input("Subtract 7 from that number. ").lower()
  
if e == "ok":
  print("Well done! Now I will guess your final answer.")
  step4 = step3 - 7
  f = input("Is your answer 3? Y/N ").lower()
  
if f == "Y":
  print("Yay, I guessed your number!")
  
else:
  print("Well you must of messed up the calculations somewhere. Redo this with the same number.")
