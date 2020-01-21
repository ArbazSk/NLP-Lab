f=open("sample.txt","r")
data=f.read().replace('\n',' ')
print (data)
noise = [';',':','!','.','<p>','<h>','@','/',',']
for i in noise:
    data=data.replace(i,'')
print (data)

