
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- USER SCORES --------------------------------------------------
user_scores = {
    "skills_match": 62,
    "experience_relevance": 100,
    "education_alignment": 100,
    "format_structure": 95,
    "keyword_optimization": 62
}

# --- BENCHMARKS -----------------------------------------------------
# 0 indicates no benchmark for that category
benchmarks = {
    "skills_match": 82,
    "experience_relevance": 80,
    "education_alignment": 95,
    "keyword_optimization": 78
    # format_structure has no benchmark
}

categories = list(user_scores.keys())
user_vals = np.array([user_scores[c] for c in categories], dtype=float)
bench_vals = np.array([benchmarks.get(c, 0) for c in categories], dtype=float)

# --- PLOT SETUP -------------------------------------------------------
sns.set_style("whitegrid")
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# ---- 1. BAR CHART -------------------------------------------------------
ax_bar = axs[0, 0]
ind = np.arange(len(categories))
width = 0.35
ax_bar.bar(ind - width/2, user_vals, width, label='User', color='tab:blue', alpha=0.7)
ax_bar.bar(ind + width/2, bench_vals, width, label='Benchmark', color='tab:orange', alpha=0.5)
ax_bar.set_xticks(ind)
ax_bar.set_xticklabels(categories, rotation=45, ha='right')
ax_bar.set_ylabel('Score (%)')
ax_bar.set_title('User vs. Benchmark Scores')
ax_bar.set_ylim(0, max(max(user_vals), max(bench_vals)) + 20)
ax_bar.legend()

# ---- 2. PIE CHART -------------------------------------------------------
ax_pie = axs[0, 1]
ax_pie.pie(user_vals,
           labels=categories,
           autopct='%1.1f%%',
           startangle=90,
           counterclock=False,
           colors=sns.color_palette('pastel'))
ax_pie.set_title('Weighted Score Contribution')

# ---- 3. RADAR CHART -------------------------------------------------------
num = len(categories)
angles = np.linspace(0, 2*np.pi, num, endpoint=False).tolist()
angles += angles[:1]
user_ext = np.concatenate([user_vals, [user_vals[0]]])
bench_ext = np.concatenate([bench_vals, [bench_vals[0]]])

# Create a polar subplot in the lower left quadrant
ax_radar = fig.add_axes([0.55, 0.15, 0.35, 0.35], polar=True)
ax_radar.set_theta_offset(np.pi / 2)
ax_radar.set_theta_direction(-1)
ax_radar.set_thetagrids(np.degrees(angles[:-1]), categories)
ax_radar.plot(angles, user_ext, label='User', color='tab:blue', linewidth=2)
ax_radar.plot(angles, bench_ext, label='Benchmark', color='tab:orange', linewidth=2)
ax_radar.fill(angles, user_ext, color='tab:blue', alpha=0.1)
ax_radar.fill(angles, bench_ext, color='tab:orange', alpha=0.1)
ax_radar.set_rlim(0, 120)
ax_radar.set_title('Radar Chart of Category Performance', y=1.08)
ax_radar.legend(loc='upper right')

# ---- 4. EMPTY SLOT -------------------------------------------------------
axs[1, 1].axis('off')

# ---- FINALISE ------------------------------------------------------------
plt.tight_layout()
fig.savefig('combine_chart.png', dpi=300, bbox_inches='tight')
plt.close(fig)

print('Charts generated')
