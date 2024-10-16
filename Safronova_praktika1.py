class Image:
    def __init__(self, title):
        self.title = title 
        self.resolution = "1200x400"
        self.extension = ".png"

    def resize(self, a, b):
        if a>0 and b>0:
            self.resolution = f"{a}x{b}"
        else:
            print("Значения разрешения должны быть положительными")

pict1 = Image("First picture")
pict2 = Image("Second picture")
print(dir(pict1))

pict1.resize(800, 400)
print(pict1.resolution)

pict2.resize(-800, 400)
print(pict2.resolution)

print(pict1.title)
print(pict1.extension)