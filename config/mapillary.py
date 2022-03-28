class mapillary_config(object):
    weight = [ 3.03871497 , 13.01999212, 4.53008444 , 38.00898985, 35.35990217,
                31.14247824, 45.82106668, 39.44451896, 6.00002668 , 32.64759009,
                17.34725897, 31.45715227, 47.0853521 , 11.70166965, 44.50966853,
                44.80501487, 45.63057065, 48.21080448, 41.21912833] # changed weights to weight to make it one
    weights= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ignore_index=255
    num_classes = 19
    color_classes = [
        ('road', (128, 64, 128), 0),
        ('sidewalk', (244, 35, 232), 8),
        ('building', (70, 70, 70), 1),
        ('wall', (102, 102, 156), 11),
        ('fence', (190, 153, 153), 2),
        ('pole', (153, 153, 153), 5),
        ('traffic_light', (250, 170, 30), 18),
        ('traffic_sign', (128, 128, 128), 12),
        ('vegetation', (107, 142, 35), 9),
        ('terrain', (152, 251, 152), 22),
        ('sky', (70, 130, 180), 13),
        ('person', (220, 20, 60), 4),
        ('rider', (220, 0, 0), 4),
        ('car', (0, 0, 142), 10),
        ('truck', (0, 0, 70), 10),
        ('bus', (0, 60, 100), 10),
        ('train', (0, 0, 142), 10),
        ('motorcycle', (0, 0, 230), 10),
        ('bicycle', (119, 11, 32), 10),
        ('void', (32, 32, 32), ignore_index)
    ] 

    swnet_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-swnet-R18.pt'
    bsnet_weight_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/cityscapes-bisenet-R18.pth'
    bisenet_resume_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/gsvnet_bisenet_r18.tar'
    swnet_resume_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/gsvnet_swnet_r18.tar'
    optical_flow_network_path = '/gpfs1/home/2018015/vprade01/repos/GSVNet/weights/flownet.pth.tar'
    data_path = '/gpfs1/dlocal/home/2018015/PARTAGE/dataset/mapillary/' # put your data path here
