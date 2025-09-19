from typing import Dict, List

# TODO: Implement Metrics Collection and Reporting


class Metrics:
    def __init__(self):
        self.floats: Dict[str, List[float]] = {}
        self.strings: Dict[str, List[str]] = {}
        self.data: Dict[str, List] = {}

    def reset(self) -> None:
        self.floats = {}
        self.strings = {}
        self.data = {}

    def get(self, name: str) -> List:
        return self.data.get(name, [])

    def summary(self) -> str:
        string = "Metrics Summary:\n"

        for name, values in self.strings.items():
            string += f"{name}: {', '.join(values)}\n"

        for name, values in self.floats.items():
            avg = sum(values)/len(values) if values else 0
            string += f"{name}: Avg {avg:.2f}, Count {len(values)}\n"

        return string

    def add(self, name: str, value: float | str | object) -> None:  # type: ignore
        if isinstance(value, float):
            self.floats.setdefault(name, []).append(value)
        elif isinstance(value, str):
            self.strings.setdefault(name, []).append(value)
        elif hasattr(value, '__str__'):
            self.data.setdefault(name, []).append(str(value))
        else:
            assert False, "Value must be float, str, or object with string method."
