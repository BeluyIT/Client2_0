"""Модуль, для результатів перевірки електронної пошти."""

from typing import Dict, Union

EmailVerificationResult = Dict[str, Union[str, bool]]


class EmailVerificationService(object):
    """Сервіс для перевірки електронної пошти."""

    def __init__(self):
        """Ініціалізує внутрішній сховище для результатів."""
        self._email_results = {}

    def save_result(
        self,
        email: str,
        verification_result: EmailVerificationResult,
    ):
        """
        Зберігає результат перевірки для вказаної електронної пошти.

        Args:
            email (str): Електронна адреса, для якої зберігається результат.
            verification_result (EmailVerificationResult): Результат перевірки.
        """
        self._email_results[email] = verification_result

    def get_results(self) -> Dict[str, EmailVerificationResult]:
        """
        Повертає усі збережені результати перевірок.

        Returns:
            Dict[str, EmailVerificationResult]: Результатами перевірок.
        """
        return self._email_results

# Add a newline here at the end of the file
