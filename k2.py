import numpy as np
import matplotlib.pyplot as plt

def k_means(data, k, max_iterations=100):
    # 随机选择初始质心
    centroids = data[np.random.choice(data.shape[0], size=k, replace=False)]
    
    for _ in range(max_iterations):
        # 分配每个点到最近的质心
        labels = np.argmin(np.linalg.norm(data[:, np.newaxis] - centroids, axis=2), axis=1)
        
        # 更新质心
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # 如果质心没有变化，则停止迭代
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids
    
    return labels, centroids

# 生成模拟数据
np.random.seed(0)
points = np.concatenate((np.random.normal(loc=[0, 0], scale=1, size=(100, 2)),
                         np.random.normal(loc=[5, 5], scale=1, size=(100, 2))))

# 运行K均值聚类
k = 2
labels, centroids = k_means(points, k)

# 可视化结果
plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='r', zorder=10)
plt.title('K-Means Clustering')
plt.show()
