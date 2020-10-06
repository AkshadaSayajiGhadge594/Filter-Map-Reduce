print("-------DEmonstration of Filter Map Reduce---------")

#Demonstration of filter ,map,reduce using normal function:

def EvenChk(no):
	return(no%2==0);

def Increase(no):
	return no+2;

def Add(a,b):
	return a+b;

arr=[8,9,5,16,2,4,21,30,11]

evenArr=list(filter(EvenChk,arr))
print("Data after filter",evenArr);

ModArray=list(map(Increase,evenArr))
print("Data After map",ModArray);

sum=reduce(Add,ModArray)			#NameError: name 'reduce' is not defined
print("addition of even Number",sum)

## DEmonstration of filter map reduce using lambda Function:
evenArr=list(filter(lambda no:(no%2==0),arr))
print("Data after filter using lambda",evenArr);

ModArray=list(map(lambda no:no+2,evenArr))
print("Data After map using lambda",ModArray);

sum=reduce(lambda a,b:a+b,ModArray)		#NameError: name 'reduce' is not defined
print("addition of even Number using Lambda",sum)
