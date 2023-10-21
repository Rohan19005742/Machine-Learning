
class QuadraticRegression:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
    def calc_line(self, x, y):
        numbers=len(x)
        x_2 = list(map(lambda number:number**2, x))
        x_3 = list(map(lambda number:number**3, x))
        x_4 = list(map(lambda number:number**4, x))
        sum_of_x = sum(x)
        sum_of_y = sum(y)
        sum_of_x_2 = sum(x_2)
        sum_of_x_3 = sum(x_3)
        sum_of_x_4 = sum(x_4)
        sum_of_x_2_y = self.calc_sum_of_x_2_y(x_2, y)



    def calc_sum_of_x_2_y(self, x_2, y):
        total = 0
        for num in range(len(y)):
            total += x_2[num] * y[num]
        return total 


    
    