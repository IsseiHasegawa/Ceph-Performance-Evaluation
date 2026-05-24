import matplotlib.pyplot as plt
import numpy as np

cache_sizes = ['10 MB', '50 MB', '100 MB', '500 MB', '1 GB', '2 GB']
x = np.arange(len(cache_sizes))

lru  = [0.8366, 0.8277, 0.8210, 0.7174, 0.6297, 0.4301]
lfu  = [0.8245, 0.8174, 0.8081, 0.6737, 0.5653, 0.4301]
fifo = [0.8413, 0.8290, 0.8214, 0.7380, 0.6335, 0.4301]
arc  = [0.8248, 0.8130, 0.7967, 0.6525, 0.5687, 0.4301]

fig, ax = plt.subplots(figsize=(8, 4.5))

ax.plot(x, lru,  color='#378ADD', linewidth=2, marker='o',
        markersize=5, label='LRU')
ax.plot(x, lfu,  color='#1D9E75', linewidth=2, marker='^',
        markersize=5, linestyle='--', label='LFU')
ax.plot(x, fifo, color='#D85A30', linewidth=2, marker='s',
        markersize=5, linestyle=':', label='FIFO')
ax.plot(x, arc,  color='#7F77DD', linewidth=2, marker='D',
        markersize=5, label='ARC')

ax.scatter([4], [0.799], color='#E24B4A', s=120, zorder=5,
           label='BlueStore actual (1 GB)')

ax.set_xticks(x)
ax.set_xticklabels(cache_sizes, fontsize=11)
ax.set_xlabel('Cache size', fontsize=12)
ax.set_ylabel('Miss rate', fontsize=12)
ax.set_ylim(0.3, 0.95)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.2f}'))
ax.grid(axis='y', color='gray', alpha=0.2, linewidth=0.8)
ax.grid(axis='x', color='gray', alpha=0.1, linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(
    fontsize=9,
    framealpha=0.9,
    loc='upper center',
    bbox_to_anchor=(0.5, -0.18),
    ncol=3,
    columnspacing=1.0,
)

plt.tight_layout(rect=(0, 0.14, 1, 1))
