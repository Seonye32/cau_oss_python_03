"""
figure 모듈을 통해 도형들과 관련된 함수, 클래스를 제공함
line 을 통해 선의 길이를 설정하고 수정함
area 와 관련된 함수들로 도형들의 넓이를 구함
"""


import math

class line:
    """
    선의 길이와 관련된 class는 line임
    외부에서는 접근 불가능한 __length 을 설정함
    해당 변수를 수정하기 위해
    set_length 와 get_length 를 제공함
    """
    __length = 0
    __height = 0

    def __init__(self, length, height):
        """
        초기의 length값과 height값을 받음
        length -> 초기 선의 가로 길이 
        height -> 초기 선의 세로 길이
        """
        self.__length = length
        self.__height = height


    def set_length(self, length):
        """
        선의 길이 설정
        length -> 수정할 선의 길이
        """
        self.__length = length

    def get_length(self):
        """
        객체가 저장하고 있는 선의 길이 반환
        리턴값: 저장된 선의 길이
        """
        return self.__length

def area_square(length):
    """
    길이를 입력 받아서 정사각형의 넓이를 구하는 함수
    인자: length-> 한 변의 길이
    리턴값: 정사각형의 넓이
    """
    return length * length

def area_circle(length):
    """
    길이를 입력 받아서 원의 넓이를 구하는 함수
    인자: length -> 반지름의 길이
    리턴값: 원의 넓이
    """
    return length * length * math.pi

def area_regular_triangle(length):
    """
    길이를 입력 받아서 정삼각형의 넓이를 구하는 함수
    인자: length -> 한 변의 길이
    리턴값: 정삼각형의 넓이
    """
    return length * length * math.sqrt(3) / 4