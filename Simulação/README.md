# Download pre-compiled binaries from the AirSim repository
- Download and extract `Blocks.zip` for [Windows 🍷](https://github.com/microsoft/AirSim/releases/tag/v1.4.0-windows) or [Linux 🐧](https://github.com/microsoft/AirSim/releases/tag/v1.4.0-linux)
- See the [reference instructions](https://github.com/microsoft/AirSim/blob/master/docs/use_precompiled.md) (*obs.: look at **Unreal Engine** and **Controlling Vehicles***)

# 🍷 Windows instructions
## Creating a `virtualenv` and installing `airsim`
```bash
$ python -m venv venv
$ venv\Scripts\activate.bat
$ pip install airsim
```
## Launcing `Blocks` and running the script
```bash
$ start path\to\Blocks\WindowsNoEditor\Blocks.exe -ResX=640 -ResY=360 -windowed
$ python path\to\follow_directions.py --directions directions.json
```

# 🐧 Linux instructions
## Creating a `virtualenv` and installing `airsim`
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install airsim
```
## Launcing `Blocks` and running the script
```bash
$ ./Blocks/LinuxNoEditor/Blocks.sh -ResX=640 -ResY=360 -windowed
$ python3 path/to/follow_directions.py --directions directions.json
```
