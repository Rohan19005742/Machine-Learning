class LinearRegression:
    def __init__(self):
        self.c = None
        self.m = None
    
    def calc_line(self, x, y):
        x_mean = self.calc_mean(x)
        y_mean = self.calc_mean(y)

        numerator = self.calc_numerator(x, y, x_mean, y_mean)
        denominator = self.calc_denominator(x, x_mean)
        self.m = numerator/denominator
        self.c = y_mean - self.m * x_mean
        print(self.c)
        print(self.m)
    
    def predict_y(self, x):
        if self.c is not None and self.m is not None:
            return self.m * x + self.c
        else:
            raise Exception("Model has not been trained yet.")

    def calc_mean(self, numbers):
        total = 0
        length = len(numbers)
        for num in range(length):
            total+=numbers[num]
        return total / length

    def calc_numerator(self, x, y, x_mean, y_mean):
        total = 0
        for num in range(len(x)):
            total+= (x[num] - x_mean) * (y[num] - y_mean)
        return total

    def calc_denominator(self, x, x_mean):
        total = 0
        for num in x:
            total+= (num - x_mean) ** 2
        return total
    
X = [1, 2, 3, 4, 5]
y = [2, 3, 4, 4.5, 5.5]

# Create and train the model
model = LinearRegression()
model.calc_line(X, y)

# Make predictions
new_X = 6
prediction = model.predict_y(new_X)
print(f"Predicted value for X={new_X}: {prediction}")