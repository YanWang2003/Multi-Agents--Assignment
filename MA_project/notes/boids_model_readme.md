### $\Rightarrow$ 初始状态建立

1. **通过输入**设定鸟群数量与更新次数

##### 自动设定以下参数：

1. 鸟群初始位置（2维）
2. 鸟群初始速度（2维，并且速度大小相同）
3. 鸟群速度大小 
4. 向心速度，离心速度与平行速度的权重 
5. 向心速度，离心速度与平行速度的探测边界

### $\Rightarrow$ 状态更新

1. 计算距离矩阵
  
2. 计算当前时刻每一只鸟的向心速度，离心速度与平行速度，乘其权重并相加得到规则速度（当前时刻某一只鸟平行速度=前一时刻所有鸟速度的平均值，当前时刻某一只鸟向心速度=前一时刻某一范围内鸟质心位置-某一只鸟位置）

3. 更新当前时刻每一只鸟速度为前一时刻速度+规则速度归一化

4. 更新当前时刻每一只鸟位置为前一时刻位置+当前速度
  

  

  
