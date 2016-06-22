# pyTools
琐碎的python工具集，仅供娱乐

---

## ip_scaner.py

说明：扫描局域网中所有存活主机（依据ping）

用法： ```python scaner.py 192.168.172.15```

资料： TTL（生存时间值）表示ping的过程中一过经过了多少个路由器，但它的数据并不是直接给出的。其工作原理是为了防止由于路由器的设置错误，使一些数据包在两个路由器之间来回传送。因为当TTL为0的时候，数据句会丢失，这样当出现循环时候，总有一个时间会使TTL为0从而使数据包丢弃。

总结：确定存活主机，使用ping命令，以返回信息中是否存在TTL字段为判断条件（不存在TTL字段返回-1）。

---

## portscanner.py

说明：扫描某一IP的所有可用端口

用法：```python portscanner.py  192.168.172.15```

资料：在python的socket中SOCK_STREAM（TCP连接），SOCK_DGRAM（UDP连接）

总结：使用TCP连接，以是否连接超时为判断条件。
