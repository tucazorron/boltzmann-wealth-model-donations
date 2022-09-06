import mesa
import numpy as np
import pandas as pd
from datetime import datetime
from source.model import BoltzmannWealthModel

steps = 100
iterations = 100

params = {
    "N": 20,
    "D": 1,
    "width": 10,
    "height": 10,
}


if __name__ == "__main__":
    data = mesa.batch_run(
        BoltzmannWealthModel,
        params,
        iterations,
        steps,
    )

    dataframe = pd.DataFrame(data)

    now = str(datetime.now()).replace(":", "-")

    suffix = (
        "_" +
        str(iterations) +
        "_iterations_" +
        str(steps) +
        "_steps_" +
        now
    )

    dataframe.to_csv(
        "BoltzmannWealthModelDonationData" +
        suffix +
        ".csv"
    )
