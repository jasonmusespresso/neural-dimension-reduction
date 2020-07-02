# learning rate test
from main import main

kwargs_list1 = [
    {'input-size': 90000, 'test-size': 1000, 'hidden-dims': [512, 512, 256, 256, 256, 128, 128, 128, 64, 64, 64, 32, 32, 20, 20], 'output-dimension': 10, 'lambda': 1,
     'epochs': 40,
     'to_plot': True, 'learning_rate': 1e-3, 'momentum': .9, 'data': 'artificial3_10_200',
     'filename_prefix': 'lr_1e-3_2*512_3*256_3*128_3*64_2*32_2*20'}
    ]
main(kwargs_list1)



kwargs_list1 = [
    {'input-size': 90000, 'test-size': 1000, 'hidden-dims': [512, 512, 256, 256, 256, 128, 128, 128, 64, 64, 64, 32, 32, 20, 20], 'output-dimension': 10, 'lambda': 1,
     'epochs': 40,
     'to_plot': True, 'learning_rate': 2e-3, 'momentum': .9, 'data': 'artificial3_10_200',
     'filename_prefix': 'lr_2e-3_2*512_3*256_3*128_3*64_2*32_2*20'}
    ]
main(kwargs_list1)

kwargs_list1 = [
    {'input-size': 90000, 'test-size': 1000, 'hidden-dims': [512, 512, 256, 256, 256, 128, 128, 128, 64, 64, 64, 32, 32, 20, 20], 'output-dimension': 10, 'lambda': 1,
     'epochs': 40,
     'to_plot': True, 'learning_rate': 4e-3, 'momentum': .9, 'data': 'artificial3_10_200',
     'filename_prefix': 'lr_4e-3_2*512_3*256_3*128_3*64_2*32_2*20'}
    ]
main(kwargs_list1)

kwargs_list1 = [
    {'input-size': 90000, 'test-size': 1000, 'hidden-dims': [512, 512, 256, 256, 256, 128, 128, 128, 64, 64, 64, 32, 32, 20, 20], 'output-dimension': 10, 'lambda': 1,
     'epochs': 40,
     'to_plot': True, 'learning_rate': 8e-3, 'momentum': .9, 'data': 'artificial3_10_200',
     'filename_prefix': 'lr_8e-3_2*512_3*256_3*128_3*64_2*32_2*20'}
    ]
main(kwargs_list1)