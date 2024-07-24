# Social Media And Its Brain Chemistry Altering Effects

## Resources
Dataset used: [Social Media Usage and Emotional Well-Being](https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being?select=val.csv)

Programs utilized: Pandas, Numpy, Matplotlib, Plotly Express, os, Scipy.Stats

# Motivations and Data
The inital motivation was to see the reported effects of social media on emotional well being, and an interest in potentially creating a predictive model to determine factors attributed to certain emotions. 

The data was collected by "AI Inventor" Emirhan BULUT and licensed by MIT. The dataset required very minor cleaning in the form of reversing some values in the gender and age columns as they were reversed and removing one misc error. Directly from Kaggle, the data is pre-split into train, test, and validation datasets. For the regressions, the gender and dominant emotion columns I used pandas get_dummy as they are categorial to be usable for analysis.

# Impressions and Questions

## Visual Analysis

To get an initial look at the data provided I used my train.csv data for some basic visual analysis.

Starting off I wanted a brief idea of what my dataset looked like beyond the shape, so I totaled the responses through the dominant emotions category, which also gave me an idea of the general distributon of the emotions.

![Emotion Totals (Bar Chart)](/img/Emotion_Totals.png)

I then started exploring some potential contributing factors, starting with emotion reporting on the basis of gender. The three categories offered were male, female, and non-binary. We can see that female and male entries outnumber non-binary responses by a considerable margin, and that while males have a fairly uniform distribution across all emotional categories, females have a slight bias towards happiness and non-binary have a slight bias towards neutral.
  
![Emotions Based on Reported Gender (Stacked Bar Chart)](/img/Emotion_to_Gender.png)
  
Moving to age as a factor, by splitting age into 5 year incremental categories, it's apparent that the poll only reached ages 20-40. In the 20-25 age range, the majority feeling heavily lies in the nuetral category, 25-30 in the anxiety category, and 30-35 in the happy category. In the 35-40 age range there is extremely few entries comparitively, where only 3 categories were even selected, in which boredom is selected as equally as the other two categories combined. This data is included for visualization purposes, but if used in a regression alone for predictions in that age group, it would not be a good source of data for training a model.

![Emotion Based on Age (Stacked Bar Chart)](/img/Age_to_Emotion_Bar.png)

Correlating these two factors and emotions as well as daily usage, there is little to no correlation between any genders and emotions confirming what we saw in the gender comparison chart. However we do see that there is some correlation between reported daily usage and those who identified as female. Age has little correlation to any emotion, we can assume based on our previous observation that the correlation between age and boredom is likely skewed due to the smaller amount of entries in the 35-40 age range. Surprisingly, in this dataset there is a strong correlation between daily usage and happiness. This did bring into question potentially the manner in which and/or audience from which the data was collected as that information was not provided by the source.

![Age, Gender, and Daily Usage to Emotion Correlation](/img/Age_Gender_to_Emotion_Corr.png)

Another provided factor included the manner in which the social media was used. This included posts per day, likes recieved per day, messages sent per day, and comments recieved per day. There is a very strong positive correlation in increasing usage and happiness. The correlation matrix also shows that the higher the daily usage, the more likely it is that the participants would partake in each manner of use. Another correlation to note is that the higher the usage is, the more of a negative correlation there is with boredom and feeling nuetral.

![Social Media Usage Types and Amount to Emotion Correlation](/img/Use_to_Emotion_Corr.png)

The last factor considered was the effect of different social media platforms on emotions. The largest correlations are that Instagram users tend to be happier, LinkdIn users tend to be bored, and Twitter users tend to be angry. Other not as strong correlations to note are Whatsapp users also tending to be more angry, Snapchat users tending to be more sad, and Facebook users being more neutral or anxious. 

![Social Media Platform to Emotion Correlation](/img/Platform_to_Emotion_Corr.png)

## Hypothesis Testing

My overall hypothesis was that time spent on social media has a direct effect on an individual's reported dominant emotion.

> Null Hypothesis (H<sub>0</sub>): The variances of "Daily_Usage_Time" are equal across different "Dominant_Emotion" groups.
Alternative Hypothesis (H<sub>a</sub>): At least one group has a variance that is different from the others.

To test this, I first tested all emotions to the amount of time spent on social media using the Pearson correlation.

    Pearson correlation coefficient: -0.5396408800429509
    P-value: 1.1931272746862407e-76

    Interpretation: A correlation coefficient close to 1 or -1 indicates a strong relationship.
    A p-value < 0.05 indicates the correlation is statistically significant.

This can be interpeted as a somewhat strong correlation between emotional state and amount of time spent on social media. Rather than accepting this, I used the Pearson correlation to test total amount of time spent on social media against each emotion individually to see if any emotions had a stronger correlation than others.

    Emotion Value: Happiness
    Correlation coefficient: 0.7024025007688279
    P-value: 1.571471817667403e-149
    ------------------------------
    Emotion Value: Anger
    Correlation coefficient: -0.05923116918731677
    P-value: 0.061157451336261916
    ------------------------------
    Emotion Value: Neutral
    Correlation coefficient: -0.23434877202553017
    P-value: 6.084063775083197e-14
    ------------------------------
    Emotion Value: Anxiety
    Correlation coefficient: -0.004216313536894743
    P-value: 0.8940625955767559
    ------------------------------
    Emotion Value: Boredom
    Correlation coefficient: -0.3327183742368559
    P-value: 2.8281079416464923e-27
    ------------------------------
    Emotion Value: Sadness
    Correlation coefficient: -0.13712020972567962
    P-value: 1.3535336135392227e-05
    ------------------------------

    Interpretation: A correlation coefficient close to 1 or -1 indicates a strong relationship.
    A p-value < 0.05 indicates the correlation is statistically significant.

From this we can gather that happiness, nuetral, boredom, and sadness maintain a statistically significant correlation, with happiness having the strongest relationship. 

## Regressions

# Further Expansion
  *Explanation here*

# Why Should Individuals Take Interest?
  *Explanation here*

# How To Replicate My Work
  *Explanation here*

* Image Template as follows
```
*Explanation here*

![](/img/)
```