from __future__ import print_function
import os, time
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
from upscaler_django_backend.upscale_models.DWSR.netx2 import model
import cv2
import pywt as pw
import ntpath

TEST_EXPERIMENT = True
MODEL_PATH = 'upscaler_django_backend/upscale_models/DWSR/Weightx2/x2.ckpt'
WV = 'db1'


def process_image(input_image_path, output_dir):

    test_input = tf.placeholder(np.float32)
    # Feeding Forward
    test_output, _, _ = model(test_input)
    with tf.Session(config=tf.ConfigProto()) as sess:
        tf.initialize_all_variables().run()
        saver = tf.train.Saver(tf.all_variables())

        saver.restore(sess, MODEL_PATH)

        print('Processing Image %s' % ntpath.basename(input_image_path))
        testBBImg = cv2.imread(input_image_path, 0)
        tcoeffs = pw.dwt2(testBBImg, WV)
        tcA, (tcH, tcV, tcD) = tcoeffs
        tcA = tcA.astype(np.float32) / 255
        tcH = tcH.astype(np.float32) / 255
        tcV = tcV.astype(np.float32) / 255
        tcD = tcD.astype(np.float32) / 255
        test_temp = np.array([tcA, tcH, tcV, tcD])
        test_elem = np.rollaxis(test_temp, 0, 3)
        test_data = test_elem[np.newaxis, ...]
        start_time = time.time()
        output_data = sess.run([test_output], feed_dict={test_input: test_data})
        duration = time.time() - start_time
        dcA = output_data[0][0, :, :, 0]
        dcH = output_data[0][0, :, :, 1]
        dcV = output_data[0][0, :, :, 2]
        dcD = output_data[0][0, :, :, 3]
        srcoeffs = (dcA * 255 + tcA * 255,
                    (dcH * 255 + tcH * 255,
                        dcV * 255 + tcV * 255,
                        dcD * 255 + tcD * 255))
        sr_img = pw.idwt2(srcoeffs, WV)

        output_image_path = os.path.join(output_dir, ntpath.basename(input_image_path))
        cv2.imwrite(output_image_path, sr_img)
        print('Processed image saved to %s, processing time: %s' % (output_image_path, str(duration)))
        
        sess.close()
