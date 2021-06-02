import color
import matplotlib as mpl

#设置自定义color与量程
colorbar = input('请选择颜色：1.nmc，2.bd，3.color，4.wv，5.ssdwv，6.bw。（不选择回车默认黑白色阶）')
if colorbar == '1':
    ys = color.nmc
elif colorbar == '2':
    ys = color.irbd
elif colorbar == '3':
    ys = color.ircolor
elif colorbar == '4':
    ys = color.wv
elif colorbar == '5':
    ys = color.ssdwv
else:
    ys = color.irbw
my_cmap = mpl.colors.LinearSegmentedColormap('my_colormap', ys, 256)
norm = mpl.colors.Normalize(-100, 50)
linewidth1 = 0.5
linewidth2 = 0.7
