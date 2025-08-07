import array as arr
array_num=arr.array("i",[5,7,10,9,1,9])
print("the original array is ",array_num)
array_num.reverse()
print("the reverse array is",array_num)
print("the frequency of 9 in my array is",array_num.count(9))