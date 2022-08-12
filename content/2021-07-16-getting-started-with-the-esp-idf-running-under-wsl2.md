---
title: Getting started with the ESP-IDF running under WSL2
date: 2021-07-16 18:10 -0600
category: Embedded
tags: [esp32, c, c++, idf]
---

I'm really excited about this post, because it's the first post slightly related to
Embedded Systems, and that's the topic I was expecting to write about when I started this blog.
The second reason is because I love the ESP32, specially using the [ESP IoT Development Framework](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/). It's been a while since I worked with an ESP32 using the IDF (2019 actually), and the framework changed a lot since, so after all this time, I decided to get myself a dev board and explore the IDF again.

When I started working with the ESP32, I followed the excellent [Neil Kolban's Book on ESP32](https://leanpub.com/kolban-ESP32), but I've heard it's slightly outdated now, so your best bet is definitely the also excelent [IDF Documentation from Espressif](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/index.html).

As I wrote [before](https://andres.world/tools/2020/08/01/development-setup-on-windows-10/), I've been using mostly Windows 10 with WSL2 for my development work, so setting up the IDF under WSL2 might be a little different to the average process you follow if running under an actual Linux distribution. This guide is a quick guide on how to start working with an ESP32 using WSL2.

# 1. Install the CP210x USB to UART Bridge VCP Drivers

Assuming you're using one of the very common [ESP32 DevKit Boards](https://www.espressif.com/en/products/devkits/esp32-devkitc/overview), you'll need the drivers for the on-board programming chip. You can download them and easily install them from [Silicon Lab's website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

After installing the drivers, connect your development board using an USB cable, and you should be able to see your board and the related serial (COM) port under Device Manager.

![CP210x USB to UART Bridge showing under Device Manager]({static}/images/esp32/uart.png)

*CP210x USB to UART Bridge showing under Device Manager*

# 2. Make sure you're running Python 3 and esptools in Windows

You must have Python 3 in both your WSL subsystem and Windows itself. 

```powershell
> python --version
Python 3.9.4
```

You also need `esptool` installed in your Windows Python environment, so open up PowerShell or your shell of choice and install the package using pip:

```powershell
pip install esptool --user
```

# 3. Install idfx in your WSL2 system

`idfx` is a simple tool made by [abobija](https://github.com/abobija) that lets you interact with your ESP32 from WSL2. Installation is pretty simple:

```bash
wget https://raw.githubusercontent.com/abobija/idfx/main/idfx -O $HOME/.local/bin/idfx && chmod u+x $HOME/.local/bin/idfx
```

Check the [project's page](https://github.com/abobija/idfx) to learn how to use the tool.

Remember to add `$HOME/.local/bin/` to your `PATH` variable, if you don't, your shell won't be able to run `idfx`:
```bash
$ idfx --help
zsh: command not found: idfx
```

# 4. Install the ESP - IDF dependencies on your WSL2 subsystem

Follow the steps found on the [Standard Setup of Toolchain for Linux](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-setup.html) page from Espressif's documentation. Ignore the permission issues part.

Assuming you're using Ubuntu (or Debian):
```bash
sudo apt-get install git wget flex bison gperf python3 python3-pip python3-setuptools cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
```

# 5. Get the ESP - IDF and install it

In your WSL2 subsystem, clone the IDF repo using Git:
```bash
mkdir -p ~/esp
cd ~/esp
git clone --recursive https://github.com/espressif/esp-idf.git
```

Then, run the install script:
```bash
cd ~/esp/esp-idf
./install.sh
```

Finally, source the environment variables:
```bash
. $HOME/esp/esp-idf/export.sh
```

**Tip**: If you're planning to use the IDF frequently, create an alias for the export script under your `.bashrc` or `.zshrc`:
```bash
alias get_idf='. $HOME/esp/esp-idf/export.sh'
```

*Taken from [Espressif's documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html#get-started-get-esp-idf)*

# 6. Build a project

Let's start with a good ol' Hello World. The IDF provides a lot of examples you can use to get yourself started. Let's use the `hello-world` project:
```bash
cd ~/esp
cp -r $IDF_PATH/examples/get-started/hello_world .
```

If you exported your environment variables, you should have access to the `idf.py` tool, the central part of the IDF:
```bash
cd ~/esp/hello_world
idf.py set-target esp32 # Configures the project for the ESP32
idf.py menuconfig # Opens the configuration menu
```

You can change the configuration all you want, but I'll go with the default configuration and just press "Q" and save.

![ESP-IDF menuconfig]({attach}/images/esp32/menuconfig.png)

*ESP-IDF menuconfig*

Then, build the project:
```bash
idf.py build
```

Once that's done, use `idfx` to flash and monitor the ESP32's serial output:
```bash
idfx flash COM3
```

(You can find your COM port's number by looking at the Device Manager).

```bash
idfx monitor COM3
```

If you did everything right, you should be getting output from the ESP32:
![ESP32 serial output]({attach}/images/esp32/hello-world.png)

*ESP32 serial output*

And that's it! You should now have all you need to play around with the IDF and build cool stuff. Thanks for reading, hope this is useful, and see you next time!
