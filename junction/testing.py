import numpy as np
from keras.models import load_model
nogo = load_model('tokenIdentifier.h5')

# Part 3 - Making new predictions
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('demo/100.JPG', target_size = (64, 64))
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

print(prediction)
