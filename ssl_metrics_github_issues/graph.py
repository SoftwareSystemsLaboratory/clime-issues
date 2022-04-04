from argparse import Namespace

import matplotlib.pyplot as plt
import pandas
from pandas import DataFrame

from ssl_metrics_github_issues.args import graphArgs


def computeXY(
    df: DataFrame,
    xKey: str,
    yThousandth: bool,
) -> tuple:
    xData: set = df[xKey].unique().tolist()
    yData: list = []
    day: int

    if yThousandth:
        for day in xData:
            yData.append(df.groupby(day).count() / 1000)
    else:
        for day in xData:
            yData.append(df.groupby(day).count())

    return (xData, yData)


def plot(
    x: list,
    y: list,
    type: str,
    title: str,
    xLabel: str,
    yLabel: str,
    output: str,
    stylesheet: str,
) -> None:
    "param: type can only be one of the following: line, bar"

    if stylesheet is not None:
        plt.style.use(stylesheet)

    if type == "line":
        plt.plot(x, y)
    elif type == "bar":
        plt.bar(x, height=y)
    else:
        print(f"Invalid plot type: {type}. Can only be one of the following: line, bar")

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    plt.savefig(output)


def main() -> None:
    args: Namespace = graphArgs()

    df: DataFrame = pandas.read_json(args.input).T

    data: tuple = computeXY(
        df=df, xKey=args.x, yThousandth=args.y_thousandths
    )
    plot(
        x=data[0],
        y=data[1],
        type=args.type,
        title=args.title,
        xLabel=args.x_label,
        yLabel=args.y_label,
        output=args.output,
        stylesheet=args.stylesheet,
    )


if __name__ == "__main__":
    main()
