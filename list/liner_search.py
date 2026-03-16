class Liner_Search:
    def liner_search(list,k):
        for i in range(0,len(list)):
            if list[i]==k:
                return i
        print("not found")


list=[3,4,5,6,7,8]
k=6
ob=Liner_Search
print(ob.liner_search(list,k))

    