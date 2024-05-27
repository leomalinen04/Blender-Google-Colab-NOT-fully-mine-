#check the specs of what you have (be sure you enable the GPU in the edit configuration in the notebook)
! nvidia-smi

#be sure to make the directory for where to store the image sequence below
mkdir Image_Sequence

#updated code for blender usage with the latest blender release (change the blend file to whatever the name of your project is)
#Step-1: Connect Google Drive to colab
from google.colab import drive
drive.mount('/content/drive')

#Step-2: Install Blender from google drive to colab
!tar xf '/content/drive/My Drive/Colab-Render/blender-4.1.1-linux-x64.tar.xz' -C "/content"

#Step-3: Remove existing folder on colab, if any
!rm -rf "./Image Sequence"

#Step-4: Render the animation on colab
! ./blender-4.1.1-linux-x64/blender -b -P "/content/drive/My Drive/Colab-Render/enable_gpu.py" "/content/drive/My Drive/Colab-Render/LCorpJet.blend" -noaudio -F PNG -E CYCLES -o "/content/Image_Sequence/" -f 1

#Step-5: Copy output files from colab to drive
import shutil
shutil.copytree("/content/Image_Sequence", "/content/drive/My Drive/Colab-Render/Image Sequence", dirs_exist_ok=True)
