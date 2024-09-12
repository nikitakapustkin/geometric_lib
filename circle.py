import math

def area(r):
    '''
    Возращает площадь круга

    Параметры :
        r (int) : радиус круга

    Возращаемое значение :
        area (float) : площадь круга с радиусом r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возращает периметр круга

    Параметры :
        r (int) : радиус круга

    Возвращаемое значение :
        perimeter (float) : периметр круга с радиусом r
    '''
    return 2 * math.pi * r

