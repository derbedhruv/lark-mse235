setwd(dirname(sys.frame(1)$ofile))  # set wd to that of this file

solera <- read.csv('solera_eligibility.csv')
reg <- read.csv('registered_solera_users.csv')

# sanity check: find any users that are in the registered group but not in the Solera list
missing.user <- setdiff(reg$solera_id, solera$Solera.ID)

# Add age column
solera$Age <- apply(as.array(as.character(solera$Birthdate)), 1, function(x) {return(floor(as.numeric(Sys.Date() - as.Date(x, "%Y%m%d"))/365))})

## Plot the zipcodes on the US map
# load zipcode package
library(zipcode)
library(ggplot2)
library(ggmap)
data("zipcode")

dat <- merge(solera, zipcode, by.x = 'Zip_Code', by.y = 'zip')
# map(database = 'state')
# ggplot(data=dat) + geom_point(aes(x=longitude, y=latitude, colour=state))

# plotting on the US map - use plot(g) to see this
g <- ggmap(get_map(location = 'USA', zoom = 4, maptype='roadmap', color='bw')) + geom_point(data=dat, aes(x=longitude, y=latitude, colour=state)) 

# localizing only to California
cal1 <- dat[dat$State == 'CA', c('Zip_Code', 'latitude', 'longitude')]
cal1$Zip_Code <- as.character(cal1$Zip_Code)  # convert to character so that table() will work - if you let it remain a factor then extra factors in dat which aren't in cal1 will also be counted (with frequency 0)
cal2 <- data.frame(table(cal1$Zip_Code))
colnames(cal2) <- c('Zip_Code', 'Frequency')

# merge them - TODO left inner join
cal <- merge(cal2, cal1, by.x='Var1', by.y = 'Zip_Code', all.y = F, all.x = T)
cal$Frequency <- as.factor(cal$Frequency) # convert frequency to a factor so that the plot may show it as discrete

# plot on California map
gcal <- ggmap(get_map(location = 'california', zoom = 6, maptype='roadmap', color='bw')) + geom_point(data=cal, aes(x=longitude, y=latitude, colour=Frequency)) 
plot(gcal)


