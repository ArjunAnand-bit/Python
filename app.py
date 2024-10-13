b = " Hello, World! "
print(b[:11])# type: ignore
print(b.upper())# type: ignore
print(b.lower())# type: ignore
print(b.strip()) # type: ignore
print(b.replace("H","Y"))# type: ignore
print(b.split(","))# type: ignore



#We can try using '''

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

for x in "Banana":
 print(x) # type: ignore

print(len(b)) # type: ignore

txt = "The best things in life are free!"
print("free" in txt) # type: ignore


txt2 = "The best things in life are free!"
print("expensive" not in txt) # type: ignore

a = "hi"
print(a) # type: ignore

c,d = (1,6)
print(c+d) # type: ignore





















































































a = "Hello"
b = "World"

print(a+",Mellow"+" "+b)# type: ignore