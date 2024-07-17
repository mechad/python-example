import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义一个函数来产生随机数，这里是y = x + random(30-40) + 5
def generate_data(x):
    return x + np.random.uniform(30, 40, size=x.shape) + 5

# 定义一个线性函数 y = mx + b
def linear_function(x, m, b):
    return m * x + b

# 生成N个点
N = 100
x = np.arange(1, N+1)
y = generate_data(x)

# 使用curve_fit找到最佳的m和b值
params, _ = curve_fit(linear_function, x, y)

# 计算拟合直线的y值
y_fit = linear_function(x, *params)

# 绘制原始数据点和拟合的直线
plt.scatter(x, y, label='Original data', color='blue')
plt.plot(x, y_fit, 'r', label='Fitted line')
plt.legend()
plt.xlabel('X axis (Natural numbers)')
plt.ylabel('Y axis (Random number + 5)')
plt.title('Linear Regression on Random Data')
plt.show()

# 输出拟合的斜率和截距
print(f"Fitted slope (m): {params[0]}, Intercept (b): {params[1]}")
