# Adapted from the code of Stephen Marsland
# http://www-ist.massey.ac.nz/smarsland/Code/2/pcn.py
import numpy as np

def add_bias_node(inputs):
    bias_node = -np.ones(len(inputs))
    return np.column_stack((inputs, bias_node))

class Perceptron(object):
    """
    A basic Perceptron

    Parameters
    ----------
    eta : float
        The learning rate of the network. Should be between
        0 and 1.
    """

    def __init__(self, eta):
        self.eta = eta

    def _initialize(self, inputs, targets):
        inputs = np.asarray(inputs)
        # gets set to 2d in _add_bias_node

        targets = np.asarray(targets)
        if targets.ndim == 1:
            targets = targets[:, None]

        self.targets = targets
        self.inputs = inputs

        # Set up network size
        self.m = inputs.shape[1]

        # Set up targets size
        self.n = targets.shape[1]

        # number of observations
        self.nobs = inputs.shape[0]

        # Initialise network weights plus 1 for bias node
        self._init_weights()

    def _init_weights(self):
        self.weights = np.random.rand(self.m+1, self.n)*0.1-0.05

    def fit(self, inputs, targets, max_iter):
        """
        Trains the network.

        Parameters
        ----------
        inputs : array-like
            The inputs data
        targets : array-like
            The targets to train on
        max_iter : int
            The number of iterations to perform
        """
        self._initialize(inputs, targets)
        inputs = self.inputs
        targets = self.targets
        weights = self.weights
        eta = self.eta

        # Add the inputs that match the bias node
        inputs = add_bias_node(inputs)
        # Training
        change = range(self.nobs)

        for n in range(max_iter):
            outputs = self.predict(inputs, weights, add_bias=False)
            weights += eta * np.dot(inputs.T, targets - outputs)

            # Randomize order of inputs
            np.random.shuffle(change)
            inputs = inputs[change, :]
            targets = targets[change, :]

        self.weights = weights

    def predict(self, inputs=None, weights=None, add_bias=True):
        """ Run the network forward """
        if weights is None:
            try:
                weights = self.weights
            except:
                raise ValueError("fit the classifier first "
                                 "or give weights")
        if inputs is None:
            inputs = self.inputs
        if add_bias:
            inputs = add_bias_node(inputs)

        outputs = np.dot(inputs, weights)

        # Threshold the outputs
        return np.where(outputs>0, 1, 0)


    def confusion_matrix(self, inputs, targets, weights, summary=True):
        """
        Confusion matrix

        If summary is True, returns percent correct, else returns
        the whole confusion matrix.
        """
        inputs = np.asarray(inputs)
        targets = np.asarray(targets)

        # Add the inputs that attach the bias node
        inputs = add_bias_node(inputs)

        outputs = np.dot(inputs, weights)

        n_classes = targets.ndim == 1 and 1 or targets.shape[1]

        if n_classes == 1:
            n_classes = 2
            outputs = np.where(outputs > 0, 1, 0)
        else:
            # 1-of-N encoding
            outputs = np.argmax(outputs, 1)
            targets = np.argmax(targets, 1)

        outputs = np.squeeze(outputs)
        targets = np.squeeze(targets)

        cm = np.histogram2d(targets, outputs, bins=n_classes)[0]
        if not summary:
            return cm
        else:
            return np.trace(cm)/np.sum(cm)*100
