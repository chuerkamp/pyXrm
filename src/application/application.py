"""
pyXrm Application (c) 2023 Claas Huerkamp <claas.huerkamp@posteo.net>
All Rights Reserved
"""


class Application:
    """
    Main controller
    """

    def __init__(self) -> None:
        self.name = "pyXrm"
        self.author_name: str = "Claas Huerkamp"
        self.author_email: str = "claas.huerkamp@posteo.net"
        self.version: str = "0.1.0"
        self.license_message: str = "All rights Reserved"

    def get_application_message(self) -> str:
        return f"{self.name} Version: {self.version} (c) 2023 {self.author_name} <{self.author_email}>, {self.license_message}"

    def run(self) -> None:
        """
        Run main controller for pyXrm

        Parameters:
        self

        Return:
        None
        """
