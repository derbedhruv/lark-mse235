# Simulation experiments from the data we collected on CTRs of ads
# reference: http://www.marketingdistillery.com/2014/09/24/bayesian-modeling-of-click-through-rate-for-small-data/
### BAYESIAN SIMULATION
ad_stats <- function(mu, v) {
  # return beta distribution for an ad
  # mu is the mean CTR for the ad
  # v is the sample size of the ad
  alpha <- mu*v
  beta <- (1-mu)*v
  
  # print variance in CTR
  cat('variance in CTR = ', variance_in_ctr <- mu*(1-mu)/v)
  
  # print the upper and lower bound of CTR
  
  
  # plot it - only the section that 'makes sense'
  # using min(5 times the CTR or 1) - i.e. if the CTR is high enough, just plot in range [0,1]
  s <- seq(0, min(5*mu,1), min(0.1*mu, 0.01))
  plot(100*s, dbeta(s, alpha, beta), type="l", ylab="Density", xlab = "CTR (%)")
}

# plot the CTR distribution of an ad
ad_stats(0.0037, 2155)


