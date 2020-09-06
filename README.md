# 使用说明

## 文件说明：

- mv2mc.py 将MagicaVoxel的ply转换成mvcd文件
- mvcd2mcf.py将mvcd翻译为《我的世界》的函数文件(单色，用户可选方块)
- mvcd2cmcf.py将mvcd翻译为《我的世界》的函数文件(自动识别颜色)
- color.py是调色盘，可以复制其中记录的颜色信息到mvcd2cmcf.py中，就会变为自动识别的一部分。

## 简单用法：

1.MagicaVoxel导出ply文件。

2.使用 python mv2mc.py 文件名 输出文件名(可以不写) 生成mvcd文件

3.使用mvcd2mcf.py/mvcd2cmcf.py可以生成对应的*.mcfunction文件

4.在《我的世界》中

​	输入 /reload

​	输入 /function 命名空间:函数名

​	等待执行完毕

## MVCD文件：

MVCD文件是一种将MagicaVoxel编辑的模型记录为一个一个方块在三维空间中位置的文件。

第一行为文件头：

MagicVoxCubePositionData

第二行为文件版本：

v1.0

第三行为方块数量：

40

以下为方块的 x z y r g b信息。(注意轴顺序！)。

## Float版本：

针对一些模型会在编译成MVCD时出现错误，所以制作了Float版本，稳定性稍低。但是暂时可以应对普通版的部分错误。

## Int版本：

上古版本。只能处理包含整数数据的文件。有浮点就会报错，但是对于整数数据文件准确率更高。
