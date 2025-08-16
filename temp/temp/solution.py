
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Data --------------------------------------------------------
user_scores = {
    "skills_match": 62,
    "experience_relevance": 100,
    "education_alignment": 100,
    "format_structure": 95,
    "keyword_optimization": 62
}

benchmarks = {
    "skills_match": 82,
    "experience_relevance": 80,
    "education_alignment": 95,
    "keyword_optimization": 78
}

categories = list(user_scores.keys())
user_vals = np.array([user_scores[c] for c in categories])
bench_vals = np.array([benchmarks.get(c, np.nan) for c in categories])

# --- Figure Setup ------------------------------------------------
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('ATS Score Visualisation', fontsize=16)

# 1. Bar chart (user vs benchmark)
ax = axes[0]
index = np.arange(len(categories))
bar_width = 0.35
ax.bar(index, user_vals, bar_width, label='User', alpha=0.7)
ax.bar(index + bar_width, bench_vals, bar_width, label='Benchmark', alpha=0.7)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_ylabel('Score (%)')
ax.set_title('User vs. Benchmark')
ax.legend()

# 2. Pie chart (weighted contribution)
ax = axes[1]
total = user_vals.sum()
sizes = user_vals / total
ax.pie(sizes, labels=categories, autopct='%1.1f%%', startangle=140)
ax.set_title('Weighted Score Contribution')

# 3. Radar chart (performance distribution)
ax = axes[2]
# Radar requires a circular axis
categories_ext = categories + [categories[0]]  # Close the loop
user_vals_ext = np.append(user_vals, user_vals[0])
bench_vals_ext = np.append(bench_vals, bench_vals[0])

angles = np.linspace(0, 2 * np.pi, len(categories_ext))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
ax.set_title('Radar Chart')
ax.plot(angles, user_vals_ext, 'b-', linewidth=2, label='User')
if not np.isnan(bench_vals_ext).all():
    ax.plot(angles, bench_vals_ext, 'r--', linewidth=2, label='Benchmark')
ax.fill(angles, user_vals_ext, 'b', alpha=0.1)
if not np.isnan(bench_vals_ext).all():
    ax.fill(angles, bench_vals_ext, 'r', alpha=0.1)
ax.set_rlabel_position(0)
ax.set_ylim(0, 100)
ax.legend(loc='upper right')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.savefig('combine_chart.png')
print("Charts generated")
