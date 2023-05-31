import math

class line:
    """
    선의 길이와 관련된 class는 line임
    외부에서는 접근 불가능한 __width 와 __height 를 설정함
    해당 변수를 수정하기 위해
    set_length 와 get_length 를 제공함
    """
    __width = 0
    __height = 0


    def __init__(self, width, height):
        """
        초기의 width값과 height값을 받음
        witdh -> 초기 선의 가로 길이 
        height -> 초기 선의 세로 길이
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """
        선의 길이 설정
        width -> 수정할 가로의 길이
        height -> 수정할 세로의 길이
        """
        self.__width = width
        self.__height = height

    def get_length(self):
        """
        객체가 저장하고 있는 선의 길이 반환
        리턴값: 저장된 선의 길이
        """
        return self.__width, self.__height

def area_rectangle(width, height):
    """
    길이를 입력 받아서 직사각형의 넓이를 구하는 함수
    인자: width-> 가로의 길이, height -> 세로의 길이
    리턴값: 작사각형의 넓이
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height

def area_ellipse(width, height):
    """
    길이를 입력 받아서 타원의 넓이를 구하는 함수
    인자: width -> 짧은쪽 반지름의 길이, height -> 긴쪽 반지름의 길이
    리턴값: 타원의 넓이
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi

def area_right_triangle(width, height):
    """
    길이를 입력 받아서 정삼각형의 넓이를 구하는 함수
    인자: width -> 밑 변의 길이, height -> 높이의 길이
    리턴값: 직각삼각형의 넓이
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2