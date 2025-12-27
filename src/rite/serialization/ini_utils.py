# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
INI Configuration Handler Module
=================================

Provides utilities for INI configuration file operations using Python's
standard library configparser module.

This module offers an INIHandler class with methods for:
- Reading and writing INI configuration files
- Updating and retrieving values from INI sections
- Managing sections and keys
- Validating INI file existence

All functionality uses only Python stdlib (configparser module).

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import configparser
from typing import Any

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================


class INIHandler(object):
    """
    A class for handling INI configuration files.


    Methods
    -------
    --------
    load_ini(file_path: str) -> configparser.ConfigParser:
        Loads an INI configuration file.
    save_ini(config: configparser.ConfigParser, file_path: str):
        Saves a ConfigParser object to an INI file.
    update_ini(config: configparser.ConfigParser, section: str, updates: dict[str, Any]):
        Updates a section in the ConfigParser object.
    get_value(
        config: configparser.ConfigParser,
        section: str,
        key: str,
        fallback: Any | None = None,
    ) -> Any:
        Gets a value from a section in the ConfigParser object.
    add_section(config: configparser.ConfigParser, section: str):
        Adds a new section to the ConfigParser object.
    remove_section(config: configparser.ConfigParser, section: str):
        Removes a section from the ConfigParser object.
    list_sections(config: configparser.ConfigParser) -> list[str]:
        Lists all sections in the configuration.
    list_keys(config: configparser.ConfigParser, section: str) -> list[str]:
        Lists all keys in a specific section.
    has_key(config: configparser.ConfigParser, section: str, key: str) -> bool:
        Checks if a specific key exists in a section.
    remove_key(config: configparser.ConfigParser, section: str, key: str) -> bool:
        Removes a specific key from a section.

    """

    @staticmethod
    def load_ini(file_path: str) -> configparser.ConfigParser:
        """
        Loads an INI configuration file.

        Parameters:
            file_path (str): Path to the INI file.

        Returns
        -------
            configparser.ConfigParser: The parsed INI file.
        """
        config = configparser.ConfigParser()
        config.read(file_path)
        return config

    @staticmethod
    def save_ini(config: configparser.ConfigParser, file_path: str) -> None:
        """
        Saves a ConfigParser object to an INI file.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object to save.
            file_path (str): Path to the INI file where the data will be saved.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            config.write(file)

    @staticmethod
    def update_ini(
        config: configparser.ConfigParser,
        section: str,
        updates: dict[str, Any],
    ) -> None:
        """
        Updates a section in the ConfigParser object.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object.
            section (str): The section in the INI file to update.
            updates (dict[str, Any]): A dictionary containing the updates.
        """
        if not config.has_section(section):
            config.add_section(section)
        for key, value in updates.items():
            config.set(section, key, str(value))

    @staticmethod
    def get_value(
        config: configparser.ConfigParser,
        section: str,
        key: str,
        fallback: Any | None = None,
    ) -> Any:
        """
        Gets a value from a section in the ConfigParser object.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object.
            section (str): The section from which to get the value.
            key (str): The key for the value to get.
            fallback (Any | None): The default value to return if the key
            is not found.

        Returns
        -------
            Any: The value from the specified section and key, or the fallback
            value.
        """
        return config.get(section, key, fallback=fallback)

    @staticmethod
    def add_section(config: configparser.ConfigParser, section: str) -> bool:
        """
        Adds a new section to the ConfigParser object.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object.
            section (str): The section to add.

        Returns
        -------
            bool: True if the section was added, False if the section already
            exists.
        """
        if not config.has_section(section):
            config.add_section(section)
            return True
        return False

    @staticmethod
    def remove_section(
        config: configparser.ConfigParser, section: str
    ) -> bool:
        """
        Removes a section from the ConfigParser object.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object.
            section (str): The section to remove.

        Returns
        -------
            bool: True if the section was removed, False if the section does
            not exist.
        """
        return config.remove_section(section)

    @staticmethod
    def list_sections(config: configparser.ConfigParser) -> list[str]:
        """
        Lists all sections in the configuration.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object.

        Returns
        -------
            list[str]: A list of section names.
        """
        return config.sections()

    @staticmethod
    def list_keys(
        config: configparser.ConfigParser, section: str
    ) -> list[str]:
        """
        Lists all keys in a specific section.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object.
            section (str): The section to list keys from.

        Returns
        -------
            list[str]: A list of key names in the section.
        """
        if config.has_section(section):
            return list(config[section])
        return []

    @staticmethod
    def has_key(
        config: configparser.ConfigParser, section: str, key: str
    ) -> bool:
        """
        Checks if a specific key exists in a section.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object.
            section (str): The section to check.
            key (str): The key to check for.

        Returns
        -------
            bool: True if the key exists in the section, False otherwise.
        """
        return config.has_option(section, key)

    @staticmethod
    def remove_key(
        config: configparser.ConfigParser, section: str, key: str
    ) -> bool:
        """
        Removes a specific key from a section.

        Parameters:
            config (configparser.ConfigParser): The ConfigParser object.
            section (str): The section to remove the key from.
            key (str): The key to remove.

        Returns
        -------
            bool: True if the key was removed, False if the key or section
            does not exist.
        """
        if config.has_section(section) and config.has_option(section, key):
            config.remove_option(section, key)
            return True
        return False


__all__: list[str] = [
    "INIHandler",
]
