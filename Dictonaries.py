"""
file_counts = {"A":10, "B":20, "C":30, "D":40}
print(file_counts)  #prints list
print(file_counts["A"])  # print value with the key
print("A" in file_counts) #check key in dictonary
file_counts["A"] = 8  # changing integer value with key
print(file_counts)
del file_counts["A"] #deleting A
print(file_counts)
####################
#interating through dictonaries
file_counts = {"A":10, "B":20, "C":30, "D":40}
for element in file_counts:
    print(element)  #this will print only key

for ext, amt in file_counts.items():
    print("{},{}".format(amt,ext))  # print key with value formatted

for value in file_counts.values():
    print(value)        # prints values in a dict

print(file_counts.keys())  # print keys in dict 
print(file_counts.values()) # print values in dict
####################
# counting letters in a string and storing in a dictonary
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaaaaaa"))
print(count_letters("Hi my name is Jatin Ahuja"))
print(count_letters("   "))
print(count_letters(" "))


###################
# sum of keys and print
def server_time(server):
    total_time = 0
    for value,key in server.items():
        total_time+=server[value]

    return round(total_time,2)

file_system = {"U1":1.1,"U2":2.3,"U3":9.9,"U4":8.8}
print(server_time(file_system))
##################
# print first name and last name together from a give dictionary
list = []
def list_fullname(Full_names):
    for lastname,firstname in Full_names.items():
        for name in firstname:
            list.append(name + " " +lastname)
    print(list)

   

Full_names = {"Ali":["mhd","amir","malik"], "Devi":["ram","amaira"], "chen":["feng","li"]}
list_fullname(Full_names)


"""
##########################
# inverting dictionary

def IT_func(it_items):
    new_items = {}
    for key,value in it_items.items():
        for x in value:
            if x in new_items:
                new_items[x].append(key)
            else:
                new_items[x] = [key]
    return(new_items)
print(IT_func({"Hard Drives":["IDE HDDs","SCSI HDDs"], 
 "PC Parts":["IDE HDDs","SCSI HDDs", "High-end video cards", "Basic video cards"],
 "Video cards":["High-end video cards", "Basic video cards"]}))

