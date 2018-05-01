# Open Source Analysis

## Team Members

- Andrew Casner - *B.S. Computer Science*
- Oliver Collins - *B.A. Computer Science*
- Carl Cortright - *B.S. Computer Science*
- Shubha Swamy - *B.S. Computer Science*

## Description

Over time, the most popular programming languages have shifted dramatically. There have been trends with the rise and fall of different programming languages over time. However, it can often be quite difficult to predict these fluctuations. So for this project, we have decided to dive into a large open-source dataset that looks into contributions to open-source software and try to map what we hope, will be an accurate representation of these trends. Acquired from [libraries.io](https://libraries.io/data), this dataset with over 397+ million rows, provides us with repository names, timestamps, programming languages, and many more attributes related to open source projects on the internet.

Our primary goal of this project is to gain insights about open source software. We will accomplish this goal by mining data from a dataset about open source projects. We will focus our work on four main areas: tracking trends in programming languages, analyzing how popular repositories have changed over time, how contributions to those repositories have changed over time, and also monitoring repository life cycles. We will use various data minining techniques and tools in order to accomplish this goal. More information about this process can be found in our [final paper](https://carlcortright.github.io/OpenSourceMiners/website/assets/pdf/Final_Paper.pdf).

## Questions and Answers

#### The primary *questions* we will consider during the duration of this project will focus on analyzing trends in open source projects.

1. **What insights can we gain to improve the open source community further?**
   - As we use numerous different techniques to mine the data throughout the project, we hope to gain more information about the various languages used, the contributions to popular repositories, and the trends in dependencies which rely on those open source projects.
2. **How can we identify areas in the open source community that need improvement?**
   - This question will help us understand the missing gaps in the open source community. To find answers to this question, we will analyze trends in contributions and repositories to figure out areas of improvement within the open source community.
3. **Can we predict upcoming popular repositories?**
   - We hope to answer this question using all the information from the mined data. We would like to predict upcoming popular repositories based on all the insights we gain from the data analysis we will perform. Answering this question will be beneficial to understand the open source community.

#### Through various data mining tools and techniques we used, we were able to gain *answers* to the questions defined above. 

- The use of clustering was essential to answering our core question: identifying areas in the open source community that need improvement. To try to find deficiencies in the open source community we clustered repositories, and from there we could identify clusters that are “lacking” and can benefit from further community involvement. We implemented a K-Means clustering algorithm on the dataset. The below diagram is an example of using the center of each K-Means cluster to determine the average number of Open Issues/ Contributors. Through an extensive process similar to this, we were able to identify 17 different repositories in need of the most community assistance. 

  <img src="https://i.imgur.com/QfEkdyL.png" width="400">

- We also used similar techniques as described above to predict upcoming popular repositories. We found that 348 repositories have the potential to be very large and heavily contributed to in the future. And due to the scope of this course, we understand that this may not be the best way to predict trends and future growth, but we are still extremely proud of the “predictions” our team executed. The below graph is one of the examples of how contributions using JavaScript have changed over time. 

<img src="https://i.imgur.com/qKgMXOZ.png" width="400">

- Through all our data mining process, we were able to gain valuable insight into the open source community. With the use of techniques and tools that facilitated the data mining process, we were able to understand trends and patterns in open source development. In addition to the conclusions and predictions described above, we were further able to understand the open source community in various aspects. The below graph is an example of one of the behaviors we observed in open source repositories. As shown below, the stars count and forks count on every individual repository are highly correlated.

<img src="https://i.imgur.com/kXIpkuf.png" width="400">



You can find more detail about the process we used to reach our conclusions in our [final paper](https://carlcortright.github.io/OpenSourceMiners/website/assets/pdf/Final_Paper.pdf).

## Application

In our application, we focus on how our conclusions will help us make better and more useful decisions regarding open source projects. Open source projects play a significant role in the development of software, and tens of thousands of open source projects run worldwide, with millions of users relying on the software. Concluding applications based on our data analysis will help us better understand open source software that influences millions across the world.

Through our cluster analysis, we were able to identify that “Stars/Contributors,” “Stars/Forks,” and “Forks/Issues” were the best indicators of future growth and popularity of a repository. These relationships will help developers working in open source software a general direction to work towards when creating new software. Furthermore, understanding the “Fork/Issue” ratio shows tremendous potential in future heavy traffic and contributions. Also by analyzing time-series of different programming languages, we can display numerous attributes that can not only be applied open source software developers but general coders. Identifying that repositories using Python or Java are currently experiencing very high contributions, and showing how trends between dying and popular programming languages can help prove the likelihood of these languages dying out soon or continuing to prosper.

## Video Demonstration

In our final report, we discuss the technical aspects of data mining and what our team accomplished through the extraction and analysis of our dataset. Also, we have also created a short video demoing our results and conclusions. You can find our video [here](https://youtu.be/WWND0ApVp94).

## Final Paper

The final paper can be found [here](https://carlcortright.github.io/OpenSourceMiners/website/assets/pdf/Final_Paper.pdf).

## Website

We have created a website which allows others to learn more about our project and interact with a force graph to better understand relationships about the conclusion we've made [here](https://carlcortright.github.io/OpenSourceMiners/website/index.html). 

![Alt Text](http://g.recordit.co/dkmiLcpaGK.gif)
