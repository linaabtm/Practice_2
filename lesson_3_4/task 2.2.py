import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 5))
x = np.linspace(-3*np.pi, 3*np.pi, 250)
y=np.sin(x)
plt.scatter(x, y)

plt.scatter(x, y,
 s=150,
 marker='s',
 c='blue',
 lw=1.5,
 edgecolor='green',
 hatch='++'
 )

plt.title(
 label='$sin(x)$ with random noise', # Заголовок
 fontsize=14 # Размер шрифта
)
plt.xlabel('x range', fontsize=14)
plt.ylabel('y range', fontsize=14)
plt.tick_params(labelsize=12)

plt.xticks(
 ticks=np.arange(-3*np.pi, 3*np.pi, 1.5) # Нужные значения по оси x
)
plt.yticks(
 ticks=np.arange(-5, 2,1), # Значения по оси y будут заменены на подкписи,
 # Которые будут на этих позициях
 labels=['можно', 'написать', 'все', 'что', 'хочется', 'вообще', 'все ='][::-1])
plt.show()