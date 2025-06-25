list1=[11, 45, 8, 23, 14, 12, 78, 45, 89]

lenght=len(list1)
chunk=int(lenght/3)
start=0
end=chunk

for i in range(3):
    indexes = slice(start, end)
    #print("index",indexes)
    list_chunk = list1[indexes]
    print("Chunk ", i, list_chunk)
     
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk