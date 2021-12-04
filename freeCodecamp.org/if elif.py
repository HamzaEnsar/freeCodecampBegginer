is_male= True 
is_tall =False
if is_male and is_tall :
    print('You are a tall male ')
elif not(is_male) and is_tall : 
       print('You are not a male but are tall')
elif is_male and not(is_tall):       
    print('You are a short male ')
else:
      print('You are not male and not tall')