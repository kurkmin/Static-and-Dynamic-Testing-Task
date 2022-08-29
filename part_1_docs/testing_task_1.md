### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
#class constructor is missed so there will be NameError as self is not defined 
#class constructor should start with def __init__(self):
#without class constructor, there will be missing self errors in the following methods 
  def check_for_ace(self, card):
  #Given there isn't any Card class or card variable in this task, card.value cannot exist
  #this will cause further errors below codes 
    if card.value = 1:
    #card.value should be compared with 1
    #, using == (comparison operater) not = (used for variable declaration)
      return True
    # so error in this case is cannot assign attribute error 
    else
    # colon(:) is missed, it should be after else to run the program
    # so error in this case is ':' expected error 
      return False
   

  dif highest_card(self, card1 card2):
  #Typo for dif, which should be def, so invalid syntax error in this case arises 
  #between card1 and card2, comma(,) should be added, so invalid syntax error as well 
  if card1.value > card2.value:
  #the line above and the lines below in this block should be indented
  #error in this case is expected indented error from if card1.value > card2.value: to return card2 
    return card
    #card is not defined so card1 should be returned 
  else:
  #else statement itself does not create any error, however, there should be elif statement for the case
  #when card1.value and card2.value is same
    return card2
  


def cards_total(self, cards):
#this whole block should be indented 
#without making indentation, indentation error arises in this case 
  total
  #total is referenced before it is actually assigned
  #total should be zero in this case so total = 0 
  for card in cards:
    total += card.value
    return "You have a total of" + total
    #return statement should exist outside for-loop as we are interested in the final value of total 
    #so it should be indented once in order to live in the method block 
    #another error in this case is TypeError from string concatenation with int, which is from total
    #the value inside total should be string so str(total) should replace total  
  
```
