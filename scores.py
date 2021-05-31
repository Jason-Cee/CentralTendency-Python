import matplotlib.pyplot as plt

test_names = ["Shuaib", "Jason", "Brent", "Yamkela", "Devin"]
test_scores = [12, 99, 65, 85, 42]
x_pos = [i for i, _ in enumerate(test_names)]  # labels on the x-axis
# labeling and visuals
plt.bar(x_pos, test_scores, color='#f9826c')
plt.xlabel("Python Scores")
plt.ylabel("Final Mark")
plt.title("Python End of Module Project")
plt.xticks(x_pos, test_names)
plt.show()
