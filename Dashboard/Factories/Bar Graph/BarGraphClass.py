class BarGraph:
    def __init__(self, graphTitle, xAxisTitle, yAxisTitle, xNumberOfDataPointsPerValue, yNumberOfDataPointsPerValue, xValues, yValues):
        self.graphTitle = graphTitle
        self.xAxisTitle = xAxisTitle
        self.yAxisTitle = yAxisTitle
        self.HorPointsPerEntry = xNumberOfDataPointsPerValue
        self.VerPointsPerEntry = yNumberOfDataPointsPerValue
        self.xValues = xValues
        self.yValues = yValues