"""
pyXrm (c) 2023 Claas Huerkamp <claas.huerkamp@posteo.net>
All Rights Reserved
"""

from application import Application


def main() -> None:
    """
    Main entry point for pyXrm

    Parameters:
    None

    Returns:
    None
    """
    application: Application = Application()
    print(application.get_application_message())
    application.run()


if __name__ == "__main__":
    main()
