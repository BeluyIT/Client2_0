"""Модуль CRUD операцій для EmailVerificationService."""

from typing import Dict, Union

EmailVerificationResult = Dict[str, Union[str, bool]]


class EmailVerificationCRUD(object):
    """Клас для CRUD операцій EmailVerificationService."""

    def __init__(self, service):
        """
        Ініціалізує CRUD операції з EmailVerificationService.

        Args:
            service: Екземпляр EmailVerificationService.
        """
        self.service = service

    def create_result(
        self,
        email: str,
        verification_result: EmailVerificationResult,
    ):
        """
        Створює новий результат перевірки.

        Args:
            email (str): Електронна адреса, яка асоціюється з результатом.
            verification_result (EmailVerificationResult): Результат адреси.
        """
        self.service.save_result(email, verification_result)

    def read_results(self) -> EmailVerificationResult:
        """
        Читає всі результати перевірок.

        Returns:
            EmailVerificationResult: Результати перевірок.
        """
        return self.service.get_results()

    def update_result(
        self,
        email: str,
        updated_result: EmailVerificationResult,
    ):
        """
        Оновлює результат перевірки.

        Args:
            email (str): Електронна адреса, результат якої потрібно оновити.
            updated_result (EmailVerificationResult): Дані результату.
        """
        current_results = self.service.get_results()
        result_to_delete = current_results.get(email)
        if result_to_delete is not None:
            current_results.pop(email, None)

    def delete_result(self, email: str):
        """
        Видаляє результат перевірки.

        Args:
            email (str): Електронна адреса, результат якої потрібно видалити.
        """
        current_results = self.service.get_results()
        current_results.pop(email, None)

# Add a newline here at the end of the file
