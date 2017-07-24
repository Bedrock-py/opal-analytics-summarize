opal-analytics-summarize
=========================

## Installation

`pip install git+https://github.com/Bedrock-py/opal-analytics-summarize.git`

## Parameters Spec for Bedrock

```
[
  { "name" : "groupby", "attrname" : "groupby", "value" : "", "type" : "input" },
  { "name" : "columns", "attrname" : "columns", "value" : "", "type" : "input" }
]
```

* `groupby` Optional columns list that should be grouped during summarization `"column1,column2"`
* `columns` Optional columns list that should be returned in the summary `"column1,column2"`

## Requires a Matrix with the following files

* `matrix.csv` The full matrix with both endogenous and exogenous variables
* `features.txt` A list of column names for the matrix (one name per row)

## Outputs the following files

`matrix.csv` The summarization table
