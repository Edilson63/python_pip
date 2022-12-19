import matplotlib.pyplot as plt

def generate_pie_chart():
    label = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values ,label=label)
    plt.savefig('pie.png')
    plt.close()
