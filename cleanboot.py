import platform
import os
import subprocess

def detect_os():
    system = platform.system()
    if system == "Linux":
        try:
            with open("/etc/os-release") as f:
                os_release = f.read()
            if "Arch Linux" in os_release:
                return "Arch"
            elif "Pop!_OS" in os_release:
                return "PopOS"
            elif "Debian" in os_release:
                return "Debian"
            elif "Ubuntu" in os_release:
                return "Ubuntu"
            else:
                return "Other"
        except:
            return "Other"
    elif system == "Darwin":
        return "Mac"
    else:
        return "Other"

def detect_cpu():
    if platform.machine().lower() == "x86_64":
        vendor = platform.processor()
        if "intel" in vendor.lower():
            return "intel"
        else:
            return "amd"
    else:
        return "other"

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def install_software(os_name):
    cpu = detect_cpu()
    
    if os_name == "Arch":
        run_command("sudo pacman -Syu")
        run_command("sudo pacman -S --needed base-devel git")
        run_command("git clone https://aur.archlinux.org/yay.git")
        run_command("cd yay && makepkg -si")
        run_command("yay -S atuin conda neofetch git tailscale exiftool nano lm_sensors usbutils pciutils btrfs-progs")
    elif os_name in ["PopOS", "Debian", "Ubuntu"]:
        run_command("sudo apt update && sudo apt upgrade -y")
        run_command("sudo apt install -y atuin conda neofetch git tailscale exiftool nano lm-sensors usbutils pciutils btrfs-progs")
    elif os_name == "Mac":
        run_command("brew update")
        run_command("brew install atuin conda neofetch git tailscale exiftool nano osx-cpu-temp")
        
    else:
        print("Unsupported OS. Please install the software manually.")
        return

    # Install minicode based on CPU
    if cpu == "intel":
        run_command("wget https://github.com/sharkdp/minicode/releases/download/v0.1.0/minicode-x86_64-intel-linux.tar.gz")
        run_command("tar -xvf minicode-x86_64-intel-linux.tar.gz")
    elif cpu == "amd":
        run_command("wget https://github.com/sharkdp/minicode/releases/download/v0.1.0/minicode-x86_64-amd-linux.tar.gz")
        run_command("tar -xvf minicode-x86_64-amd-linux.tar.gz")
    else:
        print("Unsupported CPU architecture for minicode. Please install manually.")

    if os_name != "Mac":
        print("Running sensors-detect to configure lm_sensors...")
        run_command("sudo sensors-detect --auto")

def main():
    os_name = detect_os()
    print(f"Detected OS: {os_name}")
    install_software(os_name)
    print("Installation complete. You may need to restart your terminal or log out and back in for some changes to take effect.")

if __name__ == "__main__":
    main()