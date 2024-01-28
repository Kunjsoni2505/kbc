que=[["National bird of india:","owl", "vulture", "peacock","hello", 3 ],
   ["Which planet in our solar system is known as the Red Planet?", "jupiter","mars","earth", "venus",2],
   ["What is the name of the biggest planet in our solar system?","jupiter","mars","earth", "venus",1],
    ["Which planet in our solar system is known as the Blue Planet?","jupiter","mars","earth", "venus",3],
   ["What is the hottest planet in the solar system?","jupiter","mars","earth", "venus",4],
   ["What is the capital of Australia?","Sydney", "Melbourne", "Canberra","Perth", 3 ],
   ["Who painted the Mona Lisa?", "Vincent van Gogh","Leonardo da Vinci","Pablo Picasso", "Michelangelo",2],
   ["What is the largest ocean in the world?","Pacific Ocean","Arctic Ocean","Indian Ocean", "Atlantic Ocean",1],
    ["Which country is home to the famous ancient monument Stonehenge?","France","Italy","United Kingdom", "Egypt",3],
   ["Which country is known as the 'Land of the Rising Sun'?","China","South Korea","Thailand", "Japan",4]]
lev=[1000,2000,3000,4000,5000,7000,10000, 12500,15000, 20000]
m=0
digit=0
for i in range(0, len(que)):
   ques=que[i]
   print(f"\n\nQuestions no. {i+1} for rs {lev[i]}")
   print(f"{ques[0]}")
   print(f"1.{ques[1]}                2.{ques[2]} ")
   print(f"3.{ques[3]}                4.{ques[4]}")

   ans=int(input("Enter your choice(1-4) or 0 for quit or for lifeline(50-50) enter 5:\n"))
   print("NOTE: you can use lifeline only one time. if you use lifeline for more than one time then the game is over.")

   if ans==5 and digit==0:
      digit+=1
      if i==0:
         print(f"3.{ques[3]}                4.{ques[4]}")
      elif i==1:
         print(f"1.{ques[1]}                2.{ques[2]} ")
      elif i==2:
         print(f"1.{ques[1]}                2.{ques[2]} ")
      elif i==3:
         print(f"3.{ques[3]}                4.{ques[4]}")
      elif i==4:
         print(f"3.{ques[3]}                4.{ques[4]}")
      elif i==5:
         print(f"3.{ques[3]}                4.{ques[4]}")
      elif i==6:
         print(f"1.{ques[1]}                2.{ques[2]} ")
      elif i==7:
         print(f"1.{ques[1]}                2.{ques[2]} ")
      elif i==8:
         print(f"3.{ques[3]}                4.{ques[4]}")
      elif i==9:
         print(f"3.{ques[3]}                4.{ques[4]}")

      ans1=int(input("Enter your choice(1-4):"))
      if ans1==ques[-1]:
         print(f"correct..., you won rs {lev[i]}")

   elif(ans==ques[-1]):
      print(f"correct..., you won rs {lev[i]}")

      if(i==4):
         m=5000
         print("if you want to continue enter 1 and if you want to exit please enter 0")
         choice=int(input(":"))
         if(choice==0):
            break
         if choice==1:
            continue
      elif(i==7):
         m=10000
         print("if you want to continue enter 1 and if you want to exit please enter 0")
         choice = int(input(":"))
         if (choice == 0):
            break
         if choice == 1:
            continue
      elif(i==9):
         m=20000
   elif ans==5 and digit>=1:
      print(" Sorry out of chance.....")
      break
   else:
      print("wrong ans....")
      break


   if(ans==0):
      break

print(f"total won ammount:{m}")
