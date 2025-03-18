class Cell:
    def __init__(self, color, shape, background):
        self.color = color
        self.shape = shape
        self.background = background

    def __str__(self):
        return f"{self.color}::{self.shape}::{self.background}"

def main():
    p1 = Cell("Red", "Square", "Gray")
    print(p1)

if __name__=="__main__":
    main()