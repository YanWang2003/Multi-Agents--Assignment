1. 设定结点总数N，结点初始连接数2K，重连成功概率p
2. 构建网络，这个网络中的N个节点排成正多边形，每个节点都与离它最近的2K个节点相连。
3. 选择网络中的一个节点，从它开始（它自己是1号节点）将所有节点顺时针编号，再将每个节点连出的连接也按顺时针排序。
4. 然后，以如下顺序对每条边以p的概率被重连至另一点。 （并且保证不能使得两个节点之间有多于1个连接；如果这其中有连接已经有过重连的机会，就不再重复；如果重连，连到所有可能点的概率相等）


##### 说明：(1，1)表示节点1的第一条边

##### 顺序示例：

(1,1),(2,1),(3,1),...(N,1); 

(1,2),(2,2),(3,2),...(N,2);

... ; 

(1,2K),(2,2K),(3,2K),...(N,2K)