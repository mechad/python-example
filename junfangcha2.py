import numpy as np
import matplotlib.pyplot as plt

# 定义一个函数来产生随机数，这里是y = x + random(30-40) + 5
def generate_data(x):
    noise = np.random.normal(scale=2, size=N)  # 添加一些噪声
    return x + np.random.uniform(30, 40, size=x.shape) + noise

# 定义一个线性函数 y = mx + b
def linear_function(x, m, b):
    return m * x + b

# 生成N个点
N = 100
x_values = np.arange(1, N+1)
y_values = generate_data(x_values)

# 将数据点添加到图表
plt.scatter(x_values, y_values, color='blue', label='Data points')

# 最小二乘法拟合直线
# 计算斜率(slope)和截距(intercept)
n = len(x_values)
x_mean = np.mean(x_values)
y_mean = np.mean(y_values)
xy_sum = np.sum(x_values * y_values)
x_sum = np.sum(x_values)
y_sum = np.sum(y_values)
xx_sum = np.sum(x_values ** 2)

slope = (n * xy_sum - x_sum * y_sum) / (n * xx_sum - x_sum ** 2)
# intercept = (y_sum - x_sum * slope) / n
# 下面的公式等价上面的
intercept = y_mean - slope * x_mean

# 计算均方误差
y_pred = slope * x_values + intercept
mse = np.mean((y_pred - y_values) ** 2)
print(f"The Mean Squared Error is: {mse}")

# 绘制拟合的直线
plt.plot(x_values, y_pred, 'r', label=f'Fitted line (slope={slope:.2f}, intercept={intercept:.2f})')

# 添加图表标题和轴标签
plt.title('Linear Regression Fit')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图例
plt.legend()

# 显示图表
plt.show()
