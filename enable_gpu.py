import bpy, _cycles

bpy.context.scene.cycles.device = 'GPU'

avail_devices = _cycles.available_devices('CUDA')
print(avail_devices)

prop = bpy.context.preferences.addons['cycles'].preferences

prop.get_devices(prop.compute_device_type)
prop.compute_device_type = 'CUDA'

for device in prop.devices:
    if device.type == 'CUDA':
        print('device: ', device)
        device.use = True
