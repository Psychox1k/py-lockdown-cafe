class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a person is not vaccinated."""
    def __init__(self, message="Visitor is not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Raised when the vaccine has expired."""
    def __init__(self, message="Vaccine is outdated") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Raised when a person is not wearing a mask."""
    def __init__(self, message="Visitor is not wearing a mask") -> None:
        super().__init__(message)
