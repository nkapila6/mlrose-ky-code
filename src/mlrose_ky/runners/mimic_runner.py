"""
Class for running optimization experiments using MIMIC, including grid search functionality.

Example usage:

    experiment_name = 'example_experiment'
    problem = TSPGenerator.generate(seed=SEED, number_of_cities=22)

    mmc = MIMICRunner(problem=problem,
                      experiment_name=experiment_name,
                      output_directory=OUTPUT_DIRECTORY,
                      seed=SEED,
                      iteration_list=2 ** np.arange(10),
                      max_attempts=500,
                      keep_percent_list=[0.25, 0.5, 0.75])

    df_run_stats, df_run_curves = mmc.run()
"""

# Authors: Andrew Rollings (modified by Kyle Nakamura)
# License: BSD 3-clause

from typing import Any

import numpy as np
import pandas as pd

from mlrose_ky.algorithms import mimic
from mlrose_ky.decorators import short_name
from mlrose_ky.runners._runner_base import _RunnerBase


@short_name("mimic")
class MIMICRunner(_RunnerBase):
    """
    A runner for performing optimization experiments using MIMIC.

    This class extends _RunnerBase and provides functionality for running experiments
    with the MIMIC algorithm, including grid search over hyperparameters such as
    population size and keep percent.

    Attributes
    ----------
    keep_percent_list : list[float]
        List of keep percentages to test in the grid search.
    population_sizes : list[int]
        List of population sizes to test in the grid search.
    _use_fast_mimic : bool, optional
        Whether to use the fast MIMIC mode, if available.
    """

    def __init__(
        self,
        problem: Any,
        experiment_name: str,
        seed: int,
        iteration_list: np.ndarray | list[int],
        population_sizes: list[int],
        keep_percent_list: list[float],
        max_attempts: int = 5,
        generate_curves: bool = True,
        use_fast_mimic: bool = True,
        output_directory: str = None,
        **kwargs: Any,
    ):
        """
        Initialize the MIMICRunner class with problem data and various experiment parameters.

        Parameters
        ----------
        problem : Any
            The optimization problem to be solved.
        experiment_name : str
            Name of the experiment.
        seed : int
            Random seed for reproducibility.
        iteration_list : np.ndarray | list of int
            List of iterations for the experiment.
        population_sizes : list of int
            List of population sizes to test in the grid search.
        keep_percent_list : list of float
            List of keep percentages to test in the grid search.
        max_attempts : int, optional
            Maximum number of attempts without improvement before stopping.
        generate_curves : bool, optional
            Whether to generate learning curves.
        use_fast_mimic : bool, optional
            Whether to use the fast MIMIC mode, if available.
        output_directory : str, optional
            Directory to save experiment result, default=None.
        """
        super().__init__(
            problem=problem,
            experiment_name=experiment_name,
            seed=seed,
            iteration_list=iteration_list,
            max_attempts=max_attempts,
            generate_curves=generate_curves,
            output_directory=output_directory,
            **kwargs,
        )
        self.keep_percent_list: list[float] = keep_percent_list
        self.population_sizes: list[int] = population_sizes
        self._use_fast_mimic: bool | None = None

        # Set fast MIMIC mode if available
        if hasattr(problem, "set_mimic_fast_mode") and callable(getattr(problem, "set_mimic_fast_mode")):
            self._use_fast_mimic = use_fast_mimic
            problem.set_mimic_fast_mode(use_fast_mimic)

    def _setup(self):
        """
        Perform any necessary setup before running the experiment.

        Logs the current state of the fast MIMIC mode if it is enabled.
        """
        super()._setup()

        if self._use_fast_mimic is not None:
            self._log_current_argument("use_fast_mimic", self._use_fast_mimic)

    def run(self) -> tuple[pd.DataFrame | None, pd.DataFrame | None]:
        """
        Run the MIMIC algorithm experiment.

        This method performs grid search over the provided population sizes
        and keep percentages and returns the statistics and curves generated by the experiment.

        Returns
        -------
        tuple
            A tuple containing two DataFrames: run statistics and run curves
        """
        return super().run_experiment_(
            algorithm=mimic, pop_size=("Population Size", self.population_sizes), keep_pct=("Keep Percent", self.keep_percent_list)
        )