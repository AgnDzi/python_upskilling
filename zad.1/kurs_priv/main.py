bill = float( input("bill?"))
persons =int( input("hoe many persons?"))
tip = int(input("tip?"))
bill_per_person = (bill + tip)/persons
print(round(bill_per_person,2))