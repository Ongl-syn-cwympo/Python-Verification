# Data Verification ~ verification (is it correct?)

Once we know our data is valid (i.e. it is logical, and in the right format, etc.) then we also need to check if it is correct 
(it maybe a valid date-of-birth, but is it your date-of-birth?!)

# Types of verification

- Proof-reading - the person entering the data simply reads through what they have entered to check it is correct

- Double-entry - the data is entered twice, either by the same, or another operator. The computer compares the data, and any that doesn’t match is questioned.

# Why do we have to have/use a verification type

The purpose of data verification is to ensure that data that are gathered are as accurate as possible, and to minimize human and instrument errors 
including those which arise during data processing.


# Double-entry data & the explination on why it can be tricky

In general the whole "equal" question can be a bit tricky. Though if you're comparing more complicated things, like your own data structure you'll have to sit
down and think "what does it mean for these two things to be equal?". For instance suppose you have a data structure that is the representation of a person in a
DB table or in a CSV or something and it looks like this Person(id, last_name, first_name, created_at) for two persons to be equal, do all fields have to be
equal? do we only compare last_name and first_name or maybe also id? This isn't some "trick question" there isn't really a correct answer. You'll have to be
cognizant of how other things use the equality you define. I don't know python well but in Java if you define a custom equality you'll have to be careful
because e.g. HashMap will use it under the hood. 

finally, please make my inner mathematician happy and make sure your equality is sane. I.e. it's symmetric (a == a  ... lol JS console.log(NaN == NaN) outputs
false), commutative (a == b implies that b == a) and transitive (a == b && b == c implies a == c) you want these things to hold that all the intuitive reasoning
you do with equality is actually sound. 

If you want to compare more complicated data structures, considering that python is an untyped language you might want to google for "deep equals" which is the common term for "traverse data structure and compare element wise".
