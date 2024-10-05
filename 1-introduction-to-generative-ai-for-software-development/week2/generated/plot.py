# Prompt: You are an expert in building interactive dashboards for websites with deep familiarity of the matplotlib library in python. Create an interactive piechart that will be included in a website dashboard

import matplotlib.pyplot as plt
import mpld3

# Sample data
labels = ["Category A", "Category B", "Category C", "Category D"]
sizes = [15, 30, 45, 10]
colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]

# Create a pie chart
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140
)

# Customize the plot
plt.setp(autotexts, size=10, weight="bold", color="white")
ax.set_title("Sample Interactive Pie Chart")

# Make the plot interactive
tooltip = mpld3.plugins.PointLabelTooltip(wedges, labels=labels)
mpld3.plugins.connect(fig, tooltip)

# Save to HTML
html_str = mpld3.fig_to_html(fig)
with open("interactive_pie_chart.html", "w") as f:
    f.write(html_str)

# Optionally, display the plot in a web browser
mpld3.show()
