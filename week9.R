dataframe15 <- read.table("15mer_out.histo") #load the data into dataframe15
plot(dataframe15[1:200,], type="l") #plots the data points 1 through 200 in the dataframe15 using a line
plot(dataframe15[2:100,], type="l") #plot line graph 
points(dataframe15[2:100,]) #plot the data points from 2 through 100
sum(as.numeric(dataframe15[2:2904,1]*dataframe15[2:2904,2]))/39
(sum(as.numeric(dataframe15[2:98,1]*dataframe15[2:98,2]))) / sum(as.numeric(dataframe15[2:2904,1]*dataframe15[2:2904,2]))/39

dataframe17 <- read.table("17mer_out.histo") #load the data into dataframe17
plot(dataframe17[1:200,], type="l") #plots the data points 1 through 200 in the dataframe17 using a line
plot(dataframe17[2:100,], type="l") #plot line graph 
points(dataframe17[2:100,]) #plot the data points from 2 through 100
sum(as.numeric(dataframe17[2:2715,1]*dataframe17[2:2715,2]))/38
(sum(as.numeric(dataframe17[2:80,1]*dataframe15[2:80,2]))) / sum(as.numeric(dataframe17[2:2715,1]*dataframe17[2:2715,2]))/38

dataframe19 <- read.table("19mer_out.histo") #load the data into dataframe19
plot(dataframe19[1:200,], type="l") #plots the data points 1 through 200 in the dataframe19 using a line
plot(dataframe19[2:100,], type="l") #plot line graph 
points(dataframe19[2:100,]) #plot the data points from 2 through 100
sum(as.numeric(dataframe19[2:2613,1]*dataframe19[2:2613,2]))/37
(sum(as.numeric(dataframe19[2:73,1]*dataframe19[2:73,2]))) / sum(as.numeric(dataframe19[2:2613,1]*dataframe19[2:2613,2]))/37

dataframe21 <- read.table("21mer_out.histo") #load the data into dataframe21
plot(dataframe21[1:200,], type="l") #plots the data points 1 through 200 in the dataframe21 using a line
plot(dataframe21[2:100,], type="l") #plot line graph 
points(dataframe21[2:100,]) #plot the data points from 2 through 100
sum(as.numeric(dataframe21[2:2503,1]*dataframe21[2:2503,2]))/36
(sum(as.numeric(dataframe21[2:71,1]*dataframe21[2:71,2]))) / sum(as.numeric(dataframe21[2:2503,1]*dataframe21[2:2503,2]))/36
