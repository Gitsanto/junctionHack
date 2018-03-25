from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from poop.models import dataset
from poop.forms import upload_dataset

def index(request):
    if request.method == 'POST':
        image_form = upload_dataset(data=request.POST)
        if image_form.is_valid:
            imageform = image_form.save(commit=False)

            if 'dataset_image' in request.FILES:
                imageform.dataset_image = request.FILES['dataset_image']
                imageform.save()
        else:
            print(image_form.errors)
    else:
        image_form = upload_dataset()
    imagelink = dataset.objects.order_by('-pk')[0]



    context_dic = {'imageform':image_form, 'links':imagelink}


    return render (request, 'poop/index.html', context_dic)



def predictcoin(request):
    imagelink = dataset.objects.order_by('-pk')[0]

    import numpy as np
    from keras.models import load_model
    nogo = load_model('/home/hosei/python35/EmekaProjects/junctionhack/junction/tokenIdentifier.h5')

    # Part 3 - Making new predictions
    import numpy as np
    from keras.preprocessing import image
    test_image = image.load_img(imagelink.dataset_image, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = nogo.predict(test_image)
    #training_set.class_indices
    if result[0][0] == 1:
        prediction = 'one-yen'
    elif result[0][1] == 1:
        prediction = 'ten-yen'
    elif result[0][2] == 1:
        prediction = 'hundred-yen'
    elif result[0][3] == 1:
        prediction = 'five-yen'
    elif result[0][4] == 1:
        prediction = 'fifty-yen'

    context_dic = {'links':imagelink, 'pred':prediction}
    context_dic = {'link':imagelink}

    return render(request, 'poop/prediction.html', context_dic)
