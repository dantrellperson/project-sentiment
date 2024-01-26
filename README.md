# project sentiment

I want to build an aspect identification model that:

1. Identifies the key topics (aspects) of customer reviews regardless of if the review is very short or has multiple sentences.
2. Identifies the sentiment of each topic found per review on a scale ranging from: very negative, negative, neutral, positive, very positive
3. Prioritize finding the reason (descriptors) that cause the aspect to be classified as positive or negative. For example take the following review: “Clean, good location Clean, good location with many restaurants, shopping near. Rooms are small, suggest requesting double beds for extra room. A/C did not cool well. Trash bins in lobby and out front overflowing/nasty. I would give 3.5 if an option.” Let’s say one of the aspects found from this review is “A/C” from the sentence “A/C did not cool well”, I would want to identify “not well” or “not cool” cause those words are obviously the reason it’s being classified as negative.

=

## exploring different areas of text analytics.

_Looking to learn more about text analytics. My overall goal is to train an accurate sentiment analyzer_

\*custom created dataset of gathered hotel reviews

## methods I'm exploring

- find a python package made for this type of analysis
- create own custom code to handle this task

## steps

### Data Collection

- Gather hotel reviews from tripadvisor

### 1. Aspect Extraction

- **Objective:** Extract aspects (key topics) from each review.

### 2. Sentiment Analysis

- **Objective:** Determine the sentiment for each identified aspect within the review.

### 3. Descriptor Identification

- **Objective:** Identify specific words or phrases in the text that influence the sentiment of an aspect.

### Implementation Plan:

1. **Preprocessing:** Clean the text data, handling different sentence structures, especially for longer reviews.
2. **Aspect Extraction:** Implement a model to extract aspects from each review.
3. **Sentiment Analysis:** For each extracted aspect, analyze the sentiment of the text surrounding it.
4. **Descriptor Identification:** Utilize dependency parsing to identify the words or phrases causing the sentiment.
