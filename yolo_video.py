import argparse
import os
from yolo_nodraw import YOLO
from PIL import Image


def detect_img(yolo, score):
    file = open('prediction_' + str(score) + '.txt', 'w')
    index = 0
    directory = 'challenge2018_test'
    for img in os.listdir(directory):
        # img = "15455953700_7e53b8f53e_o.jpg"
        try:
            image = Image.open(directory + '/' + img)
        except:
            print('Open Error! Try again!')
            continue
        yolo.detect_image(image, img[:-4], file)
        index += 1
        if index % 50 == 0:
            print(index)
    # while True:
    #     img = input('Input image filename:')
    #     try:
    #         image = Image.open("img/15455953700_7e53b8f53e_o.jpg")
    #     except:
    #         print('Open Error! Try again!')
    #         continue
    #     else:
    #         r_image = yolo.detect_image(image)
    #         r_image.show()
    yolo.close_session()


FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model_path', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors_path', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes_path', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--score', type=float,
        help='path to score threshold, default '
    )

    parser.add_argument(
        '--iou_all_classes', type=float,
        help='path to score threshold, default '
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str, required=False, default='./path2your_video',
        help="Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help="[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)), FLAGS.score)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
