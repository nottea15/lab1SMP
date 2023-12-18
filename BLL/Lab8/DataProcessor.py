import os
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


class DataProcessor:
    # Constructor for the DataProcessor class
    def __init__(self):
        # Get the current file directory and the relative path to the data file
        current_file_directory = os.path.dirname(os.path.abspath(__file__))
        relative_file_path = os.path.join(current_file_directory, 'iris.csv')

        # Load the data from the CSV file into a pandas DataFrame
        self.df = pd.read_csv(relative_file_path)

        # Define the output directory for saving visualizations
        self.output_directory = os.path.join('..', 'Data')

    # Method to explore the data
    def explore_data(self):
        # Print the descriptive statistics of the DataFrame
        print(self.df.describe())

        # Print the maximum values of each column in the DataFrame
        print("\nMaximum values:\n", self.df.max())

        # Print the minimum values of each column in the DataFrame
        print("\nMinimum values:\n", self.df.min())

    # Method to visualize the data
    def visualize_data(self, save=False):
        # Basic visualization: scatter plot of sepal length vs sepal width
        plt.scatter(self.df['sepal.length'], self.df['sepal.width'])
        plt.title('Basic Visualization')
        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'basic_visualization.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'basic_visualization.png'), format='png')
        else:
            plt.show()

        # Extended visualizations: scatter plot with different colors for each variety
        colors = {'Setosa': 'r', 'Versicolor': 'g', 'Virginica': 'b'}
        plt.scatter(self.df['sepal.length'], self.df['sepal.width'], c=self.df['variety'].apply(lambda x: colors[x]))
        plt.title('Extended Visualization')
        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'extended_visualization.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'extended_visualization.png'), format='png')
        else:
            plt.show()

        # Multiple subplots: scatter plots of sepal length vs sepal width and petal length vs petal width
        fig, axs = plt.subplots(2)
        fig.suptitle('Vertically stacked subplots')
        axs[0].scatter(self.df['sepal.length'], self.df['sepal.width'], c=self.df['variety'].apply(lambda x: colors[x]))
        axs[0].set(xlabel='Sepal Length', ylabel='Sepal Width')
        axs[1].scatter(self.df['petal.length'], self.df['petal.width'], c=self.df['variety'].apply(lambda x: colors[x]))
        axs[1].set(xlabel='Petal Length', ylabel='Petal Width')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'multiple_subplots.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'multiple_subplots.png'), format='png')
        else:
            plt.show()

        # Violin plot of sepal length distribution by variety
        plt.figure(figsize=(10, 6))
        sns.violinplot(x='variety', y='sepal.length', data=self.df, hue='variety', palette='Set1', legend=False)
        plt.title('Sepal Length Distribution by Variety')
        plt.xlabel('Flower Variety')
        plt.ylabel('Sepal Length')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'violin_plot.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'violin_plot.png'), format='png')
        else:
            plt.show()

        # Bar plot
        plt.figure(figsize=(10, 6))
        sns.barplot(x='variety', y='sepal.length', data=self.df)
        plt.title('Bar Plot of Sepal Length by Variety')
        plt.xlabel('Flower Variety')
        plt.ylabel('Sepal Length')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'bar_plot.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'bar_plot.png'), format='png')
        else:
            plt.show()

        # Histogram
        plt.figure(figsize=(10, 6))
        plt.hist(self.df['sepal.length'], bins=10)
        plt.title('Histogram of Sepal Length')
        plt.xlabel('Sepal Length')
        plt.ylabel('Frequency')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'histogram.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'histogram.png'), format='png')
        else:
            plt.show()

        # Pie chart
        plt.figure(figsize=(10, 6))
        variety_counts = self.df['variety'].value_counts()
        plt.pie(variety_counts, labels=variety_counts.index, autopct='%1.1f%%')
        plt.title('Pie Chart of Flower Varieties')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'pie_chart.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'pie_chart.png'), format='png')
        else:
            plt.show()

        # Facet plot: scatter plots of sepal length vs sepal width for each variety
        g = sns.FacetGrid(self.df, col='variety', height=5, aspect=1)
        g.map(plt.scatter, 'sepal.length', 'sepal.width', alpha=0.7)
        g.set_titles(col_template="{col_name}")
        g.set_axis_labels('Sepal Length', 'Sepal Width')

        if save:
            g.savefig(os.path.join(self.output_directory, 'facet_plot.svg'))
            g.savefig(os.path.join(self.output_directory, 'facet_plot.png'))
        else:
            plt.show()




