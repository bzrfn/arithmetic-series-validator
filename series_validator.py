from __future__ import annotations

from typing import Iterable, List, Optional

import pandas as pd


class ArithmeticProgressionValidator:
    """Valida si una secuencia numérica sigue una progresión aritmética."""

    def __init__(self, numbers: Iterable[float]):
        self.numbers: List[float] = list(numbers)

    def is_arithmetic_progression(self) -> bool:
        """Retorna True si la lista sigue una progresión aritmética."""
        if len(self.numbers) < 2:
            return False

        series = pd.Series(self.numbers)
        differences = series.diff().dropna()

        return differences.nunique() == 1

    def get_difference(self) -> Optional[float]:
        """Retorna la diferencia común si la serie es válida; en caso contrario, None."""
        if not self.is_arithmetic_progression():
            return None

        series = pd.Series(self.numbers)
        difference = series.diff().dropna().iloc[0]

        if pd.isna(difference):
            return None

        return int(difference) if float(difference).is_integer() else float(difference)
