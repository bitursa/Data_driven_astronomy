# Write your hms2dec and dms2dec functions here
def hms2dec(h,m,s):
   return (15*(h + m/60 + s/(60*60)))

def dms2dec(d,m,s):
   if d>0:
      dec = (d + m/60 + s/(60*60))
   else:
      dec = (-1*(-d + m/60 + s/(60*60)))
   return dec



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(0,10,35.92))

  # The second example from the question
  print(dms2dec(-47,36,19.1))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))