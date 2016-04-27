#Takes input from user and applies it to story
status =("")
name = input("Name:  ")
name = str.capitalize(name)
gender = input("Male/Female:  ")
gender = str.capitalize(gender)
heOrShe = ("")

# Uses input of gender to also apply he/she to the story
if gender == "F":
    gender = "Female"
if gender == "M":
    gender = "Male"

if gender == "Female":
    heOrShe = "she"
elif gender == "Male":
    heOrShe = "he"

heOrShe = str.capitalize(heOrShe)
gender = str.lower(gender)

list = [name, gender, heOrShe]

print ("\n\n\n\n\n\n")
print ("# Character Info")
print ("Gender:     " + str.capitalize(gender))
print ("Name:       " + str.capitalize(name))
status = input("\n\nData correct? Y/N\n")
status = str.upper(status)
print ("\n\n\n\n\n\n\n\n\n")


if status == ("Y"):
    
    print ("Loading...")

    import time
    time.sleep(5)

    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    intro = ("\n\n\n# {0}'s story of alcoholic glory...\n\n\n\n\n".format(*list))
    print (intro)


    story = ("""{0} was a {1}
who really liked to sail
{2} drunk a lot of ale 
but went very pale

{2} was rushed away 
but was forced to stay
{0} went home in a week 
but was still a bit of a freak!\n\n\nThe end...\n\n\n\n\n\n\n\n\n""".format(*list))

    print (story)

else:
    print ("I am still learning to loop! Restart the application to modify character attributes!")
