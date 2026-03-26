#Experiment 1
new_lst=[1,2,3,4,5,4]
print(new_lst[3])
new_lst.append(23)
print(new_lst)
new_lst.remove(4)
print(new_lst)
new_lst.sort()
print(new_lst)
new_lst.sort(reverse=True)
print(new_lst)

#Experiment 2
new_set={12,345,34,1222,564,7878}
n=list(new_set)
print(n)
print(n[2])
o={56,34,436,78,90}
a=new_set.union(o)
print(a)
p=new_set.intersection(o)
print(p)
l=new_set.difference(o)
print(l)

#Experiment 3
new_tup=(12,56,76,234,678,45)
print(new_tup[1])
nested_tup=(12,34,(345,67,45))
print(nested_tup)
repeated_tup=new_tup*3
print(repeated_tup)
concatenated_tup=new_tup+nested_tup
print(concatenated_tup)

#Experiment 4
new_dict={1:'name',2:'age',3:'time'}
print(new_dict)
new_dict[2]='roll'
print(new_dict)
new_dict.pop(2)
print(new_dict)
dic={4:'class',5:'division'}
mergerd_dic=new_dict+dic
print(mergerd_dic)
