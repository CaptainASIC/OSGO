# OSGO
# CleanBoot

CleanBoot is a Python script that automates the installation of essential software packages on various Linux distributions and macOS. It detects your operating system and installs a predefined set of tools and utilities, making it easier to set up a new system or maintain consistency across different machines.

## Features

- Automatic OS detection (Arch, PopOS, Debian, Ubuntu, macOS, and others)
- Installation of common utilities and development tools
- CPU detection for architecture-specific installations
- BTRFS tools installation
- System monitoring tools installation (lm_sensors, lsusb, lspci)

## Supported Operating Systems

- Arch Linux
- PopOS
- Debian
- Ubuntu
- macOS (partial support)

## Quick Start

To download and run CleanBoot, use the following one-line command:

```bash
curl -sSL https://raw.githubusercontent.com/yourusername/cleanboot/main/cleanboot.py | sudo python3 -
```

This command downloads the script and immediately executes it with sudo privileges. Make sure to review the script before running it on your system.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Disclaimer

CleanBoot makes changes to your system by installing software packages. While it's designed to be safe, please make sure you understand the changes it will make to your system. Always back up your important data before running system-modifying scripts.

## Contributing

Contributions to CleanBoot are welcome! Please feel free to submit pull requests, report bugs, or suggest features.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.