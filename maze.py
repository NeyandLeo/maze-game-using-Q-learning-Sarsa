import matplotlib.pyplot as plt

def draw_maze(maze, path=[]):
    plt.imshow(maze, cmap='gray')
    for step in path:
        plt.scatter(step[1], step[0], color='red')
    plt.scatter(len(maze) - 1, len(maze[0]) - 1, color='green')  # 终点
    plt.show()
