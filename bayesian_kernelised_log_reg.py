import numpy as np
from scipy.optimize import fmin_l_bfgs_b

#------------------------- Helper functions for logistic --------------------------#


def sigmoid(X):
    return 1. / ( 1 + np.exp(-X))


def cost_grad(X,Y,w,alpha):
    '''
    Calculates cost and gradient for logistic regression
    
    X: numpy matrix of size 'n x m'
       Matrix of explanatory variables       
       
    Y: numpy vector of size 'n x 1'
       Vector of dependent variables
       
    w: numpy array of size 'm x 1'
    '''
    Xw    = np.dot(X,w)
    s     = sigmoid(Xw)
    cost  =  - np.log(s)*Y - np.log(1 - s)*(1 - Y) + alpha*np.dot(w,w) / 2
    grad  = np.dot(X.T, s - Y) + alpha*w
    return [cost,grad]
    
    
#--------------------------- Bayesian Logistic Regression ------------------------#
    

class BayesianLogisticRegression(object):
    '''
    Implements Bayesian Logistic Regression with type II maximum likelihood, uses
    Gaussian (Laplace) method for approximation of evidence function.
    
    Parameters:
    -----------
    X: numpy matrix of size 'n x m'
       Matrix of explanatory variables       
       
    Y: numpy vector of size 'n x 1'
       Vector of dependent variables
       
    evidence_max_method: str (either 'fixed-point' or 'EM')
       Optimization method used for evidence maximization
    
    max_iter_evidence_max: float 
       Maximum number of iterations for maximizing marginal likelihood
       
    max_iter_irls: float
       Maximum number of iterations for minimizing cost function of logistic
       regression (in its regularised version)
    
    conv_thresh_evidence: float 
       convergence threshold for evidence maximization procedure
       
    conv_thresh_irls: float
       convergence threshold for irls
       
    w_init: numpy array of size 'm x 1' (DEFAULT = None)
       Initial guess on parameters, if not defined then random guess
       
    alpha_init: float (DEFAULT = None)
       Initial guess on precision parameter of prior, if not defined random guess
       
    '''
    
    
    def __init__(self,X,Y,evidence_max_method = "fixed-point", max_iter_evidence_max = 100,
                                                               max_iter_irls         = 20,
                                                               w_init                = None,
                                                               conv_thresh_evidence  = 1e-3,
                                                               conv_thresh_irls      = 1e-3,
                                                               alpha_init            = None):
        self.X = X
        # all classes in Y
        classes = set(Y)
        # check that there are only two classes in vector Y
        assert len(classes)==2,"Number of classes in dependent variable should be 2"
        # convert dependent variable to 0 1 vector
        
        assert evidence_max_method in ['fixed-point','EM'], 'Can be either "fixed-point" or "EM"'
        self.evidence_max_method    = evidence_max_method
        self.max_iter_evidence      = max_iter_evidence
        self.max_iter_irls          = max_iter_irls
        self.conv_thresh_evidence   = conv_thresh_evidence
        self.conv_thresh_irls       = conv_thresh_irls
        if w_init is None:
           self.w_init              = np.random.random()
           self.alpha_init          = np.random.random()
           
        # dimensionality of input 
        self.m                      = self.X.shape[1]
        
        
    def fit(self):
        '''
        Fits Bayesian Logistic Regression with Laplace approximation 
        '''
        self._evidence_maximize()
        
        
    def predict_prob(self,X):
        '''
        Predicts probability of observation being of particular class
        
        Parameters:
        -----------
        
        X: numpy array of size 'unknown x m'
           Matrix of explanatory variables test data
           
        Returns:
        --------
        
        P: numpy array of size 'unknown x 1'
           Matrix of probabilities
        '''
        
    

    def _irls(self, X, Y, alpha, Theta):
        '''
        Iteratively refitted least squares method using l_bfgs_b.
        Finds MAP estimates for weights and Hessian at convergence point
        
        Returns:
        --------
        
        [Wmap,negHessian]: list of two numpy arrays
              
              Wmap: numpy array of size 'm x 1'
                    Mode of posterior distribution (mean for Gaussian approx.)
                    
              negHessian: numpy array of size 'm x m'
                    Covariance of Gaussian (Laplace) approximation
        '''
        # calculate solution using version of Newton-Raphson
        f          = lambda w: cost_grad(X,Y,w,alpha)
        Wmap       = fmin_l_bfgs_b(f, x0 = Theta, pgtol   = self.conv_thresh_irls,
                                                  maxiter = self.max_iter_irls)
        
        # calculate negative of Hessian at w = Wmap
        s          = sigmoid(np.dot(X,Wmap))
        R          = s * (1 - s)
        negHessian = np.dot(X.T*R,X)
        negHessian.fill_diagonal(np.diag(negHessian + alpha))
        u,d,vt     = np.linalg.svd(negHessian,full_matrices = False)
        return [Wmap, negHessian, u, d, vt]
        
        
    def _evidence_maximize(self):
        '''
        Maximize evidence (type II maximum likelihood) 
        '''
        # initial guess on paramters
        alpha_old    = self.alpha_init
        Wmap_old     = self.w_init
        evid_old     = np.NINF
                
        # evidence maximization
        for i in range(self.max_iter_evidence):
            
            # find mean & covariance of Laplace approximation to posterior
            Wmap, A, u, d, vt = self._irls(self.X, self.Y, alpha_old, Wmap_old)            
            mu_sq             = np.dot(Wmap,Wmap) 
            
            # use EM or fixed-point procedures to update parameters            
            if self.evidence_max_method == "EM":
                alpha = self.m / (mu_sq + np.sum(d)) 
            else:
                gamma = np.sum((d - alpha) / d)
                alpha = gamma / mu_sq
                
            # calculate value of type II maximum likelihood
            evid = self._evidence_value(d,alpha,Wmap)
            
            # check termination conditions, if true write optimal values of 
            # parameters to instance variables
            if evid - evid_old < self.conv_thresh_evidence or i==self.max_iter_evidence - 1:
                self.alpha = alpha
                self.Wmap  = Wmap
                self.A     = A
                return 
            
            evid_old  = evid
            Wmap_old  = Wmap

            
            
    def _evidence_value(self,d,alpha,Wmap):
        '''
        Calculates value of evidence (type II likelihood)
        
        Parameters:
        -----------
        
        d: numpy array of size m
           
        '''
        Likelihood_Wmap = -1*cost_grad(self.X, self.Y, Wmap, alpha)
        Prior_Wmap      = self.m/2 * np.log(alpha) - alpha / 2 * np.dot(Wmap,Wmap)
        Z_normaliser    = 0.5*self.m*np.log(np.pi) - 0.5*np.log(np.sum(d))
        ED              = Likelihood_Wmap + Prior_Wmap + Z_normaliser
        return ED
            
        
        
if __name__ == "__main__":
    X
    