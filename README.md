## Bayesian Machine Learning Algorithms with scikit-learn api


### Installing & Upgrading package

    pip install https://github.com/AmazaspShumik/sklearn_bayes/archive/master.zip
    pip install --upgrade https://github.com/AmazaspShumik/sklearn_bayes/archive/master.zip

   
### Algorithms
 
* [Linear Models](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/linear_models)
     * Empirical Bayes Linear Regression [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/linear_models/bayes_linear.py)
     * Empirical Bayes Logistic Regression (uses Laplace Approximation)  [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/linear_models/bayes_logistic.py)
     * Variational Bayes Linear Regression  [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/linear_models/bayes_linear.py)
     * Variational Bayes Logististic Regression (uses Jordan local variational bound) [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/linear_models/bayes_logistic.py)
* [Decomposition Models](https://github.com/AmazaspShumik/sklearn-bayes/tree/master/skbayes/decomposition_models)
     * Latent Dirichlet Allocation (collapsed Gibbs Sampler) [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/decomposition_models/gibbs_lda_cython.pyx), [tutorial](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/ipython_notebooks_tutorials/decomposition_models/example_lda.ipynb)
     * Restricted Boltzmann Machines (PCD-k / CD-k, weight decay, adaptive learning rate) [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/decomposition_models/rbm.py), [tutorial](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/ipython_notebooks_tutorials/decomposition_models/rbm_demo.ipynb)
* [ARD Models](https://github.com/AmazaspShumik/sklearn-bayes/tree/master/skbayes/rvm_ard_models)
     * Relevance Vector Regression (version 2.0) [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/rvm_ard_models/fast_rvm.py)
     * Relevance Vector Classifier (version 2.0) [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/rvm_ard_models/fast_rvm.py)
     * Type II Maximum Likelihood ARD Linear Regression  [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/rvm_ard_models/fast_rvm.py)
     * Type II Maximum Likelihood ARD Logistic Regression  [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/rvm_ard_models/fast_rvm.py)
     * Variational Relevance Vector Regression [code](https://github.com/AmazaspShumik/sklearn_bayes/blob/master/skbayes/rvm_ard_models/vrvm.py)
     * Variational Relevance Vector Classification [code](https://github.com/AmazaspShumik/sklearn_bayes/blob/master/skbayes/rvm_ard_models/vrvm.py), [tutorial](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/ipython_notebooks_tutorials/rvm_ard/vbard_classification.ipynb)
* [Mixture Models](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/mixture_models)
     * Variational Bayes Gaussian Mixture Model with Automatic Model Selection [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/mixture_models/mixture.py), [tutorial](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/ipython_notebooks_tutorials/mixture_models/example_gaussian_mixture_with_ard.ipynb)
     * Variational Bayes Bernoulli Mixture Model [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/mixture_models/mixture.py), [tutorial](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/ipython_notebooks_tutorials/mixture_models/example_bernoulli_mixture.ipynb)
     * Variational Multinoulli Mixture Model [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/mixture_models/mixture.py)
* [Hidden Markov Models](https://github.com/AmazaspShumik/sklearn-bayes/tree/master/skbayes/hidden_markov_models)
     * Variational Bayes Poisson Hidden Markov Model [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/hidden_markov_models/hmm.py), [demo](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/ipython_notebooks_tutorials/hidden_markov_models/examples_hmm.ipynb)
     * Variational Bayes Bernoulli Hidden Markov Model [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/hidden_markov_models/hmm.py)
     * Variational Bayes Gaussian Hidden Markov Model [code](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/skbayes/hidden_markov_models/hmm.py), [demo](https://github.com/AmazaspShumik/sklearn-bayes/blob/master/ipython_notebooks_tutorials/hidden_markov_models/examples_hmm.ipynb)

### Contributions:

There are several ways to contribute (and all are welcomed)

     * improve quality of existing code (find bugs, suggest optimization, etc.)
     * implement machine learning algorithm (it should be bayesian; you should also provide examples & notebooks)
     * implement new ipython notebooks with examples 


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/AmazaspShumik/sklearn_bayes/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

