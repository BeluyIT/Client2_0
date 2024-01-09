"""Модуль для верифікації електронної пошти."""
import logging

from email_verification.client import EmailVerificationClient
from email_verification.crud_operations import EmailVerificationCRUD
from email_verification.email_service import EmailVerificationService

logging.basicConfig(level=logging.INFO)


def main():
    """Головна функція для процесу верифікації."""
    client = EmailVerificationClient()
    crud = EmailVerificationCRUD(EmailVerificationService())

    test_email = '3ujlo4eck@gmail.com'
    email_verification_result = client.verify_email(test_email)
    crud.create_result(test_email, email_verification_result)

    logging.info(crud.read_results())


if __name__ == '__main__':
    main()
