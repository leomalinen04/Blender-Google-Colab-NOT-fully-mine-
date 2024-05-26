#initial code to start the notebook for usage
import psutil
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
print("="*40, "Memory Information", "="*40)
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}") ; print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}") ; print(f"Percentage: {svmem.percent}%")

#check the specs of what you have (be sure you enable the GPU in the edit configuration in the notebook)
! nvidia-smi

#updated code for blender usage with the latest blender release
Blender_Version = 'Blender 4.1.1' #@param ["Blender 4.1.1"]

def path_leaf(path):
  import ntpath
  head, tail = ntpath.split(path)
  return tail or ntpath.basename(head)

dl_link = {
    "Blender 4.1.1" : "https://download.blender.org/release/Blender4.1/blender-4.1.1-linux-x64.tar.xz"
}

dl = dl_link[Blender_Version]
filename = path_leaf(dl)

!wget -nc $dl
!mkdir ./blender && tar xf $filename -C ./blender --strip-components 1

!apt install libboost-all-dev
!apt install libgl1-mesa-dev
!apt install libglu1-mesa libsm-dev

data = "import re\n"+\
    "import bpy\n"+\
    "scene = bpy.context.scene\n"+\
    "scene.cycles.device = 'GPU'\n"+\
    "prefs = bpy.context.preferences\n"+\
    "prefs.addons['cycles'].preferences.get_devices()\n"+\
    "cprefs = prefs.addons['cycles'].preferences\n"+\
    "print(cprefs)\n"+\
    "# Attempt to set GPU device types if available\n"+\
    "for compute_device_type in ('CUDA', 'OPENCL', 'NONE'):\n"+\
    "    try:\n"+\
    "        cprefs.compute_device_type = compute_device_type\n"+\
    "        print('Device found',compute_device_type)\n"+\
    "        break\n"+\
    "    except TypeError:\n"+\
    "        pass\n"+\
    "# Enable all CPU and GPU devices\n"+\
    "for device in cprefs.devices:\n"+\
    "    if not re.match('intel', device.name, re.I):\n"+\
    "        print('Activating',device)\n"+\
    "        device.use = True\n"
with open('setgpu.py', 'w') as f:
    f.write(data)

#mount to google drive + the content
from google.colab import drive
drive.mount('/gdrive')

from google.colab import drive
drive.mount('/content/drive')

#execute blender render commands with sample files (second line of code is animation with frames ex 1-100)
!sudo ./blender/blender -P setgpu.py -b '/content/drive/My Drive/Monkey.blend' -o '/content/drive/My Drive/Monkey.png' -f 1

!sudo ./blender/blender -P setgpu.py -b '/content/drive/My Drive/Monkey.blend' -o '/content/drive/My Drive/Monkey_####.png' -s 1 -e 5 -a
