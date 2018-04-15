from matplotlib import pyplot as plt

movies=["ani","benhur","casabalanca","gandi","westworld"]
num_oscars=[4,11,3,8,10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs,num_oscars)

plt.ylabel("of award ")
plt.title("My fav. Mov.")

plt.xticks([i+0.1 for i,_ in enumerate(movies)],movies)

plt.show()
