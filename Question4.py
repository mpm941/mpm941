it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26} #intilializing sets
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter') #adding values to the companies set
print(it_companies)
adding_companies=["Samsung","sony","TCS"] #adding values to the companies set
it_companies.update(adding_companies)
print(it_companies)
it_companies.remove("Samsung")
print(it_companies)
#remove() will raise and error if the element to be removed doesn't exist in the set while the discard() dosen't raise any error
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
#As the function isusbset() return true A is a Subset of B)
print(A.isdisjoint(B))
#As the function isdisjoint() returns false A and B are not disjoint sets
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
A.clear() #cleared the set A
B.clear() #cleared the set B
print(A)
