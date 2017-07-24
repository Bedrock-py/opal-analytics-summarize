
import subprocess
import os
from bedrock.analytics.utils import Algorithm
import pandas as pd
import logging
import csv


class Summarize(Algorithm):
    def __init__(self):
        super(Summarize, self).__init__()
        self.parameters = []
        self.inputs = ['matrix.csv','features.txt']
        self.outputs = ['matrix.csv']
        self.name ='Summarize'
        self.type = 'Summarize'
        self.description = 'Summary statistics on a matrix with optional group by'
        self.parameters_spec = [
            { "name" : "groupby", "attrname" : "groupby", "value" : "", "type" : "input" },
            { "name" : "columns", "attrname" : "columns", "value" : "", "type" : "input" }
        ]

    def __build_df__(self, filepath):
        featuresPath = filepath['features.txt']['rootdir'] + 'features.txt'
        matrixPath = filepath['matrix.csv']['rootdir'] + 'matrix.csv'
        df = pd.read_csv(matrixPath, header=-1)
        featuresList = pd.read_csv(featuresPath, header=-1)

        df.columns = featuresList.T.values[0]

        return df

    def compute(self, filepath, **kwargs):
        df = self.__build_df__(filepath)

        try:
            groups = self.groupby.split(',')

            if len(groups) > 0:
                df = df.groupby(groups)
        except AttributeError:
            pass


        output = df.describe()

        try:
            cols = self.columns.split(',')

            if len(cols) > 0:
                output = output[cols]
        except AttributeError:
            pass

        logging.error(output)

        self.results = {'matrix.csv': list(csv.reader(output.to_csv().split('\n')))}
