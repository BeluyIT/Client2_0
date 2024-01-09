"""Модуль для перевірки електронної пошти через Hunter API."""

import os
from typing import Dict, Union

import requests


class EmailVerificationClient(object):
    """Клієнт для перевірки електронної пошти через Hunter API."""

    def __init__(self):
        """Ініціалізує клієнт з ключем API та базовим URL."""
        self.api_key = os.getenv('HUNTER_API_KEY')
        self.base_url = 'https://api.hunter.io/v2'

    def verify_email(self, email: str) -> Dict[str, Union[str, bool]]:
        """
        Перевіряє електронну пошту, повертаючи відповідь у форматі JSON.

        Args:
            email (str): Електронна адреса для перевірки.

        Returns:
            Dict[str, Union[str, bool]]: Відповідь від API у форматі JSON.
        """
        endpoint = '{0}/email-verifier'.format(self.base_url)
        query_params = {'email': email, 'api_key': self.api_key}
        response = requests.get(
            endpoint,
            params=query_params,
            timeout=10,
        )

        return response.json()

    def get_email_info(self, email: str) -> Dict[str, Union[str, bool]]:
        """
        Отримує інформацію про електронну пошту у форматі JSON.

        Args:
            email (str): Електронна адреса для отримання інформації.

        Returns:
            Dict[str, Union[str, bool]]: Відповідь від API у форматі JSON.
        """
        endpoint = '{0}/get-email-info'.format(self.base_url)
        query_params = {'email': email, 'api_key': self.api_key}
        response = requests.get(
            endpoint,
            params=query_params,
            timeout=10,
        )
        return response.json()

# Add a newline here at the end of the file
