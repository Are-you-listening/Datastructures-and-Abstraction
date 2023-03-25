import ADT.MyCircularLinkedChainKars

slots = ADT.MyCircularLinkedChainKars.LCTable()  # Bijhouden van tijdslots

# Slots beginnen op index 1
slots.tableInsert(1, 14 * 3600 + 30 * 60)
#print(slots.tableRetrieve(1))# 14:30.
slots.tableInsert(2, 17 * 3600)  # 17:00
slots.tableInsert(3, 20 * 3600)  # 20:00
slots.tableInsert(4, 22 * 3600 + 30 * 60)  # 22:30 #Initaliseert de huidige slots

print(slots.tableRetrieve(1))
print(slots.tableRetrieve(2))
print(slots.tableRetrieve(3))
print(slots.tableRetrieve(4))
print(slots.save())