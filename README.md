# 481-P2

The aim of this project is to test the efficacy of several neural network architectures, optimized using gradient descent. The architectures to be tested are:
1.	Multioutput perceptron, with varying learning rates.
2.	Deep neural network, with varying depth.
3.	Deep neural network, with varying learning rates.

3-fold cross-validation will be used to select the optimal hyperparameter for each model, which will be used to train an optimal model for each architecture to see the effectiveness of each.

The data that the models will be trained on is of handwritten digits, where each pixel is represented with a 0 (black) or a 1 (white), where the dimensions of each image is 32 x 32. All data used for training and testing is stored in the ‘data/’ directory.

The implementations for neural network classes and utilities were all provided by Professor Luis E. Ortiz in the file ‘src/learn_nnet.ipynb’, with the implementations for this project added at the end of the same file.
