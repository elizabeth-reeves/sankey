import plotly.graph_objects as go
import sys
import random

# require an input data file (example provided at bottom)
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    raise Exception("please provide a file name")

# open the data file and read it in
with open(filename, "r") as file:
    # split each line and strip off newline characters
    lines = [line.strip().split(",") for line in file.readlines()]
    # take the first row for labels
    labels = lines[0][1:]
    # change strings to floats in nested lists, excluding the labels
    mat = [[float(item) for item in lst[1:]] for lst in lines[1:]]

source = []
target = []
value = []

# check for square dimensions
if len(mat) != len(mat[0]):
    raise Exception("Matrix Dimensions are not Square")

# read in all nonzero values from the matrix
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] != 0:
            source.append(i)
            target.append(j)
            value.append(mat[i][j])

# initialize a random color for each node
# colors = ['rgba({}, {}, {}, 0.8)'.format(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
#           for dummy in labels]

colors = ['rgba(2, 54, 24, 0.8)',  # green
          'rgba(114, 14, 7, 0.8)',  # red
          'rgba(62, 146, 204, 0.8)',  # lightest blue
          'rgba(246, 174, 45, 0.8)',  # yellow
          'rgba(164, 66, 0, 0.8)',  # orange 1
          'rgba(10, 36, 99, 0.8)',  # dark blue
          'rgba(87, 92, 85, 0.8)',  # grey
          'rgba(220, 129, 24, 0.8)',  # fulvous
          'rgba(36, 91, 152, 0.8)',  # blue
          'rgba(114, 157, 88, 0.8)'  # light green
          ]
# make all edges have the same color as the node they end on
edge_colors = [colors[i].replace("0.8", "0.4") for i in target]

fig = go.Figure(go.Sankey(
    node={
        "label": labels,
        "pad": 50,
        "color": colors
        },
    link={
        "source": source,
        "target": target,
        "value": value,
        "color": edge_colors
        }
    )
)

fig.show()
