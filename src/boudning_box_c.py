import numpy as np
import cv2


def get_bounding_box_character(input_img):
    
    img = np.array(input_img)
    horz_hist = img.shape[1] -np.sum(img, axis=1,keepdims=True)/255
    depth_list =[]
    for y, depth in enumerate(horz_hist):
        depth= 64-depth
        if depth>0:
            depth_list.append(y)
        # print(depth)


    depth_list2 = []
    vert_hist = np.sum(img, axis=0)/255
    for x, depth2 in enumerate(vert_hist):
        # depth2 = 64-depth2
        if depth2>0 and x>0:
            depth_list2.append(x)
        # print(depth2)
    try:
        max_x = max(depth_list)
        min_x = min(depth_list)

        max_y = max(depth_list2)
        min_y = min(depth_list2)
    except:
        return []
    # print([min_y, min_x, max_y, max_x])
    return [min_y, min_x, max_y, max_x]

