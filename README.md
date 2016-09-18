From our project description on Devpost

Working prototype with data for Las Vegas NV is available here:

https://www.airmanopus.net/hackthenorth2016/

## Inspiration

There are a number of different symptoms and treatment strategies for Post Traumatic Stress Disorder (PTSD); while a full description of each is beyond the scope of this project, one of the hardest symptoms to overcome is that of avoidance. It is often easier to avoid a potential or triggering environment than to face it, but facing triggers is ultimately the only way to diminish their importance (as well as the problems avoidance causes). 

It is often the unexpected events and situations that are the hardest to cope with-- one minute an environment is stable, and the next it's full of triggers. Avoiding all difficult situations is the wrong answer since doing so makes things worse, but it is also important to be able to pick one's battles.

## What it does

Since it is difficult to tell what an environment is like from a map or even from standing outside and looking in, we use reviews written by people and submitted to Yelp. Using the text of the reviews we can use sentiment and emotional analysis to find the reviews that indicate that the author was feeling certain emotions when writing the review of a place. Often, the emotions of fear and anger that can be identified in Yelp reviews are similar to the same emotions that accompany PTSD symptoms.  By identifying locations that might be triggering we offer an option for someone to PTSD to compare the emotions they are feeling at a location to those of other people, and make a more rational decision in responding to those emotions.

This is similar to the process used to treat PTSD, involving mindfulness and cognitive processing therapy to challenge the assumptions that PTSD introduces in response to stimuli.

## How we built it

Our primary data source was Yelp, specifically the data available at yelp.com/dataset_challenge. Shamya used Python to filter the Yelp data to extract the text of reviews of each place, and then pass the reviews to the IBM Alchemy API for sentiment and emotional analysis. "Fear" was a major factor in identifying reviews of places where review authors felt strong emotions that would apply to someone experiencing PTSD symptoms at the same location.

## Challenges we ran into

There are over 2.7 million reviews in the dataset offtered by Yelp; student-class laptops turned out to be not quite fast enough, and we rapidly reached the transaction limits of the Alchemy API. Ideally we'd like to be able to make information available on all of the locations listed in Yelp's data so that the application would work anywhere that has had Yelp reviews written for it. For this weekend, we had to limit the data we used to a specific location (Las Vegas NV) to be able to process enough to display meaningful output reasonably quickly.

## Accomplishments that we're proud of

Using existing data in a new way-- although Yelp reviews are meant to only describe individuals experiences at businesses and other places, they can include other information that can be useful. Alchemy allowed us to see Yelp's reviews differently and apply the result to a problem that affects many people, including (but certainly not limited to) military veterans. 

## What we learned

You can't put 2.7 million reviews into an API that only lets you process 1,000 requests at a time without making some changes to your approach. Maybe we knew that already though.

In our planning discussion, and in deciding how to display data and what functions to include, the problem of displaying the results of applying machine learning and analysis to text data is a deep and complicated one. We used a heatmap to illustrate our data, but the colors used and how they appear on a map made a difference between useful information and just showing dots on a map.

## What's next for Stress Radar

Still working on adding the button to allow a user to add how they're feeling at a particular location; this input will be used as another input to calculating the score a location receives. More coding needed to finish the auto adjustment that will happen if people indicate they feel non-stressed at a location that the Yelp reviews or open crime data indicate are potentially triggering. The idea is to maximize the amount of available human input as a check against inaccuracy in the results of processing the Yelp reviews.
