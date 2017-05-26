# Simulation experiments from the data we collected on CTRs of ads
# reference: http://www.marketingdistillery.com/2014/09/24/bayesian-modeling-of-click-through-rate-for-small-data/
### BAYESIAN SIMULATION
beta <- function(mu, v) {
  # return beta distribution for an ad
  # mu is the mean CTR for the ad
  # v is the sample size of the ad
  alpha <- mu*v
  beta <- (1-mu)*v
  
  # pritn variance in CTR
  cat('variance in CTR = ', variance_in_ctr <- mu*(1-mu)/v)
  
  # plot it
  s <- seq(0, 5*mu, 0.1*mu)
  plot(100*s, dbeta(s, alpha, beta), type="l", ylab="Density", xlab = "CTR (%)")
}

# plot the CTR distribution of an ad
beta(0.0037, 2155)


