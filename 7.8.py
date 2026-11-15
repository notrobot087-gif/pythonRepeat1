a=str(input("Extension of file:    "))
dot_i  =  a.rfind('.')
name=a[:dot_i]
extension=a[dot_i+1:]
print(name)
print(extension)