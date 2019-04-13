from mnist import MNIST

mndata = MNIST('../numbers.jpg')
images, labels = mndata.load_training()