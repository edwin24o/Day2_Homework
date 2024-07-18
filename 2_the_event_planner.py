attendees = int(input("Enter number of attendees: "))  #now need to be a int type
venue = "large hall" if attendees > 100 else "conference room" #first error on terminal was expected else instead of elif
print(venue)

vegetarian = input("Do you want vegetarian foor?: ")
if vegetarian == "yes":
    print("we recommend Veggie Delight Caterers.")
else:
    print("We recomment Gourmet Meals Caterers.")