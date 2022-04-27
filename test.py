fileNew = open("sample.txt",'w')
fileRead = open("sample.txt", 'r')
fileAdd = open("sample.txt",'a')
hamlet = ["To", "be", "or", "not", "to", "be", "that", "is", "the", "question"]
for i in hamlet:
    fileAdd.write(str(i) + "\n")
    fileNew.close()
fileRead.readlines
fileNew.close()
