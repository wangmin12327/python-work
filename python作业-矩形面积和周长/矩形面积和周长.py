class Rectangle:
    @staticmethod
    def calculator_area(length,width):
        area = length * width
        return area

    @staticmethod
    def calculator_perimeter(length,width):
        perimeter = (length + width) * 2
        return perimeter

if __name__ == "__main__":

    print("请输入矩形的长和宽：")
    length = float(input())
    width = float(input())

    rectangle = Rectangle()
    rectangle_area = Rectangle.calculator_area(length,width)
    rectangle_perimeter = Rectangle.calculator_perimeter(length,width)

    print(f"矩形的面积为：{rectangle_area}")
    print(f"矩形的周长为：{rectangle_perimeter}")