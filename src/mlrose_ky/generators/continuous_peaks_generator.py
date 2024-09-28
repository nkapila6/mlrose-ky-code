"""Class defining a Continuous Peaks optimization problem generator."""

# Authors: Genevieve Hayes (modified by Andrew Rollings, Kyle Nakamura)
# License: BSD 3-clause

import numpy as np

from mlrose_ky import DiscreteOpt, ContinuousPeaks


class ContinuousPeaksGenerator:
    """A class to generate Continuous Peaks optimization problems."""

    @staticmethod
    def generate(seed: int = 42, size: int = 20, t_pct: float = 0.1) -> DiscreteOpt:
        """
        Generate a Continuous Peaks optimization problem instance.

        Parameters
        ----------
        seed : int, optional, default=42
            Seed for the random number generator.
        size : int, optional, default=20
            The size of the optimization problem.
        t_pct : float, optional, default=0.1
            The threshold percentage for the Continuous Peaks fitness function.

        Returns
        -------
        problem : Any
            An instance of the DiscreteOpt class representing the optimization problem.

        Raises
        ------
        ValueError
            If the `size` is not a positive integer or if `t_pct` is not between 0 and 1.
        """
        if not isinstance(size, int) or size <= 0:
            raise ValueError(f"Size must be a positive integer. Got {size}")
        if not isinstance(t_pct, float):
            raise ValueError(f"Threshold percentage must be a float. Got {type(t_pct).__name__}")
        if not (0 <= t_pct <= 1):
            raise ValueError(f"Threshold percentage must be between 0 and 1. Got {t_pct}")

        np.random.seed(seed)

        fitness = ContinuousPeaks(t_pct=t_pct)
        return DiscreteOpt(length=size, fitness_fn=fitness)