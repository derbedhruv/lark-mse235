# Simulation experiments from the data we collected on CTRs of ads
# reference: http://www.marketingdistillery.com/2014/09/24/bayesian-modeling-of-click-through-rate-for-small-data/
### BAYESIAN SIMULATION
ad.stats <- function(mu, v, error=5) {
  # return beta distribution for an ad
  # mu is the mean CTR for the ad
  # v is the sample size of the ad
  # 'error' is the (percentage) chance of error used to estimate the confidence intervals
  alpha <- mu*v  # also, no of clicks
  beta <- (1-mu)*v
  
  # print variance in CTR
  # cat('variance in CTR = ', variance_in_ctr <- mu*(1-mu)/v)
  
  # print the upper and lower bound of CTR
  # http://www.marketingdistillery.com/2015/02/08/how-to-calculate-confidence-intervals-for-conversion-rate/
  ctr.lower <- 0  # if CTR == 0%
  if (mu != 0) {
    ctr.lower <- qbeta(0.01*error, alpha, v-alpha+1)   # beta inverse cumulative distribution, see https://stackoverflow.com/questions/10151888/what-is-the-equivalent-r-function-to-gamma-invprobability-alpha-beta-excel-fun
  }
  ctr.upper <- 1  # if CTR == 100%
  if (alpha != v) {
    ctr.upper <- qbeta(1-0.01*error/2, alpha+1, v-alpha)
  }
  cat('CTR lies between', 100*ctr.lower, '% and', 100*ctr.upper, '%\n')
  
  # plot it - only the section that 'makes sense'
  # using min(5 times the CTR or 1) - i.e. if the CTR is high enough, just plot in range [0,1]
  s <- seq(0, min(5*mu,1), min(0.1*mu, 0.01))
  plot(100*s, dbeta(s, alpha, beta), type="l", ylab="Density", xlab = "CTR (%)")
}

# plot the CTR distribution of an ad
ad.stats(0.0037, 2182)
ad.stats(0.0053, 1130)


