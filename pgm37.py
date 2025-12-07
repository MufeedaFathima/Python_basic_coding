lst = [1,2,3,2,4,3]
for i in set(lst):
    if lst.count(i)>1:
        print(i)



nums = [1,2,3,2,4,3]
seen = set()
dupes = set()
for num in nums:
    if num in seen:
        dupes.add(num)
    else:
        seen.add(num)
print(list(dupes))
