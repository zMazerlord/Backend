from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import numpy as np
import cv2


def home_page(request):
    global file_url
    print(request.POST)
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)


        def loading_displaying_saving():
            image = cv2.imread(r'file_url', cv2.IMREAD_COLOR)
            print(image)
            image_revers = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return image_revers



        def comparison():
            img = loading_displaying_saving()
            black = [0, 0, 0]
            result_black = np.count_nonzero(np.all(img == black, axis=2))
            white = [255, 255, 255]
            result_white = np.count_nonzero(np.all(img == white, axis=2))
            if result_black > result_white:
                print('Чёрных больше')
            else:
                print('Белых больше')

        def hex2rgb(val):
            val = val.lstrip('#')
            lv = len(val)
            return tuple(int(val[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

        def find_pixels(val):
            img = loading_displaying_saving()
            rgb = hex2rgb(val)
            result_rgb = np.count_nonzero(np.all(img == rgb, axis=2))
            print(result_rgb)

        return render(request, 'home_page.html', {
           'find': find_pixels(request.POST.get('name_field')),
            'comparision': comparison(),
            })
    return render(request, 'home_page.html')
