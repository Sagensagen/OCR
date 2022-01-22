import torch

print("CUDA available?: ",torch.cuda.is_available())
print('CUDA current device index: ', torch.cuda.current_device())
print('CUDA device: ', torch.cuda.device(0))
print('CUDA device count: ',torch.cuda.device_count())
print('CUDA device name: ', torch.cuda.get_device_name(0))
