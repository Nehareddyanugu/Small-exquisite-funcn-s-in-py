#input the elements in list
list=[9,8,7,6,5]
#first we will go through filter() function 
filtered_list=list(filter(lambda x:x%2==0,list))#where filtered_list is even_num list
map_list=list(map(lambda x:x*2,list))#where map_list is double times the given list
reduced_num=reduce(lambda x,y:x+y,list))#all the numbers in list gets reduced to a number 


